def soul(num):
    while len(str(num)) > 1:
        num = sum([int(i) for i in list(str(num)) if i.isdigit()])
    return num
num = '30.04.1980'
print(soul(num))