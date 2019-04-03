#!/usr/bin/env python

import sys
import time
import board
import busio
import adafruit_mpr121
from lib.functions import load_json
from lib.player import play


def detectPin():
    print("========= WAITING FOR KEYS =========")
    i2c = busio.I2C(board.SCL, board.SDA)
    adafruit_mpr121.MPR121_TOUCHTH_0 = 10
    adafruit_mpr121.MPR121_RELEASETH_0 = 10
    mpr121 = adafruit_mpr121.MPR121(i2c)

    while True:
        # Loop through all 12 inputs (0-11).
        for i in range(12):
            # Call is_touched and pass it then number of the input.  If it's touched
            # it will return True, otherwise it will return False.
            if mpr121[i].value:
                print(f'Input detected PIN {i} touched!')
                play(i)
        time.sleep(0.25)  # Small delay to keep from spamming output messages.


if __name__ == '__main__':
    # Start detecting pins
    detectPin()
