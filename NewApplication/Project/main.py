def valid_string(value: str) -> bool:
    for x in value:
        if not (x.isalnum() or x.isspace()):
            return False
    return True


def valid_float(value: str) -> bool:
    for x in value:
        if not (x.isnumeric() or x == '.'):
            return False
    return True


def string_input(key) -> str:
    var = input('\n\n' + key)
    valid = valid_string(var)
    if not valid:
        print('\n\nInvalid input. Please reenter.')
        return string_input(key)
    return var


def float_input(key) -> float:
    var = input('\n\n' + key)
    valid = valid_float(var)
    if not valid:
        print('\n\nInvalid input. Please reenter.')
        return float_input(key)
    num = float(var)
    if float < 0:
        print('\n\nInvalid input. Please reenter.')
        return float_input(key)
    return num


def age_input() -> int:
    var = input('\n\nAge: ')
    if not var.isnumeric():
        print('\n\nInvalid input. Please reenter.')
        return age_input()
    num = int(var)
    if num < 0 or num > 120:
        print('\n\nInvalid input. Please reenter.')
        return age_input()
    return num


def gender_input() -> str:
    var = input('\n\nGender(M/F/T): ')
    if not (var == 'F' or var == 'M' or var == 'T'):
        print('\n\nInvalid input. Please reenter.')
        return gender_input()
    return var


print('\n\n\n\t\t\t\t\tNEW APPLICATION\n')

name = string_input('Name: ')
age = age_input()
gender = gender_input()
salary = float_input('Salary: ')
state = string_input('State: ')
city = string_input('City: ')
