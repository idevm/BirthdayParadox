"Иммитационное моделирование парадокса дней рождения"

from datetime import date, timedelta
import random
from typing import Optional

def getBirthdays(numberOfBirthdays: int) -> 'list[date]':
    birthdays: list[date] = []
    for _ in range(numberOfBirthdays):
        startOfYear: date = date(2001,1,1)
        randomNumberOfDays: timedelta = timedelta(random.randint(0, 364))
        birthday: date = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays: 'list[date]') -> Optional[date]:
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, dateA in enumerate(birthdays):
        for b, dateB in enumerate(birthdays[a + 1:]):
            if dateA == dateB:
                return dateA

def main():
    print('''Парадокс дней рождения

    Программа показывает, что в группе из N людей вероятность совпадения дней рождения у двух из них удивительно большая. На самом деле это не парадокс, а немного неожиданный результат.''')

    MONTHS: list[str] = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')

    while True:
        print('Сколько дней рождения сгенерировать? (мин 2, макс 100)')
        response: str = input('> ')
        if response.isdecimal() and (1 < int(response) <= 100):
            numBDays: int = int(response)
            break

    print()

    print(f'Сгенерировано {numBDays} дней рождения:')
    birthdays: list[date] = getBirthdays(numBDays)
    for i, bd in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
        monthName: str = MONTHS[bd.month - 1]
        dateText: str = f'{bd.day} {monthName}'
        print(dateText, end='')

    print('\n\n')

    match: Optional[date] = getMatch(birthdays)

    print('В этой симуляции ', end='')
    if match != None:
        monthName: str = MONTHS[match.month - 1]
        dateText: str = f'{match.day} {monthName}'
        print(f'у некоторых людей совпали дни рождения: {dateText}.\n')
    else:
        print('нет совпадающих дней рождения.\n')

    print(f'Генерация {numBDays} случайных дней рождения 100000 раз...')
    
    input('Нажмите Enter чтобы начать')

    print('Генерируется 100000 симуляций')
    simMatch: int = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, 'сгенерировано...')
        birthdays: list[date] = getBirthdays(numBDays)
        if getMatch(birthdays) != None:
            simMatch += 1

    print('Сгенерировано 100000 симуляций')

    probability: float = round(simMatch / 100_000 * 100, 2)
    print(f'''Из 100000 симуляций групп численностью {numBDays} человек, дни рождения двух человек совпали {simMatch} раз. Это значит, что среди {numBDays} человек вероятность совпадения дней рождения составляет {probability}%. Наверняка это больше, чем вы могли представить!''')

if __name__ == '__main__':
    main()