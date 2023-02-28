responses = {}
flag = True
while flag:
    name = input('What is your name: ')
    response = input('What place would you like to go?: ')
    responses[name] = response
    repeat = input('Would you mind anyone else response(yes/no): ')
    if repeat == 'no':
        flag = False
print('-----------RESULTS-----------')
for k, v in responses.items():
    print(f'{k.title()} wants to go to {v.title()}')
