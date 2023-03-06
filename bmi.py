from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Калькулятор индекса массы тела (ИМТ)')
window.geometry('400x300')

frame = Frame(window, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10 ) #Задаём отступ по вертикали.
frame.pack(expand=True) #Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.
label1 = Label(frame, text='Введите свой вес в кг', font='arial 16 bold', fg='purple')
label2 = Label(frame, text='Введите свой рост в см', font='arial 16 bold', fg='purple')

weight = Entry(frame, font='arial 16 bold')
height = Entry(frame, font='arial 16 bold')
output = Entry(frame, font='arial 16 bold')

label1.grid(row=1, column=1)
label2.grid(row=2, column=1)

weight.grid(row=1, column=2)
height.grid(row=2, column=2)
def decide(weight, height):
    weight = int(weight.get())
    height = int(height.get())
    output = round(weight / (height / 100) ** 2)

    if output < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {output } соответствует недостаточному весу')
    elif (output > 18.5) and (output  < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {output } соответствует нормальному весу')
    elif (output  > 24.9) and (output  < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {output } соответствует избыточному весу')
    else:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {output } соответствует ожирению')
    return

my_button = Button(frame, text='Рассчитать ИМТ', font='arial 14 bold', command=lambda: decide(weight, height),
                   fg='green')

my_button.grid(row=3, column=1, columnspan=2)
window.mainloop()
