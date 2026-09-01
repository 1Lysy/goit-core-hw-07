import decorators as dec
from classes import AddressBook, Record, Phone

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@dec.input_error
def add_contact(args, contacts):
    name, phone = args
    record = contacts.find(name)
    if record is None:
        record = Record(name)
        contacts.add_record(record)
    record.add_phone(phone)
    return "Contact added."

@dec.input_error
def change_contact(args, book):
    name, new_phone = args
    record = book.find(name)
    if record:
        record.phones = [Phone(new_phone)]
        return 'contact updated'
    else:
        return 'contact is not found'
    
@dec.input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

def show_all(contacts):
    lines = []
    if not contacts:
        return 'Contacts list is empty'
    for name, phone in contacts.items():
        line = f'{name} - {phone}'
        lines.append(line)
    all_phones = '\n'.join(lines)
    return all_phones

@dec.input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return 'date of birthday is added'
    return 'name not found'

@dec.input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return record.birthday.value # остання зміна була тут
    return 'not found'   

@dec.input_error
def birthdays(book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return 'No upcoming birthdays.'
    return '/n'.join(f'{item['name']} : {item['birthday']}' for item in upcoming)

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ") 
        if not user_input.strip():
            print('Enter command please')
            continue
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == 'change':
            print(change_contact(args, book))
        elif command == 'phone':
            print(show_phone(args, book))
        elif command == 'all':
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()