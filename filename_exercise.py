text = '''Белеет парус одинокой
В тумане моря голубом!..
Что ищет он в стране далекой?
Что кинул он в краю родном?...
Играют волны — ветер свищет,
И мачта гнется и скрыпит...
Увы! Он счастия не 'Как' ищет
И не от счастия бежит!
Под ним струя светлей лазури,
Над ним луч солнца золотой...
А он, мятежный, просит бури,
Как будто в бурях есть покой!

'''
filename = open('venv/text.txt', 'w')
filename.close()
filename = 'venv/text.txt'
with open(filename, 'w') as f:
    f.write(text)
with open(filename, 'r') as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())
with open(filename, 'a') as f:
    f.write('М.Ю. Лермонтов.\n')
    f.write('1841')
with open(filename, 'r') as f:
    line = f.read()
    print(line)
