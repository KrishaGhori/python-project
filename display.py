import tkinter 
from tkinter import messagebox


def displayy():
        with open('D:/Python/projects/dataa.txt' , 'r') as f:
          x = f.read()
          messagebox.showinfo('Result',x if x else "No name is saved in file.")