file = "my_text.txt"
with open(file, 'w') as f:
  for i in range(3):
    name = input("Enter your name: ").title()
    f.write(f"{name}\n")
print("List is written.")
print()
file = "my_text.txt"
with open(file, 'a') as f:
  print("If you wont to quit enter (q)")
  while True:
    name = input("Add new name: ").title()
    if name == 'q'.title():
      break
    f.write(f"{name}\n")
     
print("List is written into.")
print()
file = "my_text.txt"
with open(file, 'r') as f:
  lines = f.read()
print(lines)
