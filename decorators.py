def input_error_add_contact(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please. (phone - 10 symbols)"

    return inner


def input_error_change_contact(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name old phone and new phone please."

    return inner


def input_error_show_phone(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me command and name please."

    return inner


def input_error_add_birthday(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me command and date of birthday please."
        except ValueError:
            return "Invalid date format. Use DD.MM.YYYY."

    return inner


def input_error_show_birthday(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me command and name please."
        except AttributeError:
            return f"{args[0][0]} dont have date of birthday yet"
    return inner


def input_error_birthdays(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me command and name please."

    return inner