from tkinter import *

window = Tk()
label=Label(window, text='TEKST')


def hello():
    label['text']='inny'


btn = Button(window, text='Click',command=hello)
btn.pack()
label.pack()
window.mainloop()