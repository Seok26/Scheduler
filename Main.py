from tkinter import *
tk = Tk()
tk.title("Part Timer Scheduler") #제목
tk.geometry("640x400+100+100") #Window 크기 설정
tk.resizable(True, True) #Window 크기 조절 여부(상하, 좌우)

title_label = Label(tk, text = 'Part Timer Scheduler', relief = 'raised', bd = 2, width = 30, height = 5, font = 20)
title_label.pack(side='top')

#시간표 조회 Button
search_button = Button(tk, text = '시간표 조회', width = 30, height = 3, padx = 10, pady = 10)
search_button.place(x = 200, y = 100)

#아르바이트 정보 입력 Button
input_button = Button(tk, text = '아르바이트 정보 입력', width = 30, height = 3, padx = 10, pady = 10)
input_button.place(x = 200, y = 200)

#급여 조회 Button
cost_button = Button(tk, text = '급여 조회', width = 30, height = 3, padx = 10, pady = 10)
cost_button.place(x = 200, y = 300)

def click_search_button():



def click_input_button():


def click_cost_button():

"""
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
"""
tk.mainloop()

