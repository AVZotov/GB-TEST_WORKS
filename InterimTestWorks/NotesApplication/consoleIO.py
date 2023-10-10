from datetime import datetime


def get_user_string(message: str) -> str:
    return input(message)


def main_menu():
    print('\n1. print all notes\n2. print notes by date\n3. print note by id\n4. add '
          'new note\n5. edit note\n6. delete note\n7. exit\n')


def print_all(notes: list):
    sorted_notes = sorted(notes, key=lambda d: d['date'])
    print('_' * 30)
    for note in sorted_notes:
        print(f'\nID: {note["id"]}\tDate: {note["date"]}\nTitle: {note["title"]}\nNote: {note["body"]}\n')
    print('_' * 30)


def print_selected_by_date(notes: list):
    start_date = get_date_from_user('Enter start date in format dd.mm.yyyy: ')
    end_date = get_date_from_user('Enter end date in format dd.mm.yyyy: ')
    selected_notes = list()

    for note in notes:
        if start_date <= (datetime.strptime(note['date'], '%d.%m.%Y %H:%M:%S')) <= end_date:
            selected_notes.append(note)
    print_all(selected_notes)


def get_date_from_user(message: str) -> datetime:
    while True:
        user_input = get_user_string(message)
        try:
            return datetime.strptime(user_input, '%d.%m.%Y')
        except (TypeError, ValueError) as error:
            print(f'Error! {error}, please try again!')


def print_by_id(notes):
    note_id = get_user_string('Enter note id for search: ')
    selected_notes = list()
    for note in notes:
        if note['id'] == note_id:
            selected_notes.append(note)
    if len(selected_notes) > 0:
        print_all(selected_notes)
    else:
        print(f'There are no notes with ID: {note_id}')