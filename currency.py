from tkinter import *
from functools import partial

class SimpleTkForm(object):
    def __init__(self):
        self.root = Tk()

    def myform(self):
        self.root.title('My form')
        frame = Frame(self.root, pady=10)
        form_data = dict()
        form_fields = ['username', 'password', 'server name', 'database name']
        cnt = 0
        for form_field in form_fields:
            Label(frame, text=form_field, anchor=NW).grid(row=cnt,column=1, pady=5, padx=(10, 1), sticky="W")
            textbox = Text(frame, height=1, width=15)
            form_data.update({form_field: textbox})
            textbox.grid(row=cnt,column=2, pady=5, padx=(3,20))
            cnt += 1

        conn_test = partial(self.test_db_conn, form_data=form_data)
        Button(frame, text='Submit', width=15, command=conn_test).grid(row=cnt,column=2, pady=5, padx=(3,20))
        frame.pack()
        self.root.mainloop()

    def test_db_conn(self, form_data):
        data = {k:v.get('1.0', END).strip() for k,v in form_data.items()}
        # validate data or do anything you want with it
        print(data)


if __name__ == '__main__':
    api = SimpleTkForm()
    api.myform()