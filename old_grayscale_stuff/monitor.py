import time
import cv2 as cv
import numpy as np
from serial import Serial
from model_grayscale import predict_garbage_class

PORT = "COM3"
BAUDRATE = 115200
PREAMBLE = "!START!\r\n"
SUFFIX = "!END!\r\n"
AI_PREAMBLE = "!AIIII!\r\n"
ROWS = 144
COLS = 174
SAVE_DIR = "ai_images/"

def monitor(port: str, baudrate: int,timeout: int, rows: int, cols: int, preamble: str, ai_preamble: str, suffix: str, quiet: bool):
    """
    Display images transferred through serial port. Press 'q' to close.
    """
    prev_frame_ts = None  # keep track of frames per second

    print(f"Opening communication on port {port} with baudrate {baudrate}")

    if isinstance(suffix, str):
        suffix = suffix.encode("ascii")

    if isinstance(preamble, str):
        preamble = preamble.encode("ascii")

    if isinstance(ai_preamble, str):
        ai_preamble = ai_preamble.encode("ascii")

    img_rx_size = rows * cols

    with Serial(port, baudrate, timeout=timeout) as ser:
        while True:
            if not quiet:
                print("Waiting for input data...")
            ai_image = wait_for_ai(ser, preamble, ai_preamble)

            if(ai_image): 
                print('\x1b[6;30;41m' + 'ai image received' + '\x1b[0m') 
            else: 
                print('\n' + '\x1b[6;30;42m' + 'normal image received' + '\x1b[0m')
            
            if not quiet:
                print("Receiving picture...")

            try:
                raw_data = get_raw_data(ser, img_rx_size, suffix)
                if not quiet:
                    print(f"Received {len(raw_data)} bytes")
            except ValueError as e:
                print(f"Error while waiting for frame data: {e}")

            try:
                new_frame = load_raw_frame(raw_data, rows, cols)
            except ValueError as e:
                print(f"Malformed frame. {e}")
                continue
        
            now = time.time()
            if prev_frame_ts is not None:
                try:
                    fps = 1 / (now - prev_frame_ts)
                    print(f"Frames per second: {fps:.2f}")
                except ZeroDivisionError:
                    print("FPS too fast to measure")
            prev_frame_ts = now

            if ai_image: 
                filename = SAVE_DIR + f"test.jpg"
                cv.imwrite(filename, new_frame)
                print(f"Image saved as: {filename}")
                print(f"Running inference ...")
                predicted_class, prediction = predict_garbage_class(filename)
                print(f"\nPredicted class: {predicted_class}\n")
                ser.write(str(prediction).encode('ascii'))

            cv.namedWindow("Video Stream", cv.WINDOW_KEEPRATIO)
            cv.imshow("Video Stream", new_frame)

            # Wait for 'q' to stop the program
            if cv.waitKey(1) == ord("q"):
                break
    cv.destroyAllWindows()


def wait_for_ai(ser: Serial, preamble: str, ai_preamble: str) -> bool:
    """
    Wait for a preamble string in the serial port.
    Returns `True` if next frame is full, `False` if it's a partial update.
    """
    while True:
        try:
            line = ser.readline()
            if line == preamble:
                return False 
            elif line == ai_preamble:
                return True
        except UnicodeDecodeError:
            pass


def get_raw_data(ser: Serial, num_bytes: int, suffix: bytes = b"") -> bytes:
    """
    Get raw frame data from the serial port.
    """
    rx_max_len = num_bytes + len(suffix)
    max_tries = 10_000
    raw_img = b""

    for _ in range(max_tries):
        raw_img += ser.read(max(1, ser.in_waiting))

        suffix_idx = raw_img.find(suffix)
        if suffix_idx != -1:
            raw_img = raw_img[:suffix_idx]
            break

        if len(raw_img) >= rx_max_len:
            raw_img = raw_img[:num_bytes]
            break
    else:
        raise ValueError("Max tries exceeded.")

    print(len(raw_img))
    return raw_img



def load_raw_frame(raw_data: bytes, rows: int, cols: int) -> np.array:
    return np.frombuffer(raw_data, dtype=np.uint8).reshape((rows, cols, 1))

def main(): 
    #port = input("Enter the port you are using")
    monitor(port=PORT, 
            baudrate=BAUDRATE, 
            timeout=1, 
            rows=ROWS, 
            cols=COLS, 
            preamble=PREAMBLE,
            ai_preamble=AI_PREAMBLE,  
            suffix=SUFFIX, 
            quiet=False 
    )

main() 
   
