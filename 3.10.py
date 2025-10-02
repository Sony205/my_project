from datetime import datetime

def format_datetime(dt: datetime) -> str:
    day = dt.day
    year = dt.year
    months = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]
    month_name = months[dt.month - 1]
    time_str = f"{dt.hour:02d}:{dt.minute:02d}"

    return f"Сегодня {day} {month_name} {year} года, время: {time_str}"


now = datetime.now()
print(format_datetime(now))
