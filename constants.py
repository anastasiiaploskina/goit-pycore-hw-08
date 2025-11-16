# --------------------
# Constants for boxes, date and commands management
# --------------------

# Boxes constants
TOTAL_WIDTH = 120
COMMAND_COLUMN_WIDTH = 25
FORMAT_COLUMN_WIDTH = 30


DATE_FORMAT = "%d.%m.%Y"


# Stores all the commands available in the bot (used in get_help() function)
COMMAND_REGISTRY = [
    {
        "command": "hello",
        "format": "hello",
        "description": "Ask 'How can I help you?'"
    },
    {
        "command": "add <NAME> <PHONE>",
        "format": "add Anna +380633727223",
        "description": "Add new contact to your contacts list."
    },
    {
        "command": "change <NAME> <PHONE>",
        "format": "change Daniil +380637927223",
        "description": "Change a specified contact's phone number."
    },
    {
        "command": "phone <NAME>",
        "format": "phone John",
        "description": "Return a specified contact's phone number."
    },
    {
        "command": "all",
        "format": "all",
        "description": "Return all contacts as a box."
    },
    {
        "command": "help",
        "format": "help",
        "description": "Return help for commands as a box."
    }
]

COMMANDS = {entry["command"].split()[0]: entry for entry in COMMAND_REGISTRY}
