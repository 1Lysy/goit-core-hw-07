def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone / name and date of birthday"
        except AttributeError:
            return "Contact or contact name is not found"
        except IndexError:
            return "Give me command and name please"
        except KeyError:
            return "Name not found"

    return inner