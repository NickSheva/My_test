from datetime import date
def your_age(y, m, d):
    today = date.today()
    return today.year - a - ((today.month, today.day) < (m, d))
y, m, d = map(int, input().split())
print(year_of_birth(y, m, d))






