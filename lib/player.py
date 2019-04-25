import os
import sys
from pygame import mixer


def play(pin):
    # Start pygame mixer if it's not running
    if not mixer.get_init():
        mixer.init()
    else:

    if not mixer.music.get_busy() == True:
        # Users pygame mixer to load an mp3 file and play it
        filename = f'./voice_files/{pin}.mp3'

        # Check if file exists
        exists = os.path.isfile(filename)

        if exists:
            mixer.music.load(filename)
        else:
            # We load the not found file if the file doesn't exist
            mixer.music.load('./voice_files/not_found.mp3')

        # Play the audio file
        mixer.music.play()


if __name__ == '__main__':
    play(sys.argv[1])
