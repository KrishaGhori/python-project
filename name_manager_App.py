# #import section
import tkinter 
from tkinter import messagebox
from add import add_name
from update import update_name
from delete import del_name
from display import displayy


def update_GUI():
    entry2_l.grid(row=1,column=0,pady=1)
    entry2.grid(row=1,column=1,pady=2)

    entry3_l.grid(row=2,column=0,pady=1)
    entry3.grid(row=2,column=1,pady=2)
    
    tkinter.Button(root, text="Update Now", command=lambda: update_name(entry2,entry3)).grid(row=4,column=1,pady=1)

#GUI 
root = tkinter.Tk()
root.title("Name Manager App")

tkinter.Label(root,text="Name :").grid(row=0,column=0,pady=1)
entry = tkinter.Entry(root)
entry.grid(row=0,column=1,pady=2)

btn_add = tkinter.Button(root, text="Add", command=lambda: add_name(entry)).grid(row=0,column=2,pady=1)

btn_update = tkinter.Button(root, text="Update", command=lambda: update_GUI()).grid(row=1,column=2,pady=1)

btn_del = tkinter.Button(root, text="Delete", command=lambda:del_name(entry)).grid(row=2,column=2,pady=1)

btn_display = tkinter.Button(root, text="display", command=displayy).grid(row=3,column=2,pady=1)


entry2_l = tkinter.Label(root,text="Old Name :")
entry2 = tkinter.Entry(root)

entry3_l = tkinter.Label(root,text=" New Name :")
entry3 = tkinter.Entry(root)

root.mainloop()