import tkinter as tk
window = tk.Tk()

window.title('Currency Converter')
input_label = tk.Label(window, text= 'Input amount of conversion', font= 'arial 12 bold', borderwidth= 5)
label_fc = tk.Label(window, text= 'Convert from currency', font= 'arial 12', borderwidth= 5)
label_tc = tk.Label(window, text= 'Convert to currency', font= 'arial 12', borderwidth= 5)
outputlabel = tk.Label(window, text= 'Converted amount', font= 'arial 12', borderwidth= 5)

input_amount = tk.Entry(window, font= 'arial 12', borderwidth=5)
from_currency = tk.Entry(window, font= 'arial 12', borderwidth=5)
to_currency = tk.Entry(window, font= 'arial 12', borderwidth=5)
output = tk.Entry(window, font= 'arial 12', borderwidth=5)

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
convert_button = tk.Button(window, text= 'CONVERT', font= 'arial 16 bold', borderwidth=5,
                           padx= 50, bg= 'powder blue',
                           command=lambda: currency_converter(from_currency, to_currency, input_amount))
convert_button.grid(row=3, columnspan=2)
window.mainloop()



