import tkinter 
from tkinter import messagebox

def update_name(entry2,entry3):
    old = entry2.get().strip()
    new = entry3.get().strip()
    if not old and not new:
        messagebox.showerror("Both fields are required!")
    
    with open('D:/Python/projects/dataa.txt' , 'r') as f:
        lines = f.readlines()

    with open('D:/Python/projects/dataa.txt' , 'w') as f:
        found = False
        for line in lines:
            if line.strip() == old:
                f.write(new + "\n")
                found = True
            else:
                f.write(line)
        if found:
            messagebox.showinfo("Result","updated successfully!")
        else:
            messagebox.showwarning("Warning","Old name not found in a file.")
        entry2.delete(0, tkinter.END)
        entry3.delete(0, tkinter.END)
