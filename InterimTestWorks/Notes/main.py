import uuid
import json
import os.path


def print_main_menu():
    print("Welcome to notes application!\n1\tShow All Notes\n2\tSelect Notes By Date\n3\tExit")


def print_selection_menu():
    print("1\tAdd note\n2\tDelete note\n3\tSave changes\n4\tReturn to main menu\n")


def get_user_input() -> str:
    pass


def convert_to_json(notebook: dict):
    pass


def save_to_file():
    path = 'notes.json'
    with open(path, 'a') as file:
        # append new record to the existing route
        pass


def load_from_file():
    path = 'notes.json'
    is_exist = os.path.isfile(path)
    if is_exist:
        with open(path, 'r') as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                print('Your notebook is empty. Lets start to work')
                return dict()
    open(path, 'w').close()
    return dict()


def add_note():
    pass


def delete_node():
    pass


def get_note():
    pass


def switch(user_input) -> bool:
    pass


def run():
    notes = dict()
    flag = True
    notes = load_from_file()

    while flag:
        print_main_menu()
        user_input = get_user_input()
        flag = switch(user_input)


run()
