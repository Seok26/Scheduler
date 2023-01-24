from tkinter import *

def start_info():
    tk = Tk()
    tk.title("Part Timer Scheduler") #제목
    tk.geometry("1280x800+100+100") #Window 크기 설정
    tk.resizable(True, True) #Window 크기 조절 여부(상하, 좌우)

    title_label = Label(tk, text = '아르바이트 정보 입력', relief = 'raised', bd = 2, width = 30, height = 5, font = 20)
    title_label.place(x = 0, y = 0)

    #요일 Label
    mon_label = Label(tk, text = '월', relief = 'raised', bd = 2, width = 12, height = 3, font = 5)
    mon_label.place(x = 300, y = 80)

    tue_label = Label(tk, text = '화', relief = 'raised', bd = 2, width = 12, height = 3, font = 5)
    tue_label.place(x = 420, y = 80)

    wed_label = Label(tk, text = '수', relief = 'raised', bd = 2, width = 12, height = 3, font = 5)
    wed_label.place(x = 540, y = 80)

    thu_label = Label(tk, text = '목', relief = 'raised', bd = 2, width = 12, height = 3, font = 5)
    thu_label.place(x = 660, y = 80)

    fri_label = Label(tk, text = '금', relief = 'raised', bd = 2, width = 12, height = 3, font = 5)
    fri_label.place(x = 780, y = 80)

    sat_label = Label(tk, text = '토', relief = 'raised', bd = 2, width = 12, height = 3, font = 5)
    sat_label.place(x = 900, y = 80)

    sun_label = Label(tk, text = '일', relief = 'raised', bd = 2, width = 12, height = 3, font = 5)
    sun_label.place(x = 1020, y = 80)


    #파트 정보 입력
    part1_entry = Entry(tk, width = 20, bd = 2, font = 10)
    part1_entry.place(x = 100, y = 150)

    tk.mainloop()