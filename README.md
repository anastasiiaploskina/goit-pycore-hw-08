
# **Personal Assistant — Command-Line Address Book**

This project is a modular, object-oriented **personal assistant CLI application**.
It manages contacts, phone numbers, birthdays, upcoming events, and provides autocompletion for all commands.
Data is automatically saved between sessions.

The application uses a structured architecture across several modules, including models, handlers, constants, decorators, persistent storage, and a CLI interface powered by **prompt-toolkit**.

---

# **Table of Contents**

* [Features](#features)
* [Project Structure](#project-structure)
* [Modules Overview](#modules-overview)

  * [classes.py](#classespy)
  * [constants.py](#constantspy)
  * [decorators.py](#decoratorspy)
  * [handlers.py](#handlerspy)
  * [storage.py](#storagepy)
  * [main.py](#mainpy)
* [Command Reference](#command-reference)
* [Birthday System](#birthday-system)
* [Autocomplete Support](#autocomplete-support)
* [Data Persistence](#data-persistence)
* [Installation](#installation)
* [Usage](#usage)
* [Requirements](#requirements)

---

# **Features**

### ✔ Contact management

Add, edit, delete, and show contacts.

### ✔ Multiple phone numbers per contact

Each contact can store multiple phone numbers.

### ✔ Birthday tracking

Store birthdays and list upcoming birthdays for any number of days.

### ✔ Input validation

Phone numbers must be **10 digits**.
Birthday format must be **DD.MM.YYYY**.

### ✔ Autocomplete

Thanks to **prompt-toolkit**, all commands support intelligent autocompletion.

### ✔ Pretty console output

Contact list and help information are displayed in clean, formatted boxes.

### ✔ Persistent storage

Contacts are saved automatically using Python’s `pickle` module.

### ✔ Clean modular architecture

Logic is separated into specialized modules for clarity and maintainability.

---

# **Project Structure**

```
project/
│
├── classes.py          # Core object models (Field, Record, AddressBook)
├── constants.py        # UI constants, command registry, date format
├── decorators.py       # Input error handling decorator
├── handlers.py         # Logic for each user command
├── storage.py          # Save/load data from file
├── main.py             # Interactive CLI application
│
├── .gitignore
├── pyproject.toml
└── addressbook.pkl     # Created dynamically after first run
```

---

# **Modules Overview**

## **classes.py**


Contains core classes:

### **Field**

Base class for all stored values.

### **Name / Phone / Birthday**

* `Phone` validates numbers using `^\d{10}$`
* `Birthday` parses dates using `DATE_FORMAT` (`DD.MM.YYYY`)

### **Record**

Represents a single contact:

* Stores name
* List of phone numbers
* Optional birthday
* Has methods:

  * `add_phone()`
  * `remove_phone()`
  * `edit_phone()`
  * `find_phone()`
  * `add_birthday()`

### **AddressBook**

Subclass of `UserDict` providing:

* Add, find, delete records
* `get_upcoming_birthdays()`

  * Handles leap years
  * Adjusts celebrations from weekends to Monday

---

## **constants.py**


Defines:

* Output formatting widths
* `DATE_FORMAT = "%d.%m.%Y"`
* `COMMAND_REGISTRY` (used in dynamic help box)
* Dictionary of valid commands: `COMMANDS`

---

## **decorators.py**


Defines `@input_error`, a wrapper for handling:

* `ValueError`
* `KeyError`
* `IndexError`

Used to prevent app crashes and provide helpful user messages.

---

## **handlers.py**


Contains implementations for individual assistant commands:

* `parse_input`
* `add_contact`
* `change_number`
* `show_phone`
* `show_all_contacts`
* `add_birthday`
* `show_birthday`
* `birthdays` (upcoming)
* `get_help` (formatted help box)

Outputs are formatted using constants from `constants.py`.

---

## **storage.py**


Uses Python `pickle` to:

* `save_data(book, filename="addressbook.pkl")`
* `load_data(filename="addressbook.pkl")`

If file does not exist, returns a **new AddressBook instance**.

---

## **main.py**


Entry point of the application.

Contains:

* **Command autocompletion** via `prompt_toolkit`
* Persistent loading/saving of address book
* Main input loop using a `match` statement
* Command routing to handlers

---

# **Command Reference**

### Contact Management

| Command                     | Example                             | Description                                |
| --------------------------- | ----------------------------------- | ------------------------------------------ |
| `add <NAME> <PHONE>`        | `add John 1234567890`               | Add a new contact or add phone to existing |
| `change <NAME> <OLD> <NEW>` | `change John 1234567890 0987654321` | Replace a phone number                     |
| `phone <NAME>`              | `phone John`                        | Show contact information                   |
| `all`                       | `all`                               | Display all contacts                       |

### Birthdays

| Command                      | Example                        | Description             |
| ---------------------------- | ------------------------------ | ----------------------- |
| `add-birthday <NAME> <DATE>` | `add-birthday John 24.02.1990` | Add a birthday          |
| `show-birthday <NAME>`       | `show-birthday John`           | Show stored birthday    |
| `birthdays <DAYS>`           | `birthdays 7`                  | Show upcoming birthdays |

### Other

| Command          | Description                          |
| ---------------- | ------------------------------------ |
| `hello`          | Greeting                             |
| `help`           | Show all commands in a formatted box |
| `exit` / `close` | Exit and save data                   |

---

# **Birthday System**

Birthdays are stored as real `datetime` objects.

The assistant:

* Considers whether the birthday has already happened this year
* Adjusts weekend birthdays:

  * Sunday → Monday
  * Saturday → Monday
* Handles invalid dates such as Feb 29 on non-leap years
* Lists all celebrants within **N days**

---

# **Autocomplete Support**

Thanks to `prompt_toolkit`, the assistant offers:

* Autocompletion while typing
* Matching only valid commands
* Case-insensitive prefix matching

Autocomplete implementation:

---

# **Data Persistence**

The assistant automatically keeps your contacts between sessions:

* Contacts saved in `addressbook.pkl`
* Loaded on every start
* Saved on exit

Storage handled via pickle:

---

# **Installation**

1. Install Python **3.12 or newer**
   (per `pyproject.toml` — )

2. Install dependencies:

```bash
pip install prompt-toolkit
```

or using Poetry/uv:

```bash
uv sync
```

---

# **Usage**

Run the assistant:

```bash
python main.py
```

You will see:

```
Welcome to the assistant bot!
Enter a command:
```

Start typing — autocompletion will assist you.

---

# **Requirements**

From `pyproject.toml` ():

* Python ≥ 3.12
* prompt-toolkit ≥ 3.0.52

