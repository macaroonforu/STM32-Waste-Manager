
<div  align=center>
	<h1>STM32 Waste Manager
	<br>
    <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/379d9473-53e4-4c29-9e3c-34c27add8541" height="40px" width="50px">
    <img src="https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/5e81f52e-1c94-4d24-b2ba-aa5fd0a254bb" height="40px" width="60px">
    <img src = "https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/9f32097b-f8bb-46ff-9397-9e1bde9c632e" height="40px" width="40px">
    <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/294f8741-c4a2-4b7c-be57-5f69f1c9fa5e" height="40px" width="120px">
	<br>
	</h1>
	<h3><b><a href="https://youtu.be/knVAxiWxsZU">View Our Demonstration Video</a></b></h3>
  <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/blob/main/demo.gif">
</div>




## Description
We were inspired by the current waste sorting scheme on the garbage cans at the University of Toronto. Often, people don't have the time to take a look at what is in their hand and read all the labels to make sure they put it in the right bin, so they just end up throwing it in a random one. 
<div  align=center>
 <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/e2b4fe69-1f78-4627-b645-14b6705c03af" height="400px" width="400px">
</div>
 
## How could a microcontroller fix this problem?

We used the LQFP144 microcontroller (through a STM32 NUCLEO-F446ZE development board) to collect YUV image data in QQVGA resolution from an OV7670 camera module, which was then converted to RGB format and streamed to a computer (via UART), where it was displayed on a "monitor" using openCV library. 

We used Resnet (a pretrained convolutional neural network for image classification) to implement a simple classifier by replacing the last layer with a linear layer for classification that would sort the image into one of the 4 waste categories (Garbage, Paper, Containers, or Coffee Cups), then send the predicted class back to the microcontroller. 


The microcontroller then writes this prediction to an LCD display as a visual cue for the user, then turns on the proper servo motor which rotates an opening to allow a person to throw their garbage away. Each servo motor is controlled through a transistor that has a GPIO output pin connected to its base, 5V connected to the collector, and VDD for the servo connected to its emitter. The GPIO output pins connected to the bases of the transistors allow them to be used as switches, so that power can be supplied-to and cut-off from the servo motors by writing high/low signals to the GPIO pins. Since all 4 motors share the same PWM signal (adjusting the duty cycle of this signal through software enables CW/CCW rotation), transistors ensure only one will ever rotate at a time because only one will ever be one at a time. 



<div align=center>
 <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/d09726ce-0833-41b5-9937-e740d9fde19b" height="500px" width="500px">
</div>

## Connections to the microcontroller 
<div align=center>
 <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/86754468-ee91-4c28-8a6c-17869651d7a7" height="500px" width="659px">
</div>

## Future Improvement 
<h4><b><a href="https://colab.research.google.com/drive/1ROumRpmJ9ZZQu_F84963ObqwUeS4Fjj7?usp=sharing">Colab Training Notebook</a></b></h4>

The ML model was not the main focus of the project, so we would like to increase its accuracy and ability to differentiate paper coffee cups from mixed paper and containers.
<div align = center>
<img width="350" alt="image" src="https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/c682e3b8-9ee7-4dab-9786-cbcceea0e134">
<img width="350" alt="image" src="https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/c1c998ea-3c6c-47ea-af62-f659a66044a5">
<img width="350" alt="image" src="https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/bf8a1e9b-8c59-4439-8603-922620751d7e">
<img width="350" alt="image" src="https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/13ca90b1-b415-45e8-bb8d-c9f1ef98c673">
</div>

We would also like to have inference be run on the microcontroller instead of on a computer, and to stream camera data to a TFT LCD display so the system can be fully offline. 

## Credits 
<h4><b><a href="https://controllerstech.com/servo-motor-with-stm32/">Controlling Servo Motors</a></b></h4>
<h4><b><a href="https://www.micropeta.com/video61/">I2C LCD Driver</a></b></h4>
<h4><b><a href="https://embeddedprogrammer.blogspot.com/2012/07/hacking-ov7670-camera-module-sccb-cheat.html">OV7670 Info</a></b></h4>
<h4><b><a href="https://fourcc.org/fccyvrgb.php">YUV-RGB Conversion</a></b></h4>

