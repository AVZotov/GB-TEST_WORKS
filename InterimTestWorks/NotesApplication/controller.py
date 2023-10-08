import note
import consoleIO
import fileIO


def run():
    notes = fileIO.load()
    print(notes)
    notes.append(note.add_note())
    fileIO.save(notes)


run()
