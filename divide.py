print('Tell me two numbers and i divide them')
print('If you wanna quit, enter "q"')
while True:
    num1 = input('Enter number one: ')
    if num1 == 'q':
        break
    num2 = input('Enter number two: ')
    if num2 == 'q':
        break
    try:
        answer = f'{num1} / {num2} = {int(num1)/ int(num2)}'
    except ZeroDivisionError:
        print('You cannot divide by zero')
    else:
        print(answer)