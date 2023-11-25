import tkinter
from tkinter import*

root = Tk()
root.geometry('300x275')
root.configure(bg = '#17161b')

text_result = tkinter.Text(root, height=2, width=16,  font=('Arial', 24))
text_result.grid(columnspan=5)

btn_1 = tkinter.Button(root, text='7', width=5, font=('Arial', 14))
btn_1.grid(row=2, column=1)

btn_2 = tkinter.Button(root, text='4', width=5, font=('Arial', 14))
btn_2.grid(row=3, column=1)

btn_3 = tkinter.Button(root, text='1', width=5, font=('Arial', 14))
btn_3.grid(row=4, column=1)

btn_4 = tkinter.Button(root, text='6', width=5, font=('Arial', 14))
btn_4.grid(row=2, column=2)

btn_5 = tkinter.Button(root, text='5', width=5, font=('Arial', 14))
btn_5.grid(row=3, column=2)

btn_6 = tkinter.Button(root, text='2', width=5, font=('Arial', 14))
btn_6.grid(row=4, column=2)

btn_7 = tkinter.Button(root, text='9', width=5, font=('Arial', 14))
btn_7.grid(row=2, column=3)

btn_8 = tkinter.Button(root, text='6', width=5, font=('Arial', 14))
btn_8.grid(row=3, column=3)

btn_9 = tkinter.Button(root, text='3', width=5, font=('Arial', 14))
btn_9.grid(row=4, column=3)

btn_0 = tkinter.Button(root, text='0', width=5, font=('Arial', 14))
btn_0.grid(row=5, column=2)

btn_plus = tkinter.Button(root, text='+', width=5, font=('Arial', 14))
btn_plus.grid(row=2, column=4)

btn_kurang = tkinter.Button(root, text='-', width=5, font=('Arial', 14))
btn_kurang.grid(row=3, column=4)

btn_kali = tkinter.Button(root, text='*', width=5, font=('Arial', 14))
btn_kali.grid(row=4, column=4)

btn_kurung1 = tkinter.Button(root, text='(', width=5, font=('Arial', 14))
btn_kurung1.grid(row=5, column=1)

btn_kurung2 = tkinter.Button(root, text=')', width=5, font=('Arial', 14))
btn_kurung2.grid(row=5, column=3)

btn_samadengan = tkinter.Button(root, text='=', width=5, font=('Arial', 14), bg=('#f15837'))
btn_samadengan.grid(row=5, column=4)

root.mainloop()