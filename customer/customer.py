import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *

root = Tk()
root.geometry ('560x650')
global reading1 
global reading2
global reading3
global reading4
global reading5
tk.Label (root, text=" customer information", fg="blue", font=(None ,"25")).place(x=100, y=5)
tk.Label (root, text=" customer name").place(x=20 ,y=40)
tk.Label (root, text=" customer card number").place(x=20 ,y=80)
tk.Label (root, text=" customer ID number").place(x=20 ,y=120)
tk.Label (root, text=" customer location").place(x=20 ,y=160)
tk.Label (root, text=" customer bill").place(x=20 ,y=200)
reading1= Entry(root)
reading1.place(x=160, y=40)
reading2= Entry(root)
reading2.place(x=160, y=80)
reading3= Entry(root)
reading3.place(x=160, y=120)
reading4= Entry(root)
reading4.place(x=160, y=160)
reading5= Entry(root)
reading5.place(x=160, y=200)
Button(root, text="add", command="Add", height=1, width=8).place(x=200, y=240)
Button(root, text="update", command="update", height=1, width=8).place(x=200, y=280)
Button(root, text="delete", command="delete", height=1, width=8).place(x=200, y=320)

cols =('customer name', 'customer card number', 'customer ID number', 'customer location','customer bill')
Listbox=ttk.Treeview(root, columns=cols,show='headings')
for col in cols:
    Listbox.heading(col, text=col)
    Listbox.grid(row=1, column=0, columnspan=2)
    Listbox.place(x=10, y=380)

root.mainloop() 
