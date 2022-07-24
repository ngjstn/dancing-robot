//This file was used for general servo instantiation by the arduino file it is currently incomplete as it was not used
#include "PinAssignments.h"
#include "Libraries.h"

Servo left1servo; // Offset +10
Servo left2servo;
Servo right1servo;  // Offset +5
Servo right2servo;

void walk_setup() {
  left1servo.attach(SERVO_LEFT_1);
  left2servo.attach(SERVO_LEFT_2);
  right1servo.attach(SERVO_RIGHT_1);
  right2servo.attach(SERVO_RIGHT_2);

}
