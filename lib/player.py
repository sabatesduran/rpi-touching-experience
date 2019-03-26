import os
import sys
from pygame import mixer


def play(pin):
    # Start pygame mixer
    mixer.init()

    # Users pygame mixer to load an mp3 file and play it
    filename = f'./voice_files/{pin}.mp3'
    not_found_filename = './voice_files/not_found.mp3'

    # Check if file exists
    exists = os.path.isfile(filename)

    if exists:
        mixer.music.load(filename)
    else:
        mixer.music.load(not_found_filename)

    mixer.music.play()

    # Checks if it's busy playing the sound
    while mixer.music.get_busy() == True:
        continue

    # Close mixer
    mixer.quit()


if __name__ == '__main__':
    play(sys.argv[1])
