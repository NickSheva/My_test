#импорт библиотеки
from tkinter import *
# Создание объекта окна
# name = Tk()
# изменение заголовка (необезательно)
# name.title('my pp')
# name.geometry('350x350')
# создание виджета метки Кнопки и поля ввода создаются так же
# my_label = Label(name, text = 'Hello World')
# расширение виджета в окне
# my_label.pack()
# запуск бесконечного цикла
# name.mainloop())


# создание объекта окна
root = Tk()
# изменение заголовка
root.title('Currency Converter')
label1 = Label(root, text='Enter Amount for Conversion:', font='arial 12 bold', borderwidth=5)
label2 = Label(root, text='Convert from Currency:', font='arial 10', borderwidth=5)
label3 = Label(root, text='Convert to Currency:', font='arial 10', borderwidth=5)
label4 = Label(root, text='Converted Amount:', font='arial 10', borderwidth=5)
output = Label(root, text='Print the output here:', font='arial 12 bold', borderwidth=5)
# создание виджетов Entry для полей ввода
Entry1 = Entry(root, borderwidth=5)
Entry2 = Entry(root, borderwidth=5)
Entry3 = Entry(root, borderwidth=5)
# создание виджета Button для кнопкп
my_button = Button(root, text='CONVERT', font='arial 12 bold', borderwidth=5)

label1.pack()
label2.pack()
label3.pack()
label4.pack()
output.pack()
Entry1.pack()
Entry2.pack()
Entry3.pack()
my_button.pack()

root.mainloop()