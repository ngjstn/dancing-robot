"""
This file contains the defintion for the first dance we created called moon_walk()
"""
import time
import board
import pwmio
from adafruit_motor import servo

SERVO_LEFT_1 = pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
SERVO_LEFT_2 = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)
SERVO_RIGHT_1 = pwmio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)
SERVO_RIGHT_2 =pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

startPos = 40
pos = startPos    
endPos = 120
flatPos = 90
left1Offset = 10
left2Offset = 0
right1Offset = 5
right2Offset = 0
footTilt = 8

left1servo = servo.Servo(SERVO_LEFT_1)
left2servo = servo.Servo(SERVO_LEFT_2)
right1servo = servo.Servo(SERVO_RIGHT_1)
right2servo = servo.Servo(SERVO_RIGHT_2)

def moon_walk(walking:bool):
  while walking:
    left2servo.angle = (flatPos + left2Offset - footTilt)
    right2servo.angle = (flatPos + right2Offset + footTilt)
    left1servo.angle = (flatPos + left1Offset)
    right1servo.angle = (flatPos + right1Offset)
    for pos in range(startPos, endPos):
      left2servo.angle = (pos)
      right2servo.angle = (endPos + (startPos - pos))
      time.sleep(15/1000)
    
    left1servo.angle = (flatPos + left1Offset + footTilt)
    right1servo.angle = (flatPos + right1Offset - footTilt)
    
    for pos in range(endPos, startPos):
      left2servo.angle = (pos)
      right2servo.angle = (endPos + (startPos - pos));            
      time.sleep(15/1000);                       
  
moon_walk(True)
    

