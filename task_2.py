import decorators as dec
from task_1 import AddressBook, Record

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@dec.input_error_add_contact
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

@dec.input_error_change_contact
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return 'number is edited'
    return f'{name} not found'

@dec.input_error_show_phone    
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return record
    return 'not found' 

def show_all(book):
    if not book:
        return 'Contacts list is empty'
    return str(book)

@dec.input_error_add_birthday
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return 'contact is added'
    return 'name not found'


@dec.input_error_show_birthday
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return record.birthday.value.strftime('%d.%m.%Y')
    return 'not found'   

# при виводі дати народження не повинно бути годин. тільки дата

@dec.input_error_birthdays
def birthdays(args, book):
    return book.get_upcoming_birthdays()
        

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
            print(birthdays(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()