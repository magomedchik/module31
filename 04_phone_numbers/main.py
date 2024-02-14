import re


numbers = ['9999999999', '8999999999', '7999999999', '999999-999', '9999x999999']


def check_number(numbers: list):
    count = 0
    for i_number in numbers:
        count += 1
        if len(i_number) == 10 and re.match(r'[89]\d', i_number) and not re.search(r'\D', i_number):
            print(f'{count} номер: все в порядке')
        else:
            print(f'{count} номер: не подходит')


check_number(numbers)
