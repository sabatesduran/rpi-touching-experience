# Touching experience with a Raspberry Pi

## TODO

- [ ] Add loader in website when updating audio files
- [ ] Add alert when not connected to the internet
- [ ] Fix MPR121 connection

### Hardware

- Raspberry Pi (2, 3, Zero or Zero W)
- MPR121 Capacitive Touch Sensor
- USB Sound Card
- Speaker with AUX 3.5
- AUX 3.5 to AUX 3.5 cable

We were triyng to create little React app that uses Chrome's [Speech Synthesis API](https://developers.google.com/web/updates/2014/01/Web-apps-that-talk-Introduction-to-the-Speech-Synthesis-API) to speak after a keypress event generated by a MakeyMakey but we have two problems with this:

- Doesn't work without Internet.
- The API doesn't work with Chromium (default browser for Raspbian, Raspberry Pi OS).

### Our solution

We use the Google Cloud [Text-to-Speech API](https://cloud.google.com/text-to-speech/) to generate `.mp3` for each key event so we can use it offline.

## Install

In this example I'm using a Raspberry Pi Zero W V1.1 with Raspbian Stretch Lite.

- Install packages

```sh
sudo apt install git mgp123 build-essential checkinstall python-pip python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavfor  mat-dev libavcodec-dev libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libudev-dev python-smbus i2c-tools
```

or (havent't try this one yet)

```sh
sudo apt-get install python-pygame
```

- Enable i2c (Nedeed to work with MPR121)

  1. `$ sudo raspi-config`
  2. Interfacing Options
  3. I2C
  4. Select `Yes`

- Install Python 3.6 with the following [gist](https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f).

  - If you can't install pip3.6 packages check this StackOverflow [answer](https://stackoverflow.com/a/44291036/3437023).

* Create credentials for the Google Text-to-Speech API [here](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries) (You will need to add a billing account).

* Add variable to `.bashrc`

```sh
echo "export GOOGLE_APPLICATION_CREDENTIALS=\"/home/pi/rpi-touching-experience/credentials.json\"" >> ~/.bashrc && souce ~/.bashrc
```

- Install dependencies (grab popcorn and open Netflix this is going to take a while)

```sh
pip3.6 install -r requirements.txt --user
```

- Generate audio (check that you have Internet if you see that it's hanging in there)

```sh
python3 synthesize_text.py
```

- Install the USB audio card following this [tutorial](https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi/updating-alsa-config).

- Execute program

```
python3 run.py
```
