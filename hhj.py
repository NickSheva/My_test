import tkinter as tk
window = tk.Tk()

window.title("Currency Convertor")

Input_label = tk.Label(window, text = "Bail", font = "arial 12 bold", borderwidth = 10)
amount_days = tk.Label(window, text = "What day :", font = "arial 12 ", borderwidth = 10)

input_amount = tk.Entry(window, font = "arial 12 bold", borderwidth = 5)
days = tk.Entry(window, font = "arial 12 bold", borderwidth = 5)
output = tk.Entry(window, font = "arial 12 bold", borderwidth = 5)

Input_label.grid(row = 0, column = 0)
amount_days.grid(row = 1, column = 0)

input_amount.grid(row = 0, column = 1)
days.grid(row = 1, column = 1)
output.grid(row = 3, column = 1)

#data = requests.get(url).json()

#rates = data['rates']
def currency_converter(money, day):
    money = int(money.get())
    day = int(day.get())

    output.insert(0, round(input_amount * rates[to_currency], 2))
    return
    money = int(money.get())
    day = int(day.get())



convert_button = tk.Button( window , text = "CONVERT",font = "arial 16 bold",
                    borderwidth = 10, padx = 50, bg = "powder blue", command = currency_converter)
convert_button.grid(row = 2, columnspan = 2)

window.mainloop()