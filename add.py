#import section
import tkinter 
from tkinter import messagebox

#functionality
def add_name(entry):
    name = entry.get()
    messagebox.showinfo("Result" , f"'{name}' added successfully!")
    with open('D:/Python/projects/dataa.txt' , 'a') as f:
        f.write(name +  "\n")
    entry.delete(0,tkinter.END)