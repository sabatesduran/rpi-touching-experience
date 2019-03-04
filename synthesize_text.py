#!/usr/bin/env python3.6

import json
from google.cloud import texttospeech


def load_json():
    with open("text_by_key.json", "r") as read_file:
        return json.load(read_file)


# This functions is from a Google API example
# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/texttospeech/cloud-client/synthesize_text.py
def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=item["text"])

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    file_name = f'./voice_files/{item["key"]}.mp3'
    with open(file_name, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to file {file_name}\n')


if __name__ == '__main__':
    json = load_json()
    print("========= GENERATING MP3 FILES =========")
    for item in json["data"]:
        print(f'{item["key"]}: {item["text"]}')
        synthesize_text(item)
    print("========= FINISHED =========")
