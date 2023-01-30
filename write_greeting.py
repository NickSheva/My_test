filename = 'guest_book.txt'
with open(filename, 'w') as f:
  while True:
    name = input('Enter your name: ')
    if name == 'q':
      break
    else:
      print(f'Hello {name.title()}!')
      f.write(f'Hello {name.title()}\n')
