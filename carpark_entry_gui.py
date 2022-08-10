# -----------------------------------------------------------
#
#
#
#
#
# -----------------------------------------------------------

import os
import numberplate
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from tkinter import Tk,filedialog,Button,Label


print("Welcome to the carpark")

#set up windows, label and buttons
window = tk.Tk()
window.geometry("900x506")

window_frame = Frame(window, height = 900, width = 506)
window_frame.pack(anchor = N, expand = True)

exit_frame = Frame(window)
exit_frame.pack(anchor = SE)

window_font=('times', 18, 'bold')
window_label = tk.Label(window_frame, text = 'Welcome to Car Park', fg = "#C0C0C0", pady = 50, padx = 30, font=window_font)  
window_label.grid(row = 0, column = 2)

#This button will call the numberplate_recognition
window_button_1 = tk.Button(window_frame, text = 'Enter Car Park', fg = "#D3D3D3",  padx = 40, command = lambda:upload_file())
window_button_1.grid(row = 2, column = 1)  
    
#This button will call the timestamp
window_button_2 = tk.Button(window_frame, text = 'Time Stamp', fg = "#D3D3D3",  padx = 40) # using Button 
window_button_2.grid(row = 2, column = 2)

#This button will call the timestamp
window_button_3 = tk.Button(window_frame, text ='Exit Car Park', fg = "#D3D3D3",  padx = 40) # using Button 
window_button_3.grid(row = 2, column = 3)

#Quit Program
window_button_4 = tk.Button(exit_frame, text = 'Exit Program', fg = "#D3D3D3", command = window.quit) # using Button
window_button_4.grid(row = 0, column = 0) 

#Dark mode and styling
window.configure(bg = "#505050")
window_frame.configure(bg = "#505050")
exit_frame.configure(bg = "#505050")
window_button_1.configure(bg = "#696969")
window_button_2.configure(bg = "#696969")
window_button_3.configure(bg = "#696969")
window_button_4.configure(bg = "#696969")
window_label.configure(bg = "#505050")

def upload_file():
    #Set global variable to make it displayed
    global displayed_image
    f_types = [('All files', '*')]
    #f_types = [('PNG Files', '*.png')]
    
    #selected_filename is the actual pic (PNG)
    selected_filename = filedialog.askopenfilename(filetypes = f_types)
    
    #Load the image
    selected_image =Image.open(selected_filename)
    # resize image
    selected_image = selected_image.resize((300, 205), Image.Resampling.LANCZOS)
    #
    displayed_image = ImageTk.PhotoImage(selected_image)
    #Use button to display the image
    window_button_4 =tk.Button(window_frame, image=displayed_image) # using Button 
    window_button_4.grid(row=3,column=1)
    #Call numberplate_recognition and print the number plate
    window_label_1 = tk.Label(window_frame, text=(numberplate.numberplate_recognition(selected_filename)),width=30,font=window_font)  
    window_label_1.grid(row=4,column=1)
    print(numberplate.numberplate_recognition(selected_filename))

#Keep the window opens
window.mainloop() 
    
#def save_numberplate(numberplate_number):
    #to be continued

#save_numberplate(entry_numberplate)

#if save_numberplate succeed,print something
#else print something