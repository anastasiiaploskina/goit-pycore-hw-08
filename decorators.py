# --------------------
# Decorator to manage input error
# --------------------

from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError:
            return "Missing arguments. Please provide both name and phone number."

        except KeyError:
            return "Contact not found. Please check the name and try again."

        except IndexError:
            return "Insufficient arguments. Please provide the required information."

    return inner
