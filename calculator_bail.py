from tkinter import *

def clear_all():
    principal_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)
    # set focus on the principal_field entry box
    principal_field.focus_set()

def calculate_ci():
    # get a content from entry box
    principal = int(principal_field.get())
    rate = float(rate_field.get())
    time = int(time_field.get())

    CI = principal * (pow((1 + rate / 100), time))

    compound_field.insert(10, CI)

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x250")

    root.title("Calculator")

    label1 = Label(root, text="Bail(sum) : ", fg='black')
    label2 = Label(root, text="Rate(%) : ", fg='black')
    label3 = Label(root, text="Time(years) : ", fg='black')
    label4 = Label(root, text="Compound Interest : ", fg='black')

    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=5, column=0, padx=10, pady=10)

    principal_field = Entry(root)
    rate_field = Entry(root)
    time_field = Entry(root)
    compound_field = Entry(root)

    principal_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    compound_field.grid(row=5, column=1, padx=10, pady=10)

    button1 = Button(root, text="Submit", bg="red", fg="black", command=calculate_ci)
    button2 = Button(root, text="Clear", bg="red", fg="black", command=clear_all)

    button1.grid(row=4, column=1, pady=10)
    button2.grid(row=6, column=1, pady=10)

    root.mainloop()

