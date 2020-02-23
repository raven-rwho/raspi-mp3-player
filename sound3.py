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
while True:
    if GPIO.input(P_TON1) == GPIO.LOW:
        print "Ton1..."
        DoSound.playTone(440, 0.3, dev)
    elif GPIO.input(P_TON2) == GPIO.LOW:
        print "Ton2..."
        DoSound.playTone(550, 0.3, dev)
    elif GPIO.input(P_TON3) == GPIO.LOW:
        print "Ton3..."
        DoSound.playTone(660, 0.3, dev)
    elif GPIO.input(P_TON4) == GPIO.LOW:
        print "Ton4..."
        p.stop()
        DoSound.playTone(770, 0.3, dev)
    elif GPIO.input(P_TON5) == GPIO.LOW:
        print "Ton5..."
        DoSound.playTone(880, 0.3, dev)
        # p = SoundPlayer("/home/pi/maja.mp3", 1)
        p.play()
    elif GPIO.input(P_TON6) == GPIO.LOW:
        print "Ton6..."
        DoSound.playTone(1000, 0.3, dev)
    time.sleep(0.1)  # Do not waste processor time
