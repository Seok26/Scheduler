from tkinter import *
from search import start_search
from info import start_info
from cost import start_cost
from threading import Thread


# 다른 페이지로 이동
def enter_info():
    new_thread = Thread(target = start_info)
    new_thread.start()

def enter_search():
    new_thread = Thread(target = start_search)
    new_thread.start()

def enter_cost():
    new_thread = Thread(target = start_cost)
    new_thread.start()


#####################################################
####################UI 작성 시작######################
#####################################################

tk = Tk()
tk.title("Part Timer Scheduler") #제목
tk.geometry("640x400+100+100") #Window 크기 설정
tk.resizable(True, True) #Window 크기 조절 여부(상하, 좌우)

title_label = Label(tk, text = 'Part Timer Scheduler', relief = 'raised', bd = 2, width = 30, height = 5, font = 20)
title_label.pack(side='top')

#시간표 조회 Button
search_button = Button(tk, text = '시간표 조회', command = enter_search, width = 30, height = 3, padx = 10, pady = 10)
search_button.place(x = 200, y = 100)

#아르바이트 정보 입력 Button
input_button = Button(tk, text = '아르바이트 정보 입력', command = enter_info, width = 30, height = 3, padx = 10, pady = 10)
input_button.place(x = 200, y = 200)

#급여 조회 Button
cost_button = Button(tk, text = '급여 조회', command = enter_cost, width = 30, height = 3, padx = 10, pady = 10)
cost_button.place(x = 200, y = 300)

tk.mainloop()

#####################################################
####################UI 작성 종료######################
#####################################################







