# import board
# from adafruit_st7735r import ST7735R
# from adafruit_display_text import label
# import adafruit_imageload
# import displayio
# import simpleio
# import PWMOut
# import pwmio
# import pulseio
# import time
# import digitalio
# import adafruit_matrixkeypad

# # Create piezo buzzer PWM output.
# buzzer = pwmio.PWMOut(board.D10, variable_frequency=True)


# cols = [digitalio.DigitalInOut(x) for x in (board.A2, board.A3, board.A4)]
# rows = [digitalio.DigitalInOut(x) for x in (board.A0, board.A1, board.D3, board.D4)]
# keys = ((1, 2, 3),
#         (4, 5, 6),
#         (7, 8, 9),
#         ('*', 0, '#'))

# keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

# notes = {
#     "rest" : 20000,
#     "C2" : 65.41,
#     "C#2" : 69.3,
#     "D2" : 69.3,
#     "D#2" : 77.78,
#     "E2" : 82.41,
#     "F2" : 87.31,
#     "F#2" : 92.50,
#     "G2" : 98.0,
#     "G#2" : 103.83,
#     "A2": 110.00,
#     "A#2" : 116.54,
#     "B2" : 123.47,
#     "C3" : 146.83,
#     "C#3" : 138.59,
#     "D3" : 146.83,
#     "D#3" : 155.56,
#     "E3" : 164.81,
#     "F3" : 174.61,
#     "F#3" : 185.00,
#     "G3" : 196.00,
#     "G#3" : 207.65,
#     "A3": 220.00,
#     "A#3" : 233.08,
#     "B3" : 246.94,
#     "C4" : 261.63,
#     "C#4" : 277.18,
#     "D4" : 293.66,
#     "D#4" : 311.13,
#     "E4" : 329.63,
#     "F4" : 349.23,
#     "F#4" : 369.99,
#     "G4" : 392.00,
#     "G#4" : 415.30,
#     "A4": 440.00,
#     "A#4" : 466.16,
#     "B4" : 493.88,
#     "C5" : 523.25,
#     "C#5" : 554.37,
#     "D5" : 587.33,
#     "D#5" : 622.25,
#     "E5" : 659.25,
#     "F5" : 698.46,
#     "F#5" : 740.99,
#     "G5" : 783.99,
#     "G#5" : 830.61,
#     "A5": 880.00,
#     "A#5" : 932.33,
#     "B5" : 987.77
# }

# crab_rave = [("D5", 0.24),
#             ("A#5", 0.24),
#             ("G5", 0.24),
#             ("G5", 0.12),
#             ("D5", 0.24),
#             ("D5", 0.12),
#             ("A5", 0.24),
#             ("F5", 0.24),
#             ("F5", 0.12),
#             ("D5", 0.24),
#             ("D5", 0.12),
#             ("A5", 0.24),
#             ("F5", 0.24),
#             ("A5", 0.12),
#             ("C5", 0.24),
#             ("C5", 0.24),
#             ("E5", 0.24),
#             ("E5", 0.12),
#             ("F5", 0.24),
#             ("D5", 0.24),
#             ("A#5", 0.24),
#             ("G5", 0.24),
#             ("G5", 0.12),
#             ("D5", 0.24),
#             ("D5", 0.12),
#             ("A5", 0.24),
#             ("F5", 0.24),
#             ("F5", 0.12),
#             ("D5", 0.24),
#             ("D5", 0.12),
#             ("A5", 0.24),
#             ("F5", 0.24),
#             ("F5", 0.12),
#             ("C5", 0.24),
#             ("C5", 0.24),
#             ("E5", 0.24),
#             ("E5", 0.12),
#             ("F5", 0.24)]

# love_story = [("D5", 0.25),
#              ("D5", 0.25),
#              ("G5", 0.5),
#              ("F#5", 0.5),
#              ("D5", 0.5),
#              ("D5", 0.25),
#              ("E5", 0.25),
#              ("E5", 0.25),
#              ("D5", 0.25),
#              ("F#5", 0.25),
#              ("D5", 0.25),
#              ("E5", 0.5),
#              ("D5", 0.5),
#              ("E5", 0.5),
#              ("F#5", 0.5),
#              ("E5", 0.5),
#              ("D5", 0.25),
#              ("E5", 0.25),
#              ("E5", 0.25),
#              ("D5", 0.25),
#              ("F#5", 0.25),
#              ("D5", 0.25),
#              ("E5", 0.5),
#              ("D5", 0.5),
#              ("E5", 0.25),
#              ("D5", 0.25),
#              ("F#5", 0.5),
#              ("E5", 0.5),
#              ("D5", 0.5),
#              ("E5", 0.25),
#              ("D5", 0.25),
#              ("F#5", 0.5),
#              ("E5", 0.5),
#              ("D5", 0.25),
#              ("D5", 0.25),
#              ("E5", 0.5),
#              ("F#5", 0.25),
#              ("E5", 0.25),
#              ("F#5", 0.5),
#              ("F#5", 0.25),
#              ("E5", 0.25),
#              ("F#5", 0.5),
#              ("F#5", 0.5),
#              ("D5", 0.5)]

# rick_roll = [("F4", 45.0/113),
#             ("F4", 45.0/113),
#             ("D#4", 60.0/113),
#             ("rest", 30.0/113),
#             ("G#3", 15.0/113),
#             ("A#3", 15.0/113),
#             ("C4", 15.0/113),
#             ("A#3", 15.0/113),
#             ("D#4", 45.0/113),
#             ("D#4", 45.0/113),
#             ("C#4", 15.0/113),
#             ("C3", 15.0/113),
#             ("A#3", 45.0/113),
#             ("G#3", 15.0/113),
#             ("A#3", 15.0/113),
#             ("C#4", 15.0/113),
#             ("A#3", 15.0/113),
#             ("C#4", 45.0/113),
#             ("D#4", 45.0/113),
#             ("C3", 15.0/113),
#             ("A#3", 45.0/113),
#             ("G#3", 30.0/113),
#             ("rest", 15.0/113),
#             ("G#3", 30.0/113),
#             ("D#4", 60.0/113),
#             ("C#4", 60.0/113),
#             ("rest", 60.0/113),
#             ("G#3", 15.0/113),
#             ("A#3", 15.0/113),
#             ("C#4", 15.0/113),
#             ("A#3", 15.0/113),
#             ("F4", 45.0/113),
#             ("F4", 45.0/113),
#             ("D#4", 75.0/113),
#             ("rest", 15.0/113),
#             ("G#3", 15.0/113),
#             ("A#3", 15.0/113),
#             ("C4", 15.0/113),
#             ("A#3", 15.0/113),
#             ("G#4", 45.0/113),
#             ("C4", 45.0/113),
#             ("C#4", 30.0/113),
#             ("C4", 15.0/113),
#             ("A#3", 45.0/113),
#             ("G#3", 15.0/113),
#             ("A#3", 15.0/113),
#             ("C4", 15.0/113),
#             ("A#3", 15.0/113),
#             ("C#4", 45.0/113),
#             ("D#4", 45.0/113),
#             ("C4", 45.0/113),
#             ("A#3", 15.0/113),
#             ("G#3", 30.0/113),
#             ("rest", 30.0/113),
#             ("G#3", 30.0/113),
#             ("D#4", 30.0/113),
#             ("C#4", 30.0/113),
#             ("C#4", 60.0/113),
#             ("rest", 120/113)]

# wii_sports = [("D#4", 30/31),
#               ("E4", 30/31),
#               ("F#4", 45/124),
#               ("B4", 45/124),
#               ("A#4", 15/62),
#               ("B4", 45/124),
#               ("F#4", 45/124),
#               ("D#4", 15/62),
#               ("B3", 45/124),
#               ("C#4", 45/124),
#               ("D#4", 15/62),
#               ("C#4", 60/31),
#               ("rest", 30/31),
#               ("D#4", 30/31),
#               ("E4", 45/62),
#               ("D#4", 15/124),
#               ("E4", 15/124),
#               ("F#4", 45/124),
#               ("B4", 45/124),
#               ("C#5", 15/62),
#               ("B4", 45/62),
#               ("B4", 15/124),
#               ("C#5", 15/124),
#               ("E5", 45/124),
#               ("D#5", 45/124),
#               ("C#5", 15/62),
#               ("B4", 15/31),
#               ("F#4", 15/62),
#               ("G#4", 15/31),
#               ("C#5", 15/62),
#               ("C#5", 30/31),
#               ("rest", 15/62),
#               ("C#5", 15/124),
#               ("D#5", 15/124),
#               ("E5", 45/124),
#               ("D#5", 45/124),
#               ("C#5", 15/62),
#               ("B4", 15/31),
#               ("F#4", 60/32),
#               ("rest", 15/62),
#               ("C#5", 15/124),
#               ("D#5", 15/124),
#               ("E5", 45/124),
#               ("D#5", 45/124),
#               ("C#5", 15/62),
#               ("B4", 15/31),
#               ("F#5", 60/31),
#               ("rest", 15/31)]

# all_star = [("rest", 45/26),
#             ("F#4", 15/26),
#             ("C#5", 15/52),
#             ("A#4", 15/52),
#             ("A#4", 15/26),
#             ("G#4", 15/52),
#             ("F#4", 15/52),
#             ("F#4", 15/52),
#             ("B4", 15/26),
#             ("A#4", 15/52),
#             ("A#4", 15/52),
#             ("G#4", 15/52),
#             ("G#4", 15/52),
#             ("F#4", 15/52),
#             ("rest", 15/52),
#             ("F#4", 15/52),
#             ("C#5", 15/52),
#             ("A#4", 15/52),
#             ("A#4", 15/52),
#             ("G#4", 15/52),
#             ("G#4", 15/52),
#             ("F#4", 15/52),
#             ("F#4", 15/52),
#             ("D#4", 15/52), 
#             ("D#4", 15/52),
#             ("C#4", 15/26),
#             ("rest", 45/52),
#             ("F#4", 15/52),
#             ("F#4", 15/52),
#             ("C#5", 15/52),
#             ("A#4", 15/52),
#             ("A#4", 15/52),
#             ("G#4", 15/52),
#             ("G#4", 15/52),
#             ("F#4", 15/52),
#             ("F#4", 15/52),
#             ("B4", 15/26),
#             ("A#4", 15/52),
#             ("A#4", 15/52),
#             ("G#4", 15/52),
#             ("G#4", 15/52),
#             ("F#4", 15/52),
#             ("F#4", 15/52),
#             ("C#5", 15/52),
#             ("rest", 15/52),
#             ("A#4", 15/52),
#             ("A#4", 15/52),
#             ("G#4", 15/26),
#             ("F#4", 15/52),
#             ("F#4", 15/52),
#             ("G#4", 15/52),
#             ("G#4", 15/52), 
#             ("D#4", 45/52),
#             ("rest", 30/26),]

# running_in_the_90s = [("A4", 5/53),
#                       ("E4", 5/53),
#                       ("A4", 5/53),
#                       ("E5", 5/53),
#                       ("D5", 5/53),
#                       ("C5", 5/53),
#                       ("A4", 5/53),
#                       ("rest", 5/53),
#                       ("A4", 5/53),
#                       ("E4", 5/53),
#                       ("A4", 5/53),
#                       ("E5", 5/53),
#                       ("D5", 5/53),
#                       ("C5", 5/53),
#                       ("A4", 5/53),
#                       ("rest", 5/53),
#                       ("C5", 5/53),
#                       ("B4", 5/53),
#                       ("G4", 5/53),
#                       ("C5", 10/53),
#                       ("B4", 5/53),
#                       ("G4", 5/53),
#                       ("rest", 5/53),
#                       ("C5", 5/53),
#                       ("B4", 5/53),
#                       ("G4", 5/53),
#                       ("D5", 10/53),
#                       ("B4", 5/53),
#                       ("G4", 5/53),
#                       ("rest", 5/53),
#                       ("A4", 5/53),
#                       ("E4", 5/53),
#                       ("A4", 5/53),
#                       ("E5", 5/53),
#                       ("D5", 5/53),
#                       ("C5", 5/53),
#                       ("A4", 5/53),
#                       ("rest", 5/53),
#                       ("A4", 5/53),
#                       ("E4", 5/53),
#                       ("A4", 5/53),
#                       ("E5", 5/53),
#                       ("D5", 5/53),
#                       ("C5", 5/53),
#                       ("A4", 5/53),
#                       ("rest", 5/53), 
#                       ("C5", 5/53),
#                       ("C5", 5/53),
#                       ("rest", 5/53),
#                       ("C5", 5/53),
#                       ("D5", 5/53),
#                       ("rest", 5/53),
#                       ("D5", 5/53),
#                       ("rest", 5/53),
#                       ("E5", 5/53),
#                       ("E5", 5/53),
#                       ("rest", 5/53),
#                       ("E5", 5/53),
#                       ("D5", 5/53),
#                       ("rest", 5/53),
#                       ("D5", 5/53),
#                       ("rest", 5/53),
#                       ("A4", 5/53),
#                       ("E4", 5/53),
#                       ("A4", 5/53),
#                       ("E5", 5/53),
#                       ("D5", 5/53),
#                       ("C5", 5/53),
#                       ("A4", 5/53),
#                       ("rest", 5/53), 
#                       ("A4", 5/53),
#                       ("E4", 5/53),
#                       ("A4", 5/53),
#                       ("E5", 5/53),
#                       ("D5", 5/53),
#                       ("C5", 5/53),
#                       ("A4", 5/53),
#                       ("rest", 5/53),
#                       ("C5", 5/53),
#                       ("B4", 5/53),
#                       ("G4", 5/53),
#                       ("C5", 10/53),
#                       ("B4", 5/53),
#                       ("G4", 5/53),
#                       ("rest", 5/53),
#                       ("C5", 5/53),
#                       ("B4", 5/53),
#                       ("G4", 5/53),
#                       ("D5", 10/53),
#                       ("B4", 5/53),
#                       ("G4", 5/53),
#                       ("rest", 5/53),
#                       ("A4", 5/53),
#                       ("E4", 5/53),
#                       ("A4", 5/53),
#                       ("E5", 5/53),
#                       ("D5", 5/53),
#                       ("C5", 5/53),
#                       ("A4", 5/53),
#                       ("rest", 5/53),
#                       ("A4", 5/53),
#                       ("E4", 5/53),
#                       ("A4", 5/53),
#                       ("E5", 5/53),
#                       ("D5", 5/53),
#                       ("C5", 5/53),
#                       ("A4", 5/53),
#                       ("rest", 5/53),
#                       ("E5", 10/53),
#                       ("D#5", 10/53),
#                       ("D5", 10/53),
#                       ("C#5", 10/53),
#                       ("C5", 10/53),
#                       ("C#5", 10/53),
#                       ("D5", 10/53),
#                       ("D#5", 10/53)]

# com = [(False, False, True),
#         (False, True, False),
#         (False, True, True),
#         (True, False, False),
#         (True, False, True),
#         (True, True, False)]

# com0 = digitalio.DigitalInOut(board.D11)
# com1 = digitalio.DigitalInOut(board.D12)
# com2 = digitalio.DigitalInOut(board.D13)
# com0.direction = digitalio.Direction.OUTPUT
# com1.direction = digitalio.Direction.OUTPUT
# com2.direction = digitalio.Direction.OUTPUT

# playlist = [crab_rave, love_story, rick_roll, wii_sports, all_star, running_in_the_90s]
# song = 2
# # Release any resources currently in use for the displays
# displayio.release_displays()

# spi = board.SPI()
# tft_cs = board.D5
# tft_dc = board.D7

# display_bus = displayio.FourWire(
#     spi, command=tft_dc, chip_select=tft_cs, reset=board.D9
# )

# display = ST7735R(display_bus, width=128, height=128, rotation=90, bgr=True)

# imgFile = ["/Crab_Rave.bmp", "/taytay.bmp", "/rick_roll.bmp"]
# images = []

# for img in imgFile:
#     bitmap, palette = adafruit_imageload.load(img,
#                                             bitmap=displayio.Bitmap,
#                                             palette=displayio.Palette)

#     # Create a TileGrid to hold the bitmap
#     tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

#     # Create a Group to hold the TileGrid
#     group = displayio.Group()

#     # Add the TileGrid to the Group
#     group.append(tile_grid)
#     images.append(group)

# # Start at the first note and start making sound.
# buzzer.frequency = round(notes[playlist[song][0][0]])
# buzzer.duty_cycle = 2**15  # 32768 value is 50% duty cycle, a square wave.
# com0.value = com[song][0]
# com1.value = com[song][1]
# com2.value = com[song][2]

# # Main loop will go through each tone in order up and down.
# while True:
#     if song < 3:
#         display.show(images[song])
#     # Play tones going from start to end of list.
#     for i in range(len(playlist[song])):
#          keys = keypad.pressed_keys
#          if keys:
#             song = keys[0] - 1
#             com0.value = com[song][0]
#             com1.value = com[song][1]
#             com2.value = com[song][2]
#             print(keys)
#             break
#          buzzer.frequency = round(notes[playlist[song][i][0]])
#          time.sleep(playlist[song][i][1])
#          buzzer.frequency = 20000
#          time.sleep(0.01)



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
    left2servo.angle = (flatPos + left2Offset)
    right2servo.angle = (flatPos + right2Offset)
    left1servo.angle = (flatPos + left1Offset - footTilt)
    right1servo.angle = (flatPos + right1Offset + footTilt)
    # for pos in range(startPos, endPos):
    #   left2servo.angle = (pos)
    #   right2servo.angle = (endPos + (startPos - pos))
    #   time.sleep(15/1000)
    pause
    while True:
        left1servo.angle = (flatPos + left1Offset - footTilt)
        right2servo.angle = (flatPos + right2Offset + 10)
        right1servo.angle = (flatPos + right1Offset + footTilt)
        time.sleep(1)
        left1servo.angle = (flatPos + left1Offset - footTilt - 60)
        right2servo.angle = (flatPos + right2Offset - 10)    
        right1servo.angle = (flatPos + right1Offset + footTilt + 60)
        time.sleep(1)
        
    
    # left1servo.angle = (flatPos + left1Offset + footTilt)
    # right1servo.angle = (flatPos + right1Offset - footTilt)
    
    # for pos in range(endPos, startPos):
    #   left2servo.angle = (pos)
    #   right2servo.angle = (endPos + (startPos - pos));            
    #   time.sleep(15/1000);  
                         
  
moon_walk(True)
    

