# пример создания графического интерфейса используя встроенную библиотеку tkinter

from tkinter import *
from tkinter.ttk import Combobox, Radiobutton


def clicked():
    res = f'Hello {txt.get()}!'
    lbl.configure(text=res)


def clicked_combo():
    res = f'Hello {combo.get()}!'
    lbl.configure(text=res)


def clicked_radio():
    res = f'Hello {selected.get()}!'
    lbl.configure(text=res)


# Рисуем окно
window = Tk()
window.title('Welcome program')
window.geometry('400x200')

# выводим текст-заголовок
lbl = Label(window, text='Welcome to: ', font=('Calibry', 12))
lbl.grid(column=0, row=0)

# выводим поле для ввода
txt = Entry(window, width=23)
txt.grid(column=0, row=1)

# Рисуем кнопку
btn = Button(window, text='Press me', width=10, command = clicked, bg='green', fg='black')
btn.grid(column=1, row=1)

# рисуем комбобокс
combo = Combobox(window)
combo['values'] = ('Me', 'You', 'Moscow')
combo.current(0)
combo.grid(column=0, row=2)

# Рисуем кнопку
btn2 = Button(window, text='Choose me', width=10, command = clicked_combo, bg='red', fg='black')
btn2.grid(column=1, row=2)

# рисуем radiobuttons
selected = IntVar()
rad1 = Radiobutton(window, text='Me', value=1, variable=selected)
rad1.grid(column=0, row=3)
rad2 = Radiobutton(window, text='You', value=2, variable=selected)
rad2.grid(column=1, row=3)
rad3 = Radiobutton(window, text='Moscow', value=3, variable=selected)
rad3.grid(column=2, row=3)

# Рисуем кнопку
btn2 = Button(window, text='Select me', width=10, command = clicked_radio, bg='blue', fg='black')
btn2.grid(column=3, row=3)

# выводим текст
lbl = Label(window, text='Hello world!', font=('Calibry', 25))
lbl.grid(column=0, row=4)

# отображаем окно
window.mainloop()
