# on Button click reading and displaying date selection
import tkinter as tk

from tkcalendar import DateEntry

import datebase_process

my_w = tk.Tk()
my_w.geometry("380x220")

cal = DateEntry(my_w, locale='en_AU', selectmode='day')
cal.grid(row=1, column=1, padx=20, pady=30)


def my_upd():  # triggered on Button Click
    selected_date = str(cal.get_date())
    l1.config(text="Selected Date is: " + selected_date)  # read and display date
    l2.config(text=datebase_process.export_report(selected_date))
    print(selected_date)


l1 = tk.Label(my_w, text='Please Select Date', bg='yellow')
l1.grid(row=3, column=1)
l2 = tk.Label(my_w, text='Result', bg='green')
l2.grid(row=4, column=1)

b1 = tk.Button(my_w, text='Generate Report', command=lambda: my_upd())
b1.grid(row=2, column=1, padx=20, pady=30)

print()
my_w.mainloop()
