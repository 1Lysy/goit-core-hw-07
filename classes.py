from collections import UserDict
from datetime import datetime, date, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
         super().__init__(name)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError('Invalid phone number')
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')  
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)  

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []    
        self.birthday = None

    def add_phone(self, phone):
         p = Phone(phone)
         self.phones.append(p)  

    def remove_phone(self, phone):
        elem = self.find_phone(phone)
        if elem:
            self.phones.remove(elem)

    def edit_phone(self, number, new_number):
        num = self.find_phone(number)
        if num:
            self.add_phone(new_number)
            self.remove_phone(number)
        else:
            raise ValueError('Phone number not found')

    
    def find_phone(self, phone):
        for elem in self.phones:
            if phone == elem.value:
                return elem

    def add_birthday(self, birthday):
        b = Birthday(birthday)
        self.birthday = b
                          
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, date of birthday: {self.birthday.value}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
        
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)

    def __str__(self):
        values = [str(v) for v in self.data.values()]
        my_str = '\n'.join(values)
        return my_str
    
    def date_to_string(self, date):
        return date.strftime("%Y.%m.%d")

    def find_next_weekday(self, start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)
    
    def adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5:
            return self.find_next_weekday(birthday, 0)
        return birthday
    
    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()

        for record in self.data.values():
            if record.birthday is None:
                continue
            birthday_date = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()
            birthday_this_year = birthday_date.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_date.replace(year=today.year + 1)

            if 0 <= (birthday_this_year - today).days < days:
                birthday_this_year = self.adjust_for_weekend(birthday_this_year)
                congratulation_date_str = self.date_to_string(birthday_this_year)
                upcoming_birthdays.append({"name": record.name.value, "birthday": congratulation_date_str})
        return upcoming_birthdays

