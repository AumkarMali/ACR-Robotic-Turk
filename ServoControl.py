from gpiozero import AngularServo
from time import sleep
import json
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
print("Starting...")

#Load instructions for all movements (per square)
with open('controlMovements.json', 'r') as file:
    servo_movements = json.load(file)

#Define all joints of ARM
servo1 = AngularServo(4, initial_angle=212, min_angle=00, max_angle=270, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo2 = AngularServo(15, initial_angle=125, min_angle=0, max_angle=270, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo3 = AngularServo(2, initial_angle=35, min_angle=0, max_angle=270, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo4 = AngularServo(3, initial_angle=12, min_angle=0, max_angle=270, min_pulse_width=0.5/1000, max_pulse_width=2/1000, pin_factory=factory)
sleep(2)

#Controls speed of joints during journey to a square
def goto(servoNum, ang):
    if servoNum == 1:
        if servo1.angle < ang:
            while servo1.angle <= ang:
                servo1.angle += 1
                sleep(0.01)
        else:
            while servo1.angle >= ang:
                servo1.angle -= 1
                sleep(0.01)

    elif servoNum == 2:
        if servo2.angle < ang:
            while servo2.angle <= ang:
                servo2.angle += 1
                sleep(0.015)
        else:
            while servo2.angle >= ang:
                servo2.angle -= 1
                sleep(0.015)

    elif servoNum == 3:
        if servo3.angle < ang:
            while servo3.angle <= ang:
                servo3.angle += 1
                sleep(0.07)
        else:
            while servo3.angle >= ang:
                servo3.angle -= 1
                sleep(0.1)

    sleep(0.2)


def move_arm(best_move):
    sq1 = best_move[0] + best_move[1]
    sq2 = best_move[2] + best_move[3]

    pickUpAngle, placeAngle = servo_movements[sq1], servo_movements[sq2]

    #Move to square 1
    goto(1, pickUpAngle[0])
    goto(2, pickUpAngle[1])
    goto(3, pickUpAngle[2])

    #Grab piece using claw
    servo4.angle = 50
    sleep(0.5)

    #Pick up the ARM
    goto(3, 35)
    goto(2, 125)
    
    #Move to square 2
    goto(1, placeAngle[0])
    goto(2, placeAngle[1])
    goto(3, placeAngle[2])

    #Drop with claw at slow rate
    sleep(0.2)
    while servo4.angle >= 12:
        servo4.angle -= 1
        sleep(0.04)
    
    sleep(0.2)

    #go to initial position
    goto(1, placeAngle[0])
    goto(3, 35)
    goto(2, 125)
    goto(1, 212)
    

#Removes piece from board before continuing with movements
def piece_remove(best_move, player):
    sq1 = best_move[0] + best_move[1]
    sq2 = best_move[2] + best_move[3]

    pickUpAngle, placeAngle = servo_movements[sq1], servo_movements[sq2]

    # move to square 2
    goto(1, placeAngle[0])
    goto(2, placeAngle[1])
    goto(3, placeAngle[2])

    servo4.angle = 50
    sleep(0.5)

    #Pick up the ARM
    goto(3, 35)
    goto(2, 125)

    #Throws piece to different sides of board depending on color
    if player:
        goto(1, 260)
        goto(2, 150)
        goto(3, 15)
    else:
        goto(1, 150)
        goto(2, 150)
        goto(3, 15)
    servo4.angle = 12

    #Goes to initial position
    sleep(0.5)
    goto(3, 35)
    goto(2, 125)
    goto(1, 212)
 
