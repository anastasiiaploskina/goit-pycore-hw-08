# --------------------
# Classes for managing contact information
# --------------------

import re
from collections import UserDict
from datetime import datetime, timedelta

from constants import DATE_FORMAT


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, phone_number):
        self.is_valid(phone_number)
        super().__init__(value=phone_number)

    @staticmethod
    def is_valid(phone_number):
        pattern = r'^\d{10}$'
        match = bool(re.search(pattern, phone_number))
        if not match:
            raise ValueError("Invalid phone number format. Please try again.")


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, DATE_FORMAT)

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return f"{self.value.strftime(DATE_FORMAT)}"


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        found = self.find_phone(phone_number)
        if found:
            self.phones.remove(found)

    def edit_phone(self, old_phone, new_phone):
        found = self.find_phone(old_phone)
        if found:
            Phone.is_valid(new_phone)
            found.value = new_phone
        else:
            raise KeyError("Phone number to edit not found")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days=7):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.values():
            if record.birthday:
                birthday = record.birthday.value

                try:
                    birthday_date = birthday.replace(year=today.year).date()
                except ValueError:
                    birthday_date = birthday.replace(year=today.year, day=28).date()

                if birthday_date < today:
                    try:
                        birthday_date = birthday.replace(year=today.year + 1).date()
                    except ValueError:
                        birthday_date = birthday.replace(year=today.year + 1, day=28).date()

                days_until_birthday = (birthday_date - today).days

                if 0 <= days_until_birthday <= days:
                    day_of_week = birthday_date.weekday()

                    if day_of_week == 6:
                        celebration_date = birthday_date + timedelta(days=1)
                    elif day_of_week == 5:
                        celebration_date = birthday_date + timedelta(days=2)
                    else:
                        celebration_date = birthday_date

                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": celebration_date.strftime(DATE_FORMAT)
                    })
        return upcoming_birthdays
