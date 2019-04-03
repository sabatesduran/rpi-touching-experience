#!/usr/bin/env python

import sys
import time
import board
import busio
import adafruit_mpr121
from lib.functions import load_json
from lib.player import play


def run():
    print("============================================")
    print("========= HRBS TOUCHING EXPERIENCE =========")
    print("============================================")
    print("\nWAITING FOR TOUCH EVENTS...\n")

    # Count amount of touch events happening
    touch_count = 0

    # Set sensor sensitivity
    adafruit_mpr121.MPR121_TOUCHTH_0 = 50
    adafruit_mpr121.MPR121_RELEASETH_0 = 51

    # Start sensor
    i2c = busio.I2C(board.SCL, board.SDA)
    mpr121 = adafruit_mpr121.MPR121(i2c)

    while True:
        # Loop through all 12 inputs (0-11).
        for i in range(12):
            # Call is_touched and pass it then number of the input. If it's touched
            # it will return True, otherwise it will return False.
            if mpr121[i].value:
                touch_count += 1
                print(f'{touch_count}: PIN {i} touched!')
                play(i)
        time.sleep(0.25)  # Small delay to keep from spamming output messages.


if __name__ == '__main__':
    run()
