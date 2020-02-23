from soundplayer import SoundPlayer
from dosound import DoSound
import RPi.GPIO as GPIO
import time
# Button pins, adapt to your configuration
P_TON1 = 10
P_TON2 = 11
P_TON3 = 12
P_TON4 = 13
P_TON5 = 15
P_TON6 = 16
dev = 1  # USB Soundadapter
button1_pressed = False
button2_pressed = False
button3_pressed = False
button4_pressed = False
button5_pressed = False
button6_pressed = False


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_TON1, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_TON2, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_TON3, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_TON4, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_TON5, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(P_TON6, GPIO.IN, GPIO.PUD_UP)
    DoSound.playTone(440, 0.3, dev)
    DoSound.playTone(550, 0.3, dev)
    DoSound.playTone(660, 0.3, dev)
    time.sleep(1)
    DoSound.playTone([440, 550, 660], 3, dev)


setup()
print "Bereit..."
p = SoundPlayer("/home/pi/maja.mp3", 1)
sound1 = SoundPlayer("/home/pi/maja.mp3", 1)
sound2 = SoundPlayer("/home/pi/maja.mp3", 1)
sound3 = SoundPlayer("/home/pi/maja.mp3", 1)
sound4 = SoundPlayer("/home/pi/maja.mp3", 1)
sound5 = SoundPlayer("/home/pi/maja.mp3", 1)
sound6 = SoundPlayer("/home/pi/maja.mp3", 1)

while True:
    if GPIO.input(P_TON1) == GPIO.LOW:
        if not button1_pressed:
            print "Ton1..."
            sound1.play()
        else:
            sound1.stop()
        button1_pressed = True
    elif GPIO.input(P_TON2) == GPIO.LOW:
        if not button2_pressed:
            print "Ton2..."
            sound2.play()
        else:
            sound2.stop()
        button2_pressed = True
    elif GPIO.input(P_TON3) == GPIO.LOW:
        if not button3_pressed:
            print "Ton3..."
            sound3.play()    
        else:
            sound3.stop()
        button3_pressed = True
    elif GPIO.input(P_TON4) == GPIO.LOW:
        if not button4_pressed:
            print "Ton4..."
            sound4.play()
        else:
            sound4.stop()
        button4_pressed = True
    elif GPIO.input(P_TON5) == GPIO.LOW:
        if not button5_pressed:
            print "Ton5..."
            sound5.play
        else:
            sound5.stop()
        button5_pressed = True
    elif GPIO.input(P_TON6) == GPIO.LOW:
        if not button6_pressed:
            print "Ton6..."
            sound6.play()
        else:
            sound6.stop()
        button6_pressed = True
    time.sleep(0.1)  # Do not waste processor time
