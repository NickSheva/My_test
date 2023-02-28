from tkinter import *
# создание объекта окна
root = Tk()
# создание заголовка окна
root.title('My app')
root.geometry('250x250')
# создание виджета метки. Кнопки и поля ввода создаются так же
my_label = Label(root, text = 'hello world')
# расширение виджетов в окне
my_label.pack()
# запуск бесконечтого цикла
root.mainloop()

