#!/usr/bin/env python

import sys
import json
from curtsies import Input
from pygame import mixer


def load_json():
    with open("text_by_key.json", "r") as read_file:
        return json.load(read_file)


def speech(key):
    mixer.init()
    mixer.music.load(f'./voice_files/{key}.mp3')
    mixer.music.play()


def keyAction(key, json):
    key = key.replace("'", '')

    if key == " ":
        key = "SPACE"

    # Current key
    print(key, ":")

    if key in json:
        print(json[key], "\n")
        speech(key)
    elif key == "q":
        print("See ya!")
        sys.exit()
    else:
        print("I don't know this mapping\n")


def detectKey(json):
    print("========= WAITING FOR KEYS =========")
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            keyAction(repr(e), json)

# def keySpeech


if __name__ == '__main__':
    json = load_json()
    detectKey(json)
