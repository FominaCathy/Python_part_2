'''
2. Напишите программу, которая получает целое число
и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

HEX_SYSTEM = 16
HEX_LIST: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def transfer_system(number: int) -> str:
    result: str = ''

    while number != 0:
        mod: int = number % HEX_SYSTEM
        result = str(HEX_LIST[mod]) + result
        number //= HEX_SYSTEM

    return result


number: int = int(input('введите число:\n'))
transfer: str = transfer_system(number)

print(f'\nРезультат перевода: {transfer}')
print(f'шестнадцатитиричная система: {hex(number)[2:]}')
