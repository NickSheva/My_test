import datetime

def year_of_birth(age):
    today = datetime.datetime.now().date()
    return int((today - age).days / 365.25)

age = datetime.date(42, 4, 30)

print(year_of_birth(age))
