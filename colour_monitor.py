import time
import cv2 as cv
import numpy as np
from serial import Serial
from model2 import predict_garbage_class

PORT = "COM3"
BAUDRATE = 115200
PREAMBLE = "!START!\r\n"
AI_PREAMBLE = "!AIIII!\r\n"
ROWS = 120
COLS = 160
SAVE_DIR = "ai_images/img.jpg"

def monitor(port: str, baudrate: int,timeout: int, rows: int, cols: int, preamble: str, ai_preamble: str, quiet: bool):
    """Display images transferred through serial port. Press 'q' to close."""
    prev_frame_ts = None  #keep track of frames per second
    print('\x1b[6;30;43m' + f'\t\tOpening communication on port {port} with baudrate {baudrate}' + '\x1b[0m') 

    with Serial(port, baudrate, timeout) as ser:
        while True:
            if not quiet:
                print("\nWaiting For Input Data")
            ai_image = wait_for_ai(ser, preamble.encode("ascii"), ai_preamble.encode("ascii"))
    
            if(ai_image): 
                print('\x1b[6;30;41m' + 'AI Image Detected' + '\x1b[0m') 
            else: 
                print('\x1b[6;30;42m' + 'Normal Image Detected' + '\x1b[0m')
            
            if not quiet:
                print("Receiving picture...")
            try:
                raw_data = ser.read(3*rows*cols)  
                if not quiet:
                    print(f"Received {len(raw_data)} bytes")
            except ValueError as e:
                print(f"Error while waiting for frame data: {e}")
            try:
                new_frame = np.frombuffer(raw_data, dtype=np.uint8).reshape(rows, cols, 3)[: , : , ::-1] #convert from RGB to BGR for openCV
            except ValueError as e:
                print(f"Malformed frame. {e}")
                continue

            if ai_image: 
                cv.imwrite(SAVE_DIR, new_frame)
                print(f"Running Inference on: {SAVE_DIR}")
                predicted_class, prediction = predict_garbage_class(SAVE_DIR)
                print('Predicted Category:' + '\t\x1B[6;30;105m' + f'{predicted_class}''\x1B[0m\n')
                ser.write(str(prediction).encode('ascii'))

            else:
                now = time.time()
                if prev_frame_ts is not None:
                    try:
                        fps = 1 / (now - prev_frame_ts)
                        print(f"Frames per second: {fps:.2f}")
                    except ZeroDivisionError:
                        print("FPS too fast to measure")
                prev_frame_ts = now
    
            cv.namedWindow("Video Stream", cv.WINDOW_KEEPRATIO)
            cv.imshow("Video Stream", new_frame)
            if cv.waitKey(1) == ord("q"):
                break
    cv.destroyAllWindows()

def wait_for_ai(ser: Serial, preamble: str, ai_preamble: str) -> bool:
    """
    Wait for a preamble string in the serial port. 
    Returns `True` if it's an AI frame, `False` if it's a normal frame
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

def main(): 
    print('\n\t\t\t\x1b[6;30;46m' + 'WELCOME TO OUR ECE342 PROJECT DEMO' + '\x1b[0m\n') 
    monitor(port=PORT, baudrate=BAUDRATE, timeout=8, rows=ROWS, cols=COLS,  preamble=PREAMBLE, ai_preamble=AI_PREAMBLE, quiet=False)

main()
