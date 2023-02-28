from tkinter import *
# создание окна виджета
root = Tk()
# создание загаловка
root.title('Currency Converter')
#root.geometry('550x350')
# создание виджетов Кнопки и поля ввода создаются так же

input_label = Label(root, text='Enter the Amount for Conversion:', font='arial 20 bold', borderwidth=5)
label_fc = Label(root, text='Convert from Currency:', font='arial 20', borderwidth=5)
label_tc = Label(root, text='Convert to Currency:', font='arial 20', borderwidth=5)
outputlabel = Label(root, text='Converted amount:', font='arial 20 bold', borderwidth=5)

# создание виджетов Entry для полей
input_amount = Entry(root, borderwidth=5)
from_currency = Entry(root, borderwidth=5)
to_currency = Entry(root, borderwidth=5)
output = Entry(root, text='Print the output here:', font='arial 20', borderwidth=5)


input_label.grid(row=0, column=0)
label_fc.grid(row=1, column=0)
label_tc.grid(row=2, column=0)

input_amount.grid(row=0, column=1)
from_currency.grid(row=1, column=1)
to_currency.grid(row=2, column=1)
outputlabel.grid(row=4, column=0)
output.grid(row=4, column=1)

ACCESS_KEY = '1cf94c2fd27ab40a0b510ccec2d0014b'
url = str.__add__('http://data.fixer.io/api/latest?access_key=', ACCESS_KEY)

import requests

data = requests.get(url).json()

rates = data['rates']


def currency_converter(from_currency, to_currency, input_amount):
    from_currency = from_currency.get()
    to_currency = to_currency.get()
    input_amount = float(input_amount.get())
    if from_currency != 'EUR':
        input_amount = input_amount / rates[from_currency]
    output.insert(0, round(input_amount * rates[to_currency], 2))
    return
convert_button = Button(root, text= 'CONVERT', font= 'arial 16 bold', borderwidth=5,
                           padx= 50, bg= 'powder blue',
                           command=lambda: currency_converter(from_currency, to_currency, input_amount))
convert_button.grid(row=3, columnspan=2)
root.mainloop()


