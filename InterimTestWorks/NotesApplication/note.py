from datetime import datetime
import consoleIO
import uuid


def get_note() -> dict:
    note_title = consoleIO.get_user_string('Please enter note title: ')
    note_body = consoleIO.get_user_string('Please enter note body: ')
    note_id = str(uuid.uuid1())[0:4]
    note_date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    keys = ['id', 'title', 'body', 'date']
    values = [note_id, note_title, note_body, note_date]
    return dict(zip(keys, values))


def edit_note(note: dict):
    note['title'] = consoleIO.get_user_string('Please enter note title: ')
    note['body'] = consoleIO.get_user_string('Please enter note body: ')
    note['date'] = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))


