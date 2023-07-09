'''
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

START_BALLANS = 0  # начальный балланс
ALIQUOT_SUMM = 50  # кратность суммы пополнения и снятия
PERCENT_WITHDRAWAL = 0.015  # процент за снятие
MIN_SUMM_PERCENT = 30  # минимальная сумма за снятие
MAX_SUMM_PERCENT = 600  # мах сумма процента за снятия
PERCENT_N_OPERATION = 0.03  # процент за каждую N-ю операцию
ALIQUOT_OPERATION = 3  # кол-во операций после которых начисляется процент
TAX_WEALTH = 0.1  # налог на богатство
LOWER_SUMM_WEALTH = 5_000_000  # нижняя граница богатства


def menu(balance, count_operation):
    print(f"МЕНЮ: \n"
          f"1. Пополнить счет\n"
          f"2. Снять наличные\n"
          f"3. Вывод\n")
    num_operation = input('введите номер операции: \n')

    match num_operation:
        case '1':
            adding_money(balance, count_operation)
        case '2':
            withdrawal_money(balance, count_operation)
        case '3':
            exit_menu(balance)
        case _:
            error_menu(balance, count_operation)


def adding_money(balance, count_operation):
    summ_add = 0
    while (summ_add % ALIQUOT_SUMM != 0) or (summ_add == 0):  # кратность суммы
        summ_add = int(input(f"введите сумму, кратную {ALIQUOT_SUMM} у.е. для зачисления на счет: \n"))

    balance -= get_tax_wealth(balance)  # налог на богатство

    count_operation += 1
    balance += summ_add

    if (count_operation % ALIQUOT_OPERATION == 0) and (ALIQUOT_OPERATION != 0):  # процент за каждую N-ю операцию
        balance += get_percent_of_operation(balance)

    print(f"сумма денег на счете: {balance} у.е.\n ")
    menu(balance, count_operation)


def withdrawal_money(balance, count_operation):  # снятие
    summ_withdrawal = 0

    while (summ_withdrawal % ALIQUOT_SUMM != 0) or (summ_withdrawal == 0):  # кратность суммы
        summ_withdrawal = int(input(f"введите сумму, кратную {ALIQUOT_SUMM} у.е. для снятия: \n"))

    balance -= get_tax_wealth(balance)  # вычитаем налог на богатство

    tax_with = get_tax_withdrawal(summ_withdrawal)  # % за снятие
    if summ_withdrawal + tax_with > balance:
        print(" недостаточно средств на счете (сумма снятия + % за снятие)")
    else:
        count_operation += 1
        balance -= (summ_withdrawal + tax_with)  # - сумма снятия - % за снятие
        print(f'удержан {PERCENT_WITHDRAWAL * 100}% за снятие в размере {tax_with} у.е.')

        if (count_operation % ALIQUOT_OPERATION == 0) and (ALIQUOT_OPERATION != 0):  # + процент за каждую N-ю операцию
            balance += get_percent_of_operation(balance)

    print(f"сумма денег на счете: {balance} у.е. \n")
    menu(balance, count_operation)


def get_percent_of_operation(balance):  # процент за каждую N-ю операцию
    print(f'начислен {PERCENT_N_OPERATION * 100}%  в размере {round(balance * PERCENT_N_OPERATION, 0)} у.е.')
    return round(balance * PERCENT_N_OPERATION, 0)


def get_tax_wealth(balance):  # налог на богатство
    tax = 0
    if balance > LOWER_SUMM_WEALTH:
        tax = round(balance * TAX_WEALTH, 0)
        print(f'удержан налог на богатство {TAX_WEALTH * 100}% в размере {tax} у.е.')

    return tax


def get_tax_withdrawal(summ_withdrawal):  # % за снятие
    tax_with = round(summ_withdrawal * PERCENT_WITHDRAWAL, 0)

    if tax_with < MIN_SUMM_PERCENT:
        tax_with = MIN_SUMM_PERCENT
    elif tax_with > MAX_SUMM_PERCENT:
        tax_with = MAX_SUMM_PERCENT

    return tax_with


def exit_menu(balance):
    balance -= get_tax_wealth(balance)  # налог на богатство
    print(f"сумма денег на счете: {balance} у.е.\n ")
    quit()


def error_menu(balance, count_operation):
    balance -= get_tax_wealth(balance)  # налог на богатство
    print(f"сумма денег на счете: {balance} у.е.\n ")
    menu(balance, count_operation)


count_operation = 0
balance = START_BALLANS
menu(balance, count_operation)
