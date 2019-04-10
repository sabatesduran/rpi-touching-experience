import keyboard
import time

def key_press(key):
    print(key.name)

keyboard.on_press(key_press)

print("Started!")
while True:
    time.sleep(0.25)
