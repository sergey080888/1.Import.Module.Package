from application import salary
from application.db import people
from datetime import date


def print_hi(name):

    print(f'Привет, {name}')


def current_date():

    print(f'Сегодня {date.today()}')


if __name__ == '__main__':
    current_date()
    print_hi('Сергей')
    salary.calculate_salary('1111')
    people.get_employees('Сергей')
