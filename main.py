# --------------------
# CL Interface for command parsing and handling
# --------------------

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.completion.base import CompleteEvent

from constants import COMMANDS
from storage import load_data, save_data
from handlers import (
    parse_input,
    add_contact,
    change_number,
    show_phone,
    show_all_contacts,
    get_help, add_birthday,
    show_birthday,
    birthdays
)


# Autocomplete class
class CommandCompleter(Completer):
    def __init__(self, commands: dict):
        self.commands = commands

    def get_completions(self, document: Document, complete_event: CompleteEvent):
        text = document.text_before_cursor

        if " " in text:
            return

        word = document.get_word_before_cursor()

        for cmd in self.commands:
            if cmd.startswith(word):
                yield Completion(cmd, start_position=-len(word))


# Operate the whole program, store all contacts, ask for an input,
# match commands to execute them
def main():
    session = PromptSession(
        completer=CommandCompleter(COMMANDS),
        complete_while_typing=True
    )

    book = load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = session.prompt("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:

            case "close" | "exit":
                save_data(book)
                print("Goodbye!")
                break

            case "hello":
                print("How can I help you?")

            case "add":
                print(add_contact(args, book))

            case "change":
                print(change_number(args, book))

            case "phone":
                print(show_phone(args, book))

            case "all":
                print(show_all_contacts(book))

            case "add-birthday":
                print(add_birthday(args, book))

            case "show-birthday":
                print(show_birthday(args, book))

            case "birthdays":
                print(birthdays(args, book))

            case "help":
                print(get_help())

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
