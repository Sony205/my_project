from datetime import datetime, date


now = datetime.now()
print("Текущая дата и время:", now.strftime("%Y-%m-%d %H:%M:%S"))

today = date.today()
print("Только текущая дата:", today.strftime("%Y-%m-%d"))

current_time = now.time()
print("Только текущее время:", current_time.strftime("%H:%M:%S"))
