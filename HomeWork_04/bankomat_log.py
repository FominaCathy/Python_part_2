'''
дополннение к программе банкомат:
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

'''
Добавлены:
- список логов: снятия и начисления ДС на счет
- вывод их на экран после кончания работы банкомата (после выхода) 
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

    tax = get_tax_wealth(balance)  # налог на богатство
    if tax > 0:
        balance -= tax
        list_logging.append(('снятие', tax, 'налог на богатство'))

    count_operation += 1
    balance += summ_add
    list_logging.append(('зачисление', summ_add, 'зачисление ДС'))

    balance += bonus_of_operation(count_operation, balance)

    print(f"сумма денег на счете: {balance} у.е.\n ")
    menu(balance, count_operation)


def withdrawal_money(balance, count_operation):  # снятие
    summ_withdrawal = 0

    while (summ_withdrawal % ALIQUOT_SUMM != 0) or (summ_withdrawal == 0):  # кратность суммы
        summ_withdrawal = int(input(f"введите сумму, кратную {ALIQUOT_SUMM} у.е. для снятия: \n"))

    tax = get_tax_wealth(balance)  # налог на богатство
    if tax > 0:
        balance -= tax
        list_logging.append(('снятие', tax, 'налог на богатство'))

    tax_with = get_tax_withdrawal(summ_withdrawal)  # % за снятие
    if summ_withdrawal + tax_with > balance:
        print(" недостаточно средств на счете (сумма снятия + % за снятие)")
    else:
        count_operation += 1
        balance -= (summ_withdrawal + tax_with)  # - сумма снятия - % за снятие
        list_logging.append(('снятие', summ_withdrawal, 'Снятие ДС'))
        list_logging.append(('снятие', tax_with, f'удержан {PERCENT_WITHDRAWAL * 100}% за снятие'))

        balance += bonus_of_operation(count_operation, balance)

    print(f"сумма денег на счете: {balance} у.е. \n")
    menu(balance, count_operation)


def bonus_of_operation(count_operation, balance):
    """начисление бонуса"""
    bonus = 0
    if (count_operation % ALIQUOT_OPERATION == 0) and (ALIQUOT_OPERATION != 0):  # + процент за каждую N-ю операцию
        bonus = round(balance * PERCENT_N_OPERATION, 0)

        if bonus > 0:
            list_logging.append(('зачисление', bonus, f'бонус за {ALIQUOT_OPERATION}-ю операцию'))

    return bonus


def get_tax_wealth(balance):  # налог на богатство
    """сумма налога на богатство"""
    tax = 0
    if balance > LOWER_SUMM_WEALTH:
        tax = round(balance * TAX_WEALTH, 0)
    return tax


def get_tax_withdrawal(summ_withdrawal):  # % за снятие
    """сумма % за снятие ДС"""
    tax_with = round(summ_withdrawal * PERCENT_WITHDRAWAL, 0)

    if tax_with < MIN_SUMM_PERCENT:
        tax_with = MIN_SUMM_PERCENT
    elif tax_with > MAX_SUMM_PERCENT:
        tax_with = MAX_SUMM_PERCENT

    return tax_with


def exit_menu(balance):
    tax = get_tax_wealth(balance)  # налог на богатство
    if tax > 0:
        balance -= tax
        list_logging.append(('снятие', tax, 'налог на богатство'))
    print(f"сумма денег на счете: {balance} у.е.\n ")


def error_menu(balance, count_operation):
    tax = get_tax_wealth(balance)  # налог на богатство
    if tax > 0:
        balance -= tax
        list_logging.append(('снятие', tax, 'налог на богатство'))
    print(f"сумма денег на счете: {balance} у.е.\n ")

    menu(balance, count_operation)


def print_logging(logs: list(tuple())):
    print(f'операция       сумма          комментарий')
    for record in logs:
        current_row = f'{record[0]:<15}{record[1]:<15_}{record[2]}'
        print(current_row)


count_operation = 0
list_logging = list(tuple())
balance = START_BALLANS
menu(balance, count_operation)

print("Логи:")
print_logging(list_logging)
