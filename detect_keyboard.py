import sys
import json
from curtsies import Input
from lib.player import play


def load_json():
    with open("static/text_by_key.json", "r") as read_file:
        return json.load(read_file)


def keyAction(key, json):
    key = key.replace("'", '')
    print(key, ": ")
    if key == " ":
        key = "SPACE"

    if key in json:
        print(json[key], "\n")
        play(key)
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


if __name__ == '__main__':
    json = load_json()
    detectKey(json)
