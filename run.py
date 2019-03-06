#!/usr/bin/env python

import sys
from curtsies import Input
from pygame import mixer
from functions import load_json


def speech(key):
    # Users pygame mixer to load an mp3 file and play it
    mixer.init()
    mixer.music.load(f'./voice_files/{key}.mp3')
    mixer.music.play()


def keyAction(key, json):
    # The detect key function return the caracter
    # with single quotes here we are removing them
    key = key.replace("'", '')

    # In case that detects an space we chnage the key to SPACE
    if key == " ":
        key = "SPACE"

    # Print pressed key
    print(key, ":")

    # In case the key exists in the object we play the audio file
    if key in json:
        print(json[key], "\n")
        speech(key)
    elif key == "q":
        # Quit the program if the key is a "q"
        print("Exiting program...See ya!")
        sys.exit()
    else:
        # Print an error if we don't know what to do with the key.
        print("I don't know this mapping\n")


def detectKey(json):
    print("========= WAITING FOR KEYS =========")
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            keyAction(repr(e), json)


if __name__ == '__main__':
    # Get JSON object
    json = load_json("text_by_key.json")
    # Start detecting keys
    detectKey(json)
