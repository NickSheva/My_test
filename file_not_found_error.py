filename = 'alica.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'Sorry {filename} does not exist.')
else:
    print(contents)