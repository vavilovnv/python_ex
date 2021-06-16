# пример создания графического интерфейса используя встроенную библиотеку tkinter

from tkinter import *

window = Tk()
window.title('Window title')
lbl = Label(window, text='Hello world!', font=('Calibry', 25))
lbl.grid(column=0, row=0)
window.mainloop()  # без этого бесконечного цикла окно не отобразится
