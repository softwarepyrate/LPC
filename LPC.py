# -----------------------------------------------------------
#
# v1.3-290922: Add if-else in enter_carpark and exit_carpark to handle errors
#
#
#
# -----------------------------------------------------------
import tkinter as tk
from tkinter import *
from tkinter import filedialog

import numberplate
from PIL import Image, ImageTk
from tkcalendar import DateEntry

import datebase_process
import fee

print("Welcome to the carpark")


# set up widget
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# set up windows, label and buttons
window = tk.Tk()
window.geometry("900x506")

window.title("Number Plate Scanner")
window.iconphoto(False, tk.PhotoImage(file="license-plate.png"))
window_frame = Frame(window, height=900, width=506)
window_frame.pack(anchor=N, expand=True)

exit_frame = Frame(window)
exit_frame.pack(anchor=SE)

window_font = ('times', 18, 'bold')
window_label = tk.Label(window_frame, text='Welcome to Car Park', fg="#C0C0C0", pady=50, padx=30, font=window_font)
window_label.grid(row=0, column=2)

# This button will call the numberplate_recognition
window_button_1 = tk.Button(window_frame, text='Enter Car Park', fg="#D3D3D3", padx=40, command=lambda: enter_carpark())
window_button_1.grid(row=2, column=1)
CreateToolTip(window_button_1, text='Upload License Plate Image\n'
                                    'for processing.')

# This button will call the timestamp

cal = DateEntry(window_frame, locale='en_AU', selectmode='day')
cal.grid(row=2, column=2, padx=20, pady=30)
CreateToolTip(cal, text='Select Date.')


def my_upd():  # triggered on Button Click
    selected_date = str(cal.get_date())
    l1.config(text="Selected Date is: " + selected_date)  # read and display date
    l2.config(text=datebase_process.export_report(selected_date))
    print(selected_date)


l1 = tk.Label(window_frame, text='Please Select Date', bg='yellow')
l1.grid(row=4, column=2)
l2 = tk.Label(window_frame, text='Result', bg='green')
l2.grid(row=5, column=2)
window_button_2 = tk.Button(window_frame, text='Report', fg="#D3D3D3", padx=40,
                            command=lambda: my_upd())  # using Button
window_button_2.grid(row=3, column=2)
CreateToolTip(window_button_2, text='View reported entries of vehicles\n'
                                    'based on selected date.')


# This button will call the timestamp
def exit_carpark():
    # Set global variable to make it displayed
    global displayed_exit_image
    f_types = [('All files', '*')]
    # f_types = [('PNG Files', '*.png')]

    # selected_filename is the actual pic (PNG)
    selected_filename = filedialog.askopenfilename(filetypes=f_types)

    # Load the image
    selected_image = Image.open(selected_filename)
    # resize image
    selected_image = selected_image.resize((168, 115), Image.Resampling.LANCZOS)
    #
    displayed_exit_image = ImageTk.PhotoImage(selected_image)
    # Use button to display the image
    window_button_6 = tk.Button(window_frame, image=displayed_exit_image)  # using Button
    window_button_6.grid(row=3, column=3)
    # Call numberplate_recognition and print the number plate
    numberplate_number = numberplate.numberplate_recognition(selected_filename)
    if numberplate_number == "!error":
        window_label_1 = tk.Label(window_frame, text="Error,try again", width=15, font=window_font)
        window_label_1.grid(row=4, column=3, pady=10, sticky=N)
    # numberplate_number = "test3"
    else:
        display_timestamp, exit_datatime = datebase_process.save_datetime(numberplate_number, 0)
        test_parking_fee = fee.fee_calculation(datebase_process.export_entry_datetime(numberplate_number),
                                               exit_datatime)
        window_label_1 = tk.Label(window_frame,
                                  text=numberplate_number + "\n" + display_timestamp + "\nParking Fee: $ " + str(
                                      test_parking_fee), width=15, font=window_font)
        window_label_1.grid(row=4, column=3, pady=10, sticky=N)

    # window_label_2 = tk.Label(window_frame, text=numberplate_timestamp,width=30,font=window_font)
    # window_label_2.grid(row=5,column=1)
    print(numberplate_number)
    pass


window_button_3 = tk.Button(window_frame, text='Exit Car Park', fg="#D3D3D3", padx=40,
                            command=lambda: exit_carpark())  # using Button
window_button_3.grid(row=2, column=3)
CreateToolTip(window_button_3, text='Input license plate to confirm\n'
                                    'time of exit and parking fees.')

# Quit Program
window_button_4 = tk.Button(exit_frame, text='Exit Program', fg="#D3D3D3", command=window.quit)  # using Button
window_button_4.grid(row=0, column=0)
CreateToolTip(window_button_4, text='Quit Program')

# Dark mode and styling
window.configure(bg="#505050")
window_frame.configure(bg="#505050")
exit_frame.configure(bg="#505050")
window_button_1.configure(bg="#696969")
window_button_2.configure(bg="#696969")
window_button_3.configure(bg="#696969")
window_button_4.configure(bg="#696969")
window_label.configure(bg="#505050")


def enter_carpark():
    # Set global variable to make it displayed
    global displayed_image
    f_types = [('All files', '*')]
    # f_types = [('PNG Files', '*.png')]

    # selected_filename is the actual pic (PNG)
    selected_filename = filedialog.askopenfilename(filetypes=f_types)

    # Load the image
    selected_image = Image.open(selected_filename)
    # resize image
    selected_image = selected_image.resize((168, 115), Image.Resampling.LANCZOS)
    #
    displayed_image = ImageTk.PhotoImage(selected_image)
    # Use button to display the image
    window_button_4 = tk.Button(window_frame, image=displayed_image)  # using Button
    window_button_4.grid(row=3, column=1)
    # Call numberplate_recognition and print the number plate
    numberplate_number = numberplate.numberplate_recognition(selected_filename)
    # print(numberplate_number)
    if numberplate_number == "!error":
        window_label_1 = tk.Label(window_frame, text="Error,try again", width=15, font=window_font)
        window_label_1.grid(row=4, column=1, pady=10, sticky=N)
    else:
        numberplate_timestamp = datebase_process.save_datetime(numberplate_number, 1)
        window_label_1 = tk.Label(window_frame, text=numberplate_number + "\n" +
                                                     numberplate_timestamp, width=15, font=window_font)
        window_label_1.grid(row=4, column=1, pady=10, sticky=N)

    # window_label_2 = tk.Label(window_frame, text=numberplate_timestamp,width=30,font=window_font)
    # window_label_2.grid(row=5,column=1)
    print(numberplate_number)


# Keep the window opens
window.mainloop()
