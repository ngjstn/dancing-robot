"""
Main python code that is ran during the operation of the robot.
Defines the dance moves, servo and display ports and selects between the dances and
Contributors: Sam, Julian, Justin, Tayyib
"""
import board
from adafruit_st7735r import ST7735R
from adafruit_display_text import label
import adafruit_imageload
import displayio
import pwmio
import time
import digitalio
from adafruit_motor import servo



# Release any resources currently in use for the displays
displayio.release_displays()

# Define the ports for the TFT display
spi = board.SPI()
tft_cs = board.D5
tft_dc = board.D7


# Define the input signals for the TFT display.
display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D9
)

# Define the display object with the input signals, dimensions, rotation, and color.
display = ST7735R(display_bus, width=128, height=128, rotation=0, bgr=True)

imgFile = ["/Crab_Rave.bmp", "/taytay.bmp", "/rick_roll.bmp", "/matt.bmp", "/shrek.bmp", "/initialD.bmp"]
images = []

# Creates connection objects to connect the ItsyBitsy to the nano and arduino boards.
com0 = digitalio.DigitalInOut(board.A2)
com1 = digitalio.DigitalInOut(board.A3)
com2 = digitalio.DigitalInOut(board.A4)

# Defines the connection objects on the ItsyBitsy as input.
com0.direction = digitalio.Direction.INPUT
com1.direction = digitalio.Direction.INPUT
com2.direction = digitalio.Direction.INPUT

# Adds a pull up resistor to the input connections.
com0.pull = digitalio.Pull.UP
com1.pull = digitalio.Pull.UP
com2.pull = digitalio.Pull.UP

# Defines input PWM objects for the servo.
pwm_one = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
pwm_four = pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)
pwm_three = pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
pwm_two = pwmio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)

# Creates servo objects using the PWM inputs.
my_servo_one = servo.Servo(pwm_one) # right thigh
my_servo_two = servo.Servo(pwm_two) # right heel
my_servo_three = servo.Servo(pwm_three) # left heel
my_servo_four = servo.Servo(pwm_four) # left thigh

# Sets the default songs.
song = 0
current_image = 1

"""
dance_zero will move the servos to dance until it the song is changes or it completes it sequence of moves
pre-condition: all servo objects are no NULL and connected to the the correct positions
@param my_servo_one: a servo object connected to the right thigh
@param my_servo_two: a servo object connected to the  right heel
@param my_servo_three: a servo object connected to the left heel
@param my_servo_four: a servo object connected to theleft thigh
"""
def dance_zero(my_servo_one, my_servo_two, my_servo_three, my_servo_four):
    my_servo_one.angle = 90
    my_servo_four.angle - 90
    my_servo_two.angle = 90
    my_servo_three.angle = 90
    song = getSong()
    if song != 0 and song != 6:
        return

    my_servo_two.angle = 160
    my_servo_three.angle = 20
    song = getSong()
    if song != 0 and song != 6:
        return
    time.sleep(0.5)
    my_servo_two.angle = 90
    my_servo_three.angle = 90
    song = getSong()
    if song != 0:
        return
    time.sleep(0.5)

    time.sleep(0.5)
    my_servo_one.angle = 170
    my_servo_four.angle = 100
    my_servo_two.angle = 160
    my_servo_three.angle = 100
    song = getSong()
    if song !=0 and song != 6:
        return
    time.sleep(1)
    my_servo_one.angle = 90
    my_servo_four.angle - 90
    my_servo_two.angle = 90
    my_servo_three.angle = 90
    song = getSong()
    if song != 0 and song != 6:
        return
    time.sleep(0.5)
    my_servo_one.angle = 100
    my_servo_four.angle = 30
    my_servo_three.angle = 40
    my_servo_two.angle = 90
    song = getSong()
    if song != 0 and song != 6:
        return
    time.sleep(0.5)
    my_servo_one.angle = 90
    my_servo_four.angle - 90
    my_servo_two.angle = 90
    my_servo_three.angle = 90
    song = getSong()
    if song != 0 and song != 6:
        return
    time.sleep(0.5)

"""
dance_one will move the servos to dance until it the song is changes or it completes it sequence of moves
pre-condition: all servo objects are no NULL and connected to the the correct positions
@param my_servo_one: a servo object connected to the right thigh
@param my_servo_two: a servo object connected to the  right heel
@param my_servo_three: a servo object connected to the left heel
@param my_servo_four: a servo object connected to theleft thigh
"""
def dance_one(my_servo_one, my_servo_two, my_servo_three, my_servo_four):
    startPos = 40
    pos = startPos
    endPos = 120
    flatPos = 90
    left1Offset = 10
    left2Offset = 0
    right1Offset = 5
    right2Offset = 0
    footTilt = 8
    if song != 1 and song != 6:
        return
    #my_servo_two.angle = (flatPos + left2Offset - footTilt)
    my_servo_four.angle = (flatPos + right2Offset + footTilt)
    #my_servo_one.angle = (flatPos + left1Offset)
    my_servo_three.angle = (flatPos + right1Offset)
    for pos in range(startPos, endPos):
      if getSong() != 1 and getSong() != 6:
        return
      #my_servo_one.angle = (pos)
      my_servo_four.angle = (endPos + (startPos - pos))
      time.sleep(15/1000)

    #my_servo_one.angle = (flatPos + left1Offset + footTilt)
    my_servo_three.angle = (flatPos + right1Offset - footTilt)

    for pos in range(endPos, startPos):
      if getSong() != 1 and getSong() != 6:
        return
      #my_servo_two.angle = (pos)
      my_servo_four.angle = (endPos + (startPos - pos))
      time.sleep(15/1000)

    for pos in range(startPos, endPos):
      if getSong() != 1 and getSong() != 6:
        return
      my_servo_one.angle = (pos)
      #my_servo_four.angle = (endPos + (startPos - pos))
      time.sleep(15/1000)

    my_servo_two.angle = (flatPos + left1Offset + footTilt)
    #my_servo_three.angle = (flatPos + right1Offset - footTilt)

    for pos in range(endPos, startPos):
      if getSong() != 1 and getSong() != 6:
        return
      my_servo_two.angle = (pos)
     #my_servo_four.angle = (endPos + (startPos - pos));
      time.sleep(15/1000)
    return

"""
dance_two will move the servos to dance until it the song is changes or it completes it sequence of moves
pre-condition: all servo objects are no NULL and connected to the the correct positions
@param my_servo_one: a servo object connected to the right thigh
@param my_servo_two: a servo object connected to the  right heel
@param my_servo_three: a servo object connected to the left heel
@param my_servo_four: a servo object connected to theleft thigh
"""
def dance_two(my_servo_one, my_servo_two, my_servo_three, my_servo_four):
    my_servo_one.angle = 90
    my_servo_two.angle = 90
    my_servo_three.angle = 90
    my_servo_four.angle = 90
    time.sleep(1)
    my_servo_two.angle = 140
    my_servo_three.angle = 140
    time.sleep(1)
    my_servo_two.angle = 40
    my_servo_three.angle = 40
    time.sleep(1)

"""
dance_three will move the servos to dance until it the song is changes or it completes it sequence of moves
pre-condition: all servo objects are no NULL and connected to the the correct positions
@param my_servo_one: a servo object connected to the right thigh
@param my_servo_two: a servo object connected to the  right heel
@param my_servo_three: a servo object connected to the left heel
@param my_servo_four: a servo object connected to theleft thigh
"""
def dance_three(my_servo_one, my_servo_two, my_servo_three, my_servo_four):
    my_servo_one.angle = 90
    my_servo_four.angle - 90
    my_servo_two.angle = 90
    my_servo_three.angle = 90
    song = getSong()
    if song != 3 and song != 6:
        return

    my_servo_two.angle = 160
    my_servo_three.angle = 20
    song = getSong()
    if song != 3 and song != 6:
        return
    time.sleep(0.5)
    my_servo_two.angle = 90
    my_servo_three.angle = 90
    song = getSong()
    if song != 3 and song != 6:
        return
    time.sleep(0.5)

    time.sleep(0.5)
    my_servo_two.angle = 160
    my_servo_three.angle = 20
    song = getSong()
    if song != 3 and song != 6:
        return
    time.sleep(1)
    my_servo_one.angle = 90
    my_servo_four.angle - 90
    my_servo_two.angle = 90
    my_servo_three.angle = 90
    song = getSong()
    if song != 3 and song != 6:
        return
    time.sleep(0.5)

"""
dance_four will move the servos to dance until it the song is changes or it completes it sequence of moves
pre-condition: all servo objects are no NULL and connected to the the correct positions
@param my_servo_one: a servo object connected to the right thigh
@param my_servo_two: a servo object connected to the  right heel
@param my_servo_three: a servo object connected to the left heel
@param my_servo_four: a servo object connected to theleft thigh
"""
def dance_four(my_servo_one, my_servo_two, my_servo_three, my_servo_four):
    time.sleep(1)
    my_servo_one.angle = 178
    my_servo_four.angle = 90
    time.sleep(1)
    my_servo_one.angle = 90
    my_servo_four.angle = 2
    time.sleep(1)
    if getSong() != 4 and getSong() != 6:
        return

"""
dance_five will move the servos to dance until it the song is changes or it completes it sequence of moves
pre-condition: all servo objects are no NULL and connected to the the correct positions
@param my_servo_one: a servo object connected to the right thigh
@param my_servo_two: a servo object connected to the  right heel
@param my_servo_three: a servo object connected to the left heel
@param my_servo_four: a servo object connected to theleft thigh
"""
def dance_five(my_servo_one, my_servo_two, my_servo_three, my_servo_four):
    startPos = 40
    pos = startPos
    endPos = 120
    flatPos = 90
    left1Offset = 10
    left2Offset = 0
    right1Offset = 5
    right2Offset = 0
    footTilt = 8
    my_servo_two.angle = (flatPos + left2Offset - footTilt)
    my_servo_four.angle = (flatPos + right2Offset + footTilt)
    my_servo_one.angle = (flatPos + left1Offset)
    my_servo_three.angle = (flatPos + right1Offset)
    for pos in range(startPos, endPos):
      my_servo_one.angle = (pos)
      my_servo_four.angle = (endPos + (startPos - pos))
      time.sleep(15/1000)

    my_servo_two.angle = (flatPos + left1Offset + footTilt)
    my_servo_three.angle = (flatPos + right1Offset - footTilt)

    for pos in range(endPos, startPos):
      my_servo_one.angle = (pos)
      my_servo_four.angle = (endPos + (startPos - pos))
      time.sleep(15/1000)
    return


"""
getSong will return the current song that shoule be played
return: the current song [0,6]
"""
def getSong():
    if not com0.value and not com1.value and not com2.value:
        song = 0
    elif com0.value and not com1.value and not com2.value:
        song = 1
    elif not com0.value and not com1.value and com2.value:
        song = 4
    elif com0.value and not com1.value and com2.value:
        song = 5
    elif not com0.value and com1.value and not com2.value:
        song = 2
    elif com0.value and com1.value and not com2.value:
        song = 3
    else:
        song = 6
    print(str(com2.value) + " " + str(com1.value) + " " + str(com0.value) + " " + str(song))
    return song

# Main loop will go through each tone in order up and down.
while True:

    song = getSong()
    # print(str(com2.value) + " " + str(com1.value) + " " + str(com0.value) + " " + str(song))
    if song <= 5 and current_image != song:
        bitmap, palette = adafruit_imageload.load(imgFile[song],
                                            bitmap=displayio.Bitmap,
                                            palette=displayio.Palette)

        # Create a TileGrid to hold the bitmap
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

        # Create a Group to hold the TileGrid
        group = displayio.Group()

        # Add the TileGrid to the Group
        group.append(tile_grid)
        display.show(group)
        current_image = song

    if song == 0:
        my_servo_one.angle = 90
        my_servo_two.angle = 90
        my_servo_three.angle = 90
        my_servo_four.angle = 90
        dance_zero(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
    if song == 1:
        my_servo_one.angle = 90
        my_servo_two.angle = 90
        my_servo_three.angle = 90
        my_servo_four.angle = 90
        dance_one(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
    if song == 2:
        my_servo_one.angle = 90
        my_servo_two.angle = 90
        my_servo_three.angle = 90
        my_servo_four.angle = 90
        dance_two(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
    if song == 3:
        my_servo_one.angle = 90
        my_servo_two.angle = 90
        my_servo_three.angle = 90
        my_servo_four.angle = 90
        dance_three(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
    if song == 4:
        my_servo_one.angle = 90
        my_servo_two.angle = 90
        my_servo_three.angle = 90
        my_servo_four.angle = 90
        dance_four(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
    if song == 5:
        my_servo_one.angle = 90
        my_servo_two.angle = 90
        my_servo_three.angle = 90
        my_servo_four.angle = 90
        dance_five(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
    if song == 6:
        my_servo_one.angle = 90
        my_servo_two.angle = 90
        my_servo_three.angle = 90
        my_servo_four.angle = 90
        dance_zero(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
        dance_one(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
        dance_two(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
        dance_three(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
        dance_four(my_servo_one, my_servo_two, my_servo_three, my_servo_four)
        dance_five(my_servo_one, my_servo_two, my_servo_three, my_servo_four)




