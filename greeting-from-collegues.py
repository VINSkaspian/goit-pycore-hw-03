from datetime import datetime, timedelta

def get_upcoming_birthdays(users, today=None):
    """
    Повертає список людей, яких потрібно привітати з днем народження
    протягом наступних 7 днів включно (з підрахованим
    перенесення на понеділок,
    якщо день народження випаде на вихідні).
    Параметри:
    users (list): список словників з 
    ключами 'name' та 'birthday' ('рік.місяць.день').
    today (date, optional): дата, з якої почнеться облік. 
    Якщо None — буде поточна дата.
    Повертає:
    list: список словників з ключами 'name' 
    та 'congratulation_date' ('рік.місяць.день').
    """
    if today is None:
        today = datetime.today().date()

    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        try:
            bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:

            continue
        birthday_this_year = bday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if today <= birthday_this_year <= end_date:

            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)

            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)
            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result
# Тестові дані
users = [
    {"name": "Yana Pechova", "birthday": "1985.01.23"},
    {"name": "Oleh Vovk", "birthday": "1990.01.27"},
    {"name": "Ivan Babish", "birthday": "1992.01.28"},
    {"name": "Olena Ivaniva", "birthday": "1995.01.29"},
]

# Встановлюємо тестову дату
test_date = datetime.strptime("2025.01.22", "%Y.%m.%d").date()

birthdays = get_upcoming_birthdays(users, today=test_date)
print("Список привітань на цьому тижні:", birthdays)
