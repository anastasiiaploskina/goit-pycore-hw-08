# --------------------
# Handlers to manage user commands
# --------------------

from classes import Record, AddressBook
from decorators import input_error
from constants import (
    TOTAL_WIDTH,
    COMMAND_COLUMN_WIDTH,
    FORMAT_COLUMN_WIDTH,
    COMMAND_REGISTRY
)

# Parse an user input to receive command and other arguments
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Add new contact, add phone number for existing contact
@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


# Change phone number for existing contact
@input_error
def change_number(args, book: AddressBook):
    name, phone, new_phone, *_ = args
    record = book.find(name)
    message = "Contact changed."
    if record is None:
        message = "Contact doesn't exist."
    else:
        record.edit_phone(phone, new_phone)
    return message


# Show phone number of a specified contact
@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    return record


# Show all contacts within a box, if there are no contacts show empty box
@input_error
def show_all_contacts(book: AddressBook):
    users_lines = []

    num_contacts = len(book)
    header_text = f"CONTACTS LIST ({num_contacts} Contacts)".center(
        TOTAL_WIDTH)
    users_lines.append("╔" + "═" * TOTAL_WIDTH + "╗")
    users_lines.append("║" + header_text + "║")
    users_lines.append("╟" + "─" * TOTAL_WIDTH + "╢")

    for name in book:
        record = book.find(name)
        middle_section = "║ " + str(record).ljust(TOTAL_WIDTH - 1) + "║"
        users_lines.append(middle_section)

    users_lines.append("╚" + "═" * TOTAL_WIDTH + "╝")

    return "\n".join(users_lines)


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    message = "Contact's birthday added."

    if record is None:
        message = f"Contact named {name} doesn't exist."

    record.add_birthday(birthday)
    return message


@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    message = f"{name}'s birthday is {record.birthday}"

    if record is None:
        message = f"Contact named {name} doesn't exist."

    if record.birthday is None:
        message = f"Contact named {name} doesn't have birthday added"

    return message


@input_error
def birthdays(args, book: AddressBook):
    days, *_ = args

    if len(args) > 0:
        try:
            days = int(days)

        except ValueError:
            return "Please provide correct amount of days."

    upcoming_birthdays = book.get_upcoming_birthdays(days)

    if not upcoming_birthdays:
        return f"There aren't any celebrants during next {days} days."

    return upcoming_birthdays


# Dynamic help box, assosiated with COMMAND REGISTRY constant
def get_help():
    help_lines = []

    help_lines.append("╔" + "═" * TOTAL_WIDTH + "╗")
    header_text = "ASSISTANT BOT'S HELP".center(TOTAL_WIDTH)
    help_lines.append("║" + header_text + "║")
    help_lines.append("╟" + "─" * TOTAL_WIDTH + "╢")

    utility_line = ("Command".ljust(COMMAND_COLUMN_WIDTH) +
                    "Example".ljust(FORMAT_COLUMN_WIDTH) +
                    "Description")

    help_lines.append("║" + utility_line.ljust(TOTAL_WIDTH) + "║")
    help_lines.append("╟" + "─" * TOTAL_WIDTH + "╢")

    for item in COMMAND_REGISTRY:
        command = item["command"].ljust(COMMAND_COLUMN_WIDTH)
        example = item["format"].ljust(FORMAT_COLUMN_WIDTH)
        description = item["description"]

        line = f"{command}{example}{description}".ljust(TOTAL_WIDTH)
        help_lines.append("║" + line + "║")

    help_lines.append("╚" + "═" * TOTAL_WIDTH + "╝")

    return "\n".join(help_lines)
