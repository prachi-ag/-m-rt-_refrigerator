# Smart_refrigerator


                                                          Assignment 
                                                    Capstone Final Project

This is the capstone project to summarize all the learnings in the 3 modules of the course and to give you practical hands-on experience by working on a major project using Bolt IOT module.


## Working principle

A) Creation of an account and configuration for SMS on Twilio<br>
B) Creation of an acount and configuration for Email on Mailgun<br>
C) Login in your Oracle VM (VirtualBox) or in your digital ocean<br>
D) Code writing in python<br>
E) Running code and view the output<br>
F) Ending with receives the SMS and the Email <br>


### Components:
1) Bolt IoT module
2) LM-35
3) Jumper Wires(Male/Female)
4) USB cable
5) Breadboard(optional)

## API's used: 
   MailGun Email API, Bolt Cloud API, Python Library, Twilio API

### Connecting the LM35 to the bolt module
1. VCC pin of the LM35 connects to 5v of the Bolt Wifi module.<br>
2. Output pin of the LM35 connects to A0 (Analog input pin) of the Bolt Wifi module.<br>
3.Gnd pin of the LM35 connects to the Gnd.<br>

## The algorithm for the code can be broken down into the following steps:
a) Fetch the latest sensor value from the Bolt device.<br>
b) Store the sensor value in a list, that will be used for computing z-score.<br>
c) Compute the z-score and upper and lower threshold bounds for normal and anomalous readings.<br>
d) Check if the sensor reading is within the range for normal readings, then send email.<br>
e) If it is not in range, send the SMS.<br>
f) Wait for 10 seconds.<br>
g) Repeat from step a.<br>

![Hardware Setup](https://github.com/prachi-ag/Smart_refrigerator/blob/master/moduleSetUp_bb.png)

## Output of Prediction using Polynomial Regression
![Hardware Setup](https://github.com/prachi-ag/Smart_refrigerator/blob/master/Screenshot%20(7).png)


## Alert! Sms using Twilio API
![Hardware Setup](https://github.com/prachi-ag/Smart_refrigerator/blob/master/twilio_Sms_Alert.jpeg)

## Alert! Email using mailGun API
![Hardware Setup](https://github.com/prachi-ag/Smart_refrigerator/blob/master/mailgun_email_Alert.jpeg)

ThankYou!
