#to call the library
from tkinter import *

class Student:
    def __init__(self , root):
        self.root = root
        self.root.geometry("2350x1000+1+1")
        self.root.title("مشروع ادارة طلاب")
        self.root.configure(background="#DFD0B8")
        self.root.resizable(True,True)
#to creat a title such as the name [ MOHAMED MAGDY OMARA]
        titel = Label(self.root ,
        text='[ MOHAMED MAGDY OMARA]',
        bg="#124076",
        font=('monospace',20,),
        fg="#FFEBB2"

                      )
        titel.pack()
       


















#to run the libarary create a variable with the name of the library in it then give this variable the run command
root = Tk()
ob = Student(root)
root.mainloop()