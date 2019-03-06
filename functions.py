import json


def load_json(file_path):
    # Reads the JSON file and returns a JSON object
    with open(file_path, "r") as read_file:
        return json.load(read_file)
