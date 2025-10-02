from datetime import date, timedelta


birthday = date(2005, 10, 21)
today = date.today()
days_since_birthday = (today - birthday).days
this_year_birthday = birthday.replace(year=today.year)

if this_year_birthday < today:
    next_birthday = this_year_birthday.replace(year=today.year + 1)
else:
    next_birthday = this_year_birthday

days_until_next_birthday = (next_birthday - today).days

print(f"Дней прошло с момента рождения: {days_since_birthday}")
print(f"Дней до следующего дня рождения: {days_until_next_birthday}")
