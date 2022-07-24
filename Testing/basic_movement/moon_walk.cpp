//This file is a template for the moon_walk dance of the robot first dance function we created
#include "PinAssignments.h"
#include "Libraries.h"

Servo left1servo; // Offset +10
Servo left2servo;
Servo right1servo;  // Offset +5
Servo right2servo;

int startPos = 40;
int pos = startPos;    // variable to store the servo position
int endPos = 120;
int flatPos = 90;
int left1Offset = 10;
int left2Offset = 0;
int right1Offset = 5;
int right2Offset = 0;
int footTilt = 8;

/**
 * @brief setup motors for the moon_walk function
 * 
 */
void moon_walk_setup() {
  left1servo.attach(SERVO_LEFT_1);
  left2servo.attach(SERVO_LEFT_2);
  right1servo.attach(SERVO_RIGHT_1);
  right2servo.attach(SERVO_RIGHT_2);

}

/**
 * @brief do the moon walk function
 * 
 */
void moon_walk(){
 
  left2servo.write(flatPos + left2Offset - footTilt);
  right2servo.write(flatPos + right2Offset + footTilt);
  left1servo.write(flatPos + left1Offset);
  right1servo.write(flatPos + right1Offset);
  for (pos = startPos; pos <= endPos; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    //left1servo.write(pos);
    left2servo.write(pos);
    //right1servo.write(pos);
    right2servo.write(endPos + (startPos - pos));
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  left1servo.write(flatPos + left1Offset + footTilt);
  right1servo.write(flatPos + right1Offset - footTilt);
  
  for (pos = endPos; pos >= startPos; pos -= 1) { // goes from 180 degrees to 0 degrees
    //left1servo.write(pos);
    left2servo.write(pos);
     //right1servo.write(pos);
    right2servo.write(endPos + (startPos - pos));            // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }


}
