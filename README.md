# Smart_refrigerator


                                                          Assignment 
                                                    Capstone Final Project

This is the capstone project to summarize all the learnings in the 3 modules of the course and to give you practical hands-on experience by working on a major project using Bolt IOT module.


## Working principle

A) Creation of an account and configuration for SMS on Twilio
B) Creation of an acount and configuration for Email on Mailgun
C) Login in your Oracle VM (VirtualBox) or in your digital ocean
D) Code writing in python
E) Runing code and view the output
F) Ending with receives the SMS and the Email 


### Components:
1) Bolt IoT module
2) LM-35
3) Jumper Wires(Male/Female)

## API's used: 
   MailGun Email API, Bolt Cloud API, Pyhon Library, Twilio API

### Connecting the LM35 to the bolt module
1. VCC pin of the LM35 connects to 5v of the Bolt Wifi module.
2. Output pin of the LM35 connects to A0 (Analog input pin) of the Bolt Wifi module.
3.Gnd pin of the LM35 connects to the Gnd.

![Hardware Setup](https://github.com/prachi-ag/Smart_refrigerator/blob/master/moduleSetUp_bb.png)

## Output of Prediction using Polynomial Regression
![Hardware Setup](https://github.com/prachi-ag/Smart_refrigerator/blob/master/Screenshot%20(7).png)


## Alert! Sms using Twilio API
![Hardware Setup](https://github.com/prachi-ag/Smart_refrigerator/blob/master/twilio_Sms_Alert.jpeg)

## Alert! Email using mailGun API
![Hardware Setup](https://github.com/prachi-ag/Smart_refrigerator/blob/master/mailgun_email_Alert.jpeg)
