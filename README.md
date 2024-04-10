
<div  align=center>
	<h1>STM32 Waste Manager
	<br>
     <img src="https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/5e81f52e-1c94-4d24-b2ba-aa5fd0a254bb" height="40px" width="60px">
    <img src = "https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/9f32097b-f8bb-46ff-9397-9e1bde9c632e" height="40px" width="40px">
    <img src = "https://github.com/macaroonforu/STM32-Waste-Manager/assets/121368271/294f8741-c4a2-4b7c-be57-5f69f1c9fa5e" height="40px" width="120px">
	<br>
	</h1>
  <h3><b>By Thardchi Ganesalingam and Claire Dimitriuc</b></h3>
	<h3><b><a href="https://devpost.com/software/ferrofetcher">View Devpost Submission</a></b></h3>
  
</div>

## Description

A joystick-controlled Arduino robot developed at MakeUofT on February 17-18, 2024 that picks up magnetic objects using an electromagnet and pulley system.The joystick by default controls the wheels of the robot, but after pressing a button, an electromagnet is turned on, and the joystick controls the motion of the pulley instead. 

## Motion Demo


## Electromagnet 

## Future Hopes 
One weakness of the robot was that the L298N motor driver -which powered both the pulley and the electromagnet- did not send enough current through the electromagnet for it to be as strong and effective as we had hoped. To fix this, we intended to add an NMOS transistor that would operate as a switch. When we wanted the magnet to be on, we would apply a gate voltage using digitalWrite from the Arduino and allow current to flow from a separate 9V battery through the copper wire, but otherwise, the transistor would cut off the 9V from the copper wires. Shown on the breadboard is a circuit that was in progress, but not fully complete, where we intended to detect a button press using the 5V supply from the Arduino (would have been easily implemented with our previous circuit), and if the button press was detected, then send a gate voltage to the NMOS through an Arduino output logic pin to turn it on. The copper wire would have been connected across the two wires circled in orange as shown, but was temporarily being modelled as an 10k resistor in series with an LED. It would have interfaced very nicely with our main circuit, as the joystick movement was also being controlled using a button, but we were unable to add it in time for the deadline of the hackathon, and were also concerned for the implications it would have on the electromagnet's motion. 

<div  align=center>
	<img src="https://github.com/macaroonforu/makeuoft2024/assets/121368271/e8659b24-408d-47e8-a7e2-393f7b857645" width="500px">
  <img width="255" alt="image" src="https://github.com/macaroonforu/makeuoft2024/assets/121368271/0f899276-f2ac-4e2d-918f-be45a8654f21">

</div>




