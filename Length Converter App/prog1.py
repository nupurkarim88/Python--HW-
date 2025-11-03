from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("300x300")
Label(root, text="Meter to Centimeter Converter").pack()
def convert():
    cm = float(e.get()) * 100
    messagebox.showinfo("Result", f"{cm} cm")

Label(root, text="Enter meters:")
e = Entry(root)
e.pack()
Button(root, text="Convert", command=convert).pack()
root.mainloop()