from datetime import datetime
dt = datetime.today()
print(dt.strftime('%H:%M - %m-%d-%Y'))
print(dt.strftime(f'{"%H"} часов {"%M"} минут {"%m-%d-%Y"} года'))
print(f'День: {dt:%d}, День недели: {dt:%A}, Месяц: {dt:%m}, Время: {dt:%H:%M}')
print()
# преобразование datetime в строку для базы данных
print(datetime.now().isoformat())
print()
import datetime
# преобразование datetime.today() в строку для базы данных
print(datetime.date.today().isoformat())
n = datetime.date(2021, 12, 12)
print(n)