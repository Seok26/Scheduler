from tkinter import *
def start_cost():
    tk = Tk()
    tk.title("Part Timer Scheduler") #제목
    tk.geometry("1280x800+100+100") #Window 크기 설정
    tk.resizable(True, True) #Window 크기 조절 여부(상하, 좌우)

    title_label = Label(tk, text = '급여 조회', relief = 'raised', bd = 2, width = 30, height = 5, font = 20)
    title_label.pack(side='top')

    tk.mainloop()