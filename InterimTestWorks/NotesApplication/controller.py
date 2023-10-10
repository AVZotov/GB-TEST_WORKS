import note as n
import consoleIO
import fileIO


def run():
    notes = fileIO.load()
    flag = True
    print('\nWelcome to your notes!\n')

    while flag:
        consoleIO.main_menu()
        user_input = consoleIO.get_user_string('enter menu point to proceed: ')
        flag = navigate_main_menu(user_input, notes)


def navigate_main_menu(user_input: str, notes: list) -> bool:
    if user_input == '1':
        consoleIO.print_all(notes)
        return True
    if user_input == '2':
        consoleIO.print_selected_by_date(notes)
        return True
    if user_input == '3':
        consoleIO.print_by_id(notes)
        return True
    if user_input == '4':
        notes.append(n.add_note())
        return True
    if user_input == '5':
        selected_note = get_note_by_id(notes)
        if not len(selected_note) == 0:
            n.edit_note(selected_note)
        return True
    if user_input == '6':
        delete_note(notes)
        return True
    if user_input == '7':
        print('Saving your changes to file...')
        fileIO.save(notes)
        print('File saved. Exiting notes application')
        return False


def get_note_by_id(notes: list) -> dict:
    note_id = consoleIO.get_user_string('Enter note ID: ')
    for single_note in notes:
        if single_note['id'] == note_id:
            return single_note
    print(f'note with ID: {note_id} not found')
    return dict()


def delete_note(notes: list):
    selected_note = get_note_by_id(notes)

    if not len(selected_note) == 0:
        notes.remove(selected_note)
