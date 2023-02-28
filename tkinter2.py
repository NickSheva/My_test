from tkinter import *
# создание объекта окна
root = Tk()
# создание загаловка окна
root.title('Currency Convert')
# создание виджетов метки. кнопки для ввода создаются так же
label_1 = Label(root, text = 'Input the amount for conversion: ', font = 'arial 12 bold', borderwidth = 10)
label_2 = Label(root, text = 'Convert from Currency: ', font= 'arial 10', borderwidth=10)
label_3 = Label(root, text= 'Convert to Currency: ', font= 'arial 10', borderwidth= 10)
label_4 = Label(root, text= 'Converted Amount: ', font= 'arial 10', borderwidth= 10)
output = Label(root, text= 'Print the ooutput here: ', font= 'arial 10', borderwidth=10)
# создание виджетов Entry полей ввода
Entry_1 = Entry(root, borderwidth=5)
Entry_2 = Entry(root, borderwidth=5)
Entry_3 = Entry(root, borderwidth=5)
# создание виджета Button для кнопки
my_button = Button(root, text = 'CONVERT', font= 'arial 10', borderwidth=5)
# размещиние виджетов в окне
label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
Entry_1.pack()
Entry_2.pack()
Entry_3.pack()
my_button.pack()
# запускаем цикл
root.mainloop()