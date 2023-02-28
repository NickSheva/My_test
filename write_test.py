from random import randint
while True:
    s = print('Flip a coin')
    a = randint(0,1)
    if a == 0:
        print('head')
    else:
        print('tail')
    res = input('Do you want to flip another one (yes/ no): ')
    if res == 'no':
        break

