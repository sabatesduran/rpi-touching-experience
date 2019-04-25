import sys
import time
import json
import keyboard
from lib.player import play


def load_json():
    with open("static/text_by_key.json", "r") as read_file:
        return json.load(read_file)


def key_press(key):
    print("Key pressed: ", key.name)
    keyAction(key.name)


def keyAction(key):
    if key in JSON_DOC:
        print(JSON_DOC[key], "\n")
        play(key)
    elif key == "q":
        print("See ya!")
        sys.exit()
    else:
        print("I don't know this mapping\n")


def detectKey():
    keyboard.on_release(key_press)
    print("========= WAITING FOR KEYS =========")
    while True:
        time.sleep(0.8)


if __name__ == '__main__':
    JSON_DOC = load_json()
    detectKey()
