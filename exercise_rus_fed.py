def right_number(d):
    if 1<=d<=100:
        return "Russian " * (not d%3) + "Federation" * (not d%5) or d
    else:
        return f"This number {d} isn't wrong"

d = int(input('Enter number from 1 to 100: '))
print(right_number(d))
