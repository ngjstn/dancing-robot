"""
This file was used to test various dance positions and function
"""
#import libraries
import time
from tracemalloc import start
import board
import pwmio
from adafruit_motor import servo

#set Pin Assignments
SERVO_LEFT_1 = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
SERVO_LEFT_2 = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
SERVO_RIGHT_1 = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
SERVO_RIGHT_2 =pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

#declare global variables
startPos = 40
pos = startPos    
endPos = 120
flatPos = 90
left1Offset = 10
left2Offset = 0
right1Offset = 5
right2Offset = 0
footTilt = 10

left1servo = servo.Servo(SERVO_LEFT_1)
left2servo = servo.Servo(SERVO_LEFT_2)
right1servo = servo.Servo(SERVO_RIGHT_1)
right2servo = servo.Servo(SERVO_RIGHT_2)

def crab_dance(walking:bool):
  while walking:
    #set flat
    left2servo.angle(flatPos + left2Offset - footTilt)
    right2servo.angle(flatPos + right2Offset + footTilt)
    left1servo.angle(flatPos + left1Offset)
    right1servo.angle(flatPos + right1Offset)
    
    for pos in range(flatPos, footTilt):
      left1servo.angle(pos+ left1Offset)
      right1servo.angle(pos + right1Offset)
      time.sleep(15/1000)
    
    for pos in range(footTilt, flatPos):
      left1servo.angle(pos+ left1Offset)
      right1servo.angle(pos + right1Offset)          
      time.sleep(15/1000);                       
  
    

