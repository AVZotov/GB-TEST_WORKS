import note
import consoleIO
import fileIO


def run():
    notes = fileIO.load()
    print(notes)


run()
