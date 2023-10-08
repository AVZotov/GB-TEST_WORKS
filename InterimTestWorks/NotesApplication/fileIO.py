import json
import os.path
from typing import Any

filename = 'notes.json'
primary_key = 'notes'


def load() -> list[Any]:
    if os.path.isfile(filename):
        print('notes loaded!')
        with open(filename, 'r') as file:
            data = json.load(file)
        return data[primary_key]

    print('notes file not found, created new data file')
    notes = {primary_key: list()}
    with open(filename, 'w') as file:
        json.dump(notes, file, indent=4)
    return list()


def save(notes: list):
    data = {primary_key: notes}
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print('notes file updated')
