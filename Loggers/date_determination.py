'''
Задание №5
📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответсвует формату.

📌 Добавьте возможность запуска из командной строки.
📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
📌 *Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.
'''
import argparse
from datetime import datetime
import logging


def convert(text: str):
    try:
        number, week_day, month = text.split()
        week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'субббота', 'воскресенье']
        months = ['', 'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']

        wd = int(week_day) if week_day.isdigit() else week.index(week_day)
        number = int(number[0])
        cur_month = int(month) if month.isdigit() else months.index(month[:3])
        cur_year = datetime.now().year
        count = 0

        for item in range(1, 32):
            cur_date = datetime(day=item, month=cur_month, year=cur_year)
            if cur_date.weekday() == wd:
                count += 1
                if count == number:
                    logger.info(f'дата: "{cur_date}"')
                    return cur_date
    except Exception as ex:
        logger.error(f'некорретный формат: "{text}", error: {ex}')
        print('некорретный формат')
        return

    logger.warning(f'некорретный формат: "{text}", такой даты нет')


if __name__ == '__main__':
    logging.basicConfig(filename='logger_date.log', style='{', filemode='a', encoding='utf-8', level=logging.NOTSET)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='my')
    parser.add_argument('-n', metavar='n', type=str, default=1, help='номер вхождения дня недели в формате "1-й"')
    parser.add_argument('-w', metavar='w', type=str, default=datetime.now().weekday(), help='название дня недели либо его номер (0-понед, 6- воскр)')
    parser.add_argument('-m', metavar='m', type=str, default=datetime.now().month, help='название месяца либо его номер: 1- январь, 12-декабрь')

    args = parser.parse_args()
    txt = f"{args.n} {args.w} {args.m}"

    print(f'{convert(txt)}')
