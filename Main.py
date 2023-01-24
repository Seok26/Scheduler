from tkinter import *
from search import start_search
from info import start_info
from cost import start_cost

tk = Tk()
tk.title("Part Timer Scheduler") #제목
tk.geometry("640x400+100+100") #Window 크기 설정
tk.resizable(True, True) #Window 크기 조절 여부(상하, 좌우)

title_label = Label(tk, text = 'Part Timer Scheduler', relief = 'raised', bd = 2, width = 30, height = 5, font = 20)
title_label.pack(side='top')

#시간표 조회 Button
search_button = Button(tk, text = '시간표 조회', command = start_search, width = 30, height = 3, padx = 10, pady = 10)
search_button.place(x = 200, y = 100)

#아르바이트 정보 입력 Button
input_button = Button(tk, text = '아르바이트 정보 입력', command = start_info, width = 30, height = 3, padx = 10, pady = 10)
input_button.place(x = 200, y = 200)

#급여 조회 Button
cost_button = Button(tk, text = '급여 조회', command = start_cost, width = 30, height = 3, padx = 10, pady = 10)
cost_button.place(x = 200, y = 300)

tk.mainloop()



