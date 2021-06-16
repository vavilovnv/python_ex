# пример создания графического интерфейса используя встроенную библиотеку tkinter

from tkinter import *

def clicked():
    lbl.configure(text='Great!')


window = Tk()
window.title('Window title')
window.geometry('400x200')
lbl = Label(window, text='Hello world!', font=('Calibry', 25))
lbl.grid(column=0, row=0)
btn = Button(window, text='Press me', command = clicked, bg='gray', fg='black')
btn.grid(column=1, row=0)
window.mainloop()  # без этого бесконечного цикла окно не отобразится
