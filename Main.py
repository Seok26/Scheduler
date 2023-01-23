from tkinter import *
tk = Tk()
tk.title("길이 변환기")

def Ft2Cm():
    ft2cm = entry1.get()
    entry2.delete(0, "end")
    entry2.insert(0, round(float(ft2cm) * 30.48, 4))

def Cm2Ft():
    cm2ft = entry2.get()
    entry1.delete(0, "end")
    entry1.insert(0, round(float(cm2ft) / 30.48, 4))

label1 = Label(tk, text = '피트(ft)').grid(row = 0, column = 0)
label2 = Label(tk, text = '센티미터(cm)').grid(row = 1, column = 0)

def reset():
    entry1.delete(0, "end")
    entry2.delete(0, "end")

entry1= Entry(tk)
entry2 = Entry(tk)
entry3 = Entry(tk)

entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)

btn1 = Button(tk, text = 'ft -> cm', bg = 'black', fg = 'white', command = Ft2Cm).grid(row = 2, column = 0)
btn2 = Button(tk, text = 'cm -> ft', bg = 'black', fg = 'white', command = Cm2Ft).grid(row = 2, column = 1)
btn3 = Button(tk, text = 'Reset', bg = 'red', command = reset).grid(row = 3)

tk.mainloop()


