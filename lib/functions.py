import os
import json


def load_json(file_path):
    # Reads the JSON file and returns a JSON object
    with open(file_path, "r") as read_file:
        return json.load(read_file)


def rewrite_json(file_path, new_json):
    with open(file_path, "w") as file:
        file.write(json.dumps(new_json, indent=4, sort_keys=True))
        file.close()


def delete_mp3_from_folder(folder):
    # Gets all the files from a directory as an array
    for filename in os.listdir(folder):
        # If the file ends with .mp3 we detete it
        if filename.endswith('.mp3'):
            os.unlink(f'./voice_files/{filename}')
            print(f'\t Deleting {filename}')
