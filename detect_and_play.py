#!/usr/bin/env python

import os
import sys
import time
import board
import busio
import adafruit_mpr121
from pygame import mixer
from lib.functions import load_json


def speech(pin):
    # Start pygame mixer
    mixer.init()

    # Users pygame mixer to load an mp3 file and play it
    filename = f'../voice_files/{pin}.mp3'
    not_found_filename = '../voice_files/not_found.mp3'

    # Check if file exists
    exists = os.path.isfile(filename)

    if exists:
        mixer.music.load(filename)
    else:
        mixer.music.load(not_found_filename)

    mixer.music.play()


def detectPin():
    print("========= WAITING FOR KEYS =========")
    i2c = busio.I2C(board.SCL, board.SDA)
    mpr121 = adafruit_mpr121.MPR121(i2c)

    while True:
        # Loop through all 12 inputs (0-11).
        for i in range(12):
            # Call is_touched and pass it then number of the input.  If it's touched
            # it will return True, otherwise it will return False.
            if mpr121[i].value:
                print(f'Input detected PIN {i} touched!')
                speech(i)
        time.sleep(0.25)  # Small delay to keep from spamming output messages.


if __name__ == '__main__':
    # Start detecting pins
    detectPin()
