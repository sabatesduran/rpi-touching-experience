#!/usr/bin/env python

from google.cloud import texttospeech
from functions import load_json


# This functions is from a Google API example
# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/texttospeech/cloud-client/synthesize_text.py
def synthesize_text(k, v):
    """Synthesizes speech from the input string of text."""
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=v)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binaryso we save it in a file.
    file_name = f'./voice_files/{k}.mp3'
    with open(file_name, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to file {file_name}\n')


if __name__ == '__main__':
    json = load_json("text_by_key.json")
    print("========= GENERATING MP3 FILES =========")
    for k, v in json.items():
        print(f'{k}: {v}')
        synthesize_text(k, v)
    print("========= FINISHED =========")
