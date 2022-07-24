//this file was used to test servo's for the 
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
 * @brief move the servos to do the crab rave dance this function is a WIP
 * 
 */
void rave(){
 
  left2servo.write(flatPos + left2Offset - footTilt);
  right2servo.write(flatPos + right2Offset + footTilt);
  left1servo.write(flatPos + left1Offset);
  right1servo.write(flatPos + right1Offset);
//   for (pos = startPos; pos <= endPos; pos += 1) { // goes from 0 degrees to 180 degrees
//     // in steps of 1 degree
//     //left1servo.write(pos);
//     left2servo.write(pos);
//     //right1servo.write(pos);
//     right2servo.write(endPos + (startPos - pos));
//     delay(15);                       // waits 15ms for the servo to reach the position
//   }
//   left1servo.write(flatPos + left1Offset + footTilt);
//   right1servo.write(flatPos + right1Offset - footTilt);
  
//   for (pos = endPos; pos >= startPos; pos -= 1) { // goes from 180 degrees to 0 degrees
//     //left1servo.write(pos);
//     left2servo.write(pos);
//      //right1servo.write(pos);
//     right2servo.write(endPos + (startPos - pos));            // tell servo to go to position in variable 'pos'
//     delay(15);                       // waits 15ms for the servo to reach the position
//   }


}
