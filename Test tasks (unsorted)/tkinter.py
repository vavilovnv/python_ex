# пример создания графического интерфейса используя встроенную библиотеку tkinter

from tkinter import *


def clicked():
    res = f'Hello {txt.get()}!'
    lbl.configure(text=res)


window = Tk()
window.title('Welcome program')
window.geometry('400x200')
lbl = Label(window, text='Welcome to: ', font=('Calibry', 12))
lbl.grid(column=0, row=0)
txt = Entry(window, width=25)
txt.grid(column=1, row=0)
btn = Button(window, text='Press me', command = clicked, bg='green', fg='black')
btn.grid(column=2, row=0)
lbl = Label(window, text='Hello world!', font=('Calibry', 25))
lbl.grid(column=0, row=1)
window.mainloop()  # без этого окно не отобразится
