
<div  align=center>
	<h1>STM32 Waste Manager
	<br>
     <img src="https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/5e81f52e-1c94-4d24-b2ba-aa5fd0a254bb" height="40px" width="60px">
    <img src = "https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/9f32097b-f8bb-46ff-9397-9e1bde9c632e" height="40px" width="40px">
    <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/294f8741-c4a2-4b7c-be57-5f69f1c9fa5e" height="40px" width="120px">
	<br>
	</h1>
	<h3><b><a href="https://youtu.be/knVAxiWxsZU">View Our Demonstration Video</a></b></h3>
  <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/blob/main/demo.gif">
</div>




## Description
We were inspired by the UofT garbage cans. 

 <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/e2b4fe69-1f78-4627-b645-14b6705c03af" height="400px" width="400px">
 
If you ever look inside one of them, people are clearly not sorting according to the labeled categories... 
### What if a computer could do the sorting for you?

We used the STM LQFP144 microcontroller (through a STM32 Nucleo-F446ZE development board) to stream image data from an OV7670 camera module in RGB QQVGA format to a computer on which A ML model performed image classification into one of the 4 waste categories (Garbage, Paper, Containers, or Coffee Cups). We then rotate a "chute" to allow a person to throw their garbage away, using servo motors. We control 4 servo motors with one PWM signal by using transistors.

 <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/d09726ce-0833-41b5-9937-e740d9fde19b" height="500px" width="500px">



