responses = {}
flag = True
while flag:
    name = input('Enter your name: ').title()
    response = input('What place would you like to go: ').title()
    responses[name] = response
    repeat = input('Would you mind to response anyone else (yes/no): ')
    if repeat == 'no':
        flag = False
print('----------RESULTS OF POLLING-------')
for k, v in responses.items():
    print(f'{k} wants to go to {v}')

responses = {}
flag = True
while flag:
    name = input('What is your name? ')
    place = input('What place would you like to go? ')
    responses[name] = place
    repeat = input('Do you want another one to response (yes/no)?  ')
    if repeat == 'no':
        flag = False
print('--------RESULTS------------')
for k, v in responses.items():
    print(f'{k.title()} want to go to {v.title()}')
