from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date


def print_hi(name):

    print(f'Привет, {name}')


def current_date():

    print(f'Сегодня {date.today()}')


if __name__ == '__main__':
    current_date()
    print_hi('Сергей')
    calculate_salary('1111')
    get_employees('Сергей')
