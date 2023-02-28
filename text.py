file = 'textf.txt'
with open(file, 'w') as f:
    word = ''
    while word.upper() != 'END':
        word = input('Enter: ')
        f.write(word + '\n')






