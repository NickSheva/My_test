from tkinter import *
# создание объекта окна
root = Tk()
# создание заголовка окна
root.title('Conver Currency')
# создание виджетов метки. Кнопки и поля ввода создаются так же
label_1 = Label(root, text = 'Input the Amount of Conversion: ', font= 'arial 12 bold', borderwidth=10)
label_2 = Label(root, text= 'Conver from Currency: ', font= 'arial 10', borderwidth= 10)
label_3 = Label(root, text= 'Conver to Currency: ', font= 'arial 10', borderwidth= 10)
label_4 = Label(root, text= 'Converted Amount: ', font= 'arial 12 bold', borderwidth= 10)
# создание виджетов Entry для полей ввода

Entry_1 = Entry(root, borderwidth=5)
Entry_2 = Entry(root, borderwidth=5)
Entry_3 = Entry(root, borderwidth=5)
output = Entry(root, text = "Print the output here", font= 'arial 10', borderwidth=10)
# создание виджета Button для кнопки
my_button = Button(root, text = "CONVERT", font = "arial 10", borderwidth= 5)
# размещение ввиджетов в окне
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)
label_3.grid(row=2, column=0)
label_4.grid(row=4, column=0)
Entry_1.grid(row=0, column=1)
Entry_2.grid(row=1, column=1)
Entry_3.grid(row=2, column=1)
output.grid(row=3, column=0, columnspan=2)
my_button.grid(row=4, column=1)
# запускаем цикл
root.mainloop()