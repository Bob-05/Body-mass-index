import tkinter as tk
from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/m**2
    bmi = round(bmi, 1)
    if bmi < 18.5:
        messagebox.showinfo('Вывод', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('Вывод', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('Вывод', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('Вывод', f'ИМТ = {bmi} соответствует ожирению')


window = Tk()
window.title("Калькулятор ИМТ")

window.geometry('600x400')
frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)

height_lb = Label(frame, text="Введите свой рост (в см) ", )
height_lb.grid(row=3, column =1)

weigth_lb= Label(frame, text="Введите свой вес (в кг) ", )
weigth_lb.grid(row=4, column = 1)

height_tf = Entry(frame,)
height_tf.grid(row=3, column=2)

weight_tf = Entry(frame,)
weight_tf.grid(row=4, column=2)

button_cl = Button(frame, text="Расчитать", command=calculate_bmi)
button_cl.grid(row=5, column = 2)

window.mainloop()