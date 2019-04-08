#!/usr/bin/env python

import sys
import time
import board
import busio
import adafruit_mpr121
from lib.functions import load_json
from lib.player import play

def calculate_average(pins):
    for i in range(12):
        pins[i] = sum(pins[i]) / len(pins[i])
    return pins
    

def run():
    print("============================================")
    print("========= HRBS TOUCHING EXPERIENCE =========")
    print("============================================")
    
    # GLOBAL VARIABLES
    AVERAGE_TIMES = 40
    
    # Count amount of touch events happening
    touch_count = 0
    average_loop_count = 1

    # Set sensor sensitivity
    #adafruit_mpr121.MPR121_TOUCHTH_0 = 50
    #adafruit_mpr121.MPR121_RELEASETH_0 = 51

    # Start sensor
    i2c = busio.I2C(board.SCL, board.SDA)
    mpr121 = adafruit_mpr121.MPR121(i2c)
    
    average_per_pin = False
    total_per_pin = [[],[],[],[],[],[],[],[],[],[],[],[]]

    while True:
        # Loop through all 12 inputs (0-11).
        for i in range(12):
            if average_loop_count <= AVERAGE_TIMES:
                total_per_pin[i].append(mpr121[i].raw_value)
                if average_loop_count == AVERAGE_TIMES and i == 11 and not average_per_pin:
                    average_per_pin = calculate_average(total_per_pin)
                    print("AVERAGE PER PIN", average_per_pin)
                    print("\nWAITING FOR TOUCH EVENTS...\n")
            
            # Call is_touched and pass it then number of the input. If it's touched
            # it will return True, otherwise it will return False.
            if average_per_pin and mpr121[i].value:
                touch_count += 1
                print(f'{touch_count}: PIN {i} TH {mpr121[i].raw_value}')
                # play(i)
        time.sleep(0.25)  # Small delay to keep from spamming output messages.
        average_loop_count += 1

if __name__ == '__main__':
    run()
