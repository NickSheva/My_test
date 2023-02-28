from tkinter import *
# создание окна виджета
root = Tk()
# создание загаловка
root.title('Калькулятор процентов')
#root.geometry('550x350')
# создание виджетов Кнопки и поля ввода создаются так же

input_label = Label(root, text='Сумма залога:', font='arial 20 bold', borderwidth=5)
label_fc = Label(root, text='Количество дней:', font='arial 20', borderwidth=5)
label_tc = Label(root, text='Процентная ставка:', font='arial 20', borderwidth=5)
outputlabel = Label(root, text='Проценты:', font='arial 20 bold', borderwidth=5)

# создание виджетов Entry для полей
input_amount = Entry(root, borderwidth=5)
amount_days = Entry(root, borderwidth=5)
percentage_rate = Entry(root, borderwidth=5)
output = Entry(root, text='Print the output here:', font='arial 30', borderwidth=5)


input_label.grid(row=0, column=0)
label_fc.grid(row=1, column=0)
label_tc.grid(row=2, column=0)

input_amount.grid(row=0, column=1)
amount_days.grid(row=1, column=1)
percentage_rate.grid(row=2, column=1)
outputlabel.grid(row=4, column=0)
output.grid(row=4, column=1)



import requests
rates = {}
data = requests.get(url).json()

rates = data['rates']


def currency_converter(amount_days, to_currency, input_amount):
    amount_days = int(amount_days.get())
    percentage_rate = int(to_currency.get())
    input_amount = float(input_amount.get())
    #if to_currency in range(1,30):
    output.insert(0, round(input_amount * rates[percentage_rate] / 100, 2))
    #elif to_currency in range(30, 60):
        #output.insert(0, round(input_amount * rates[from_currency] / 100, 2))

    return
convert_button = Button(root, text= 'CONVERT', font= 'arial 16 bold', borderwidth=5,
                           padx= 50, bg= 'powder blue',
                           command=lambda: currency_converter(amount_days, percentage_rate, input_amount))
convert_button.grid(row=3, columnspan=2)
root.mainloop()


