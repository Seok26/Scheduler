from tkinter import *

def start_info():
    tk = Tk()
    tk.title("Part Timer Scheduler") #제목
    tk.geometry("1280x800+100+100") #Window 크기 설정
    tk.resizable(True, True) #Window 크기 조절 여부(상하, 좌우)

    frame1 = Frame(tk, relief = 'solid', bd = 2)
    frame1.pack(side = 'left', fill = 'both', expand=True)

    frame2 = Frame(tk, relief = "solid", bd = 2)
    frame2.pack(side="right", fill= "both", expand = True)


    title_label = Label(frame1, text = '아르바이트 정보 입력', relief = 'raised', bd = 2, width = 30, height = 5, font = 20)
    title_label.place(x = 0, y = 0)

    name_label = Label(frame1, text = '파트 정보 입력', relief = 'raised', bd = 2, width = 20, height = 4, font = 20)
    name_label.place(x = 220, y = 100)

    weekday_label = Label(frame1, text = '평일', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    weekday_label.place(x = 150, y = 275)

    weekend_label = Label(frame1, text = '주말', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    weekend_label.place(x = 380, y = 275)

    costset_button = Button(frame1, text = '급여 일괄 적용', overrelief= "solid", bg = 'white', width = 12, height = 2, font = 12)
    costset_button.place(x = 15, y = 285)

    announce_label = Label(frame1, text = '사용하지 않는 파트 칸은 비워두세요.', relief = 'groove', bd = 2, width = 40, height = 3, font = 15)
    announce_label.place(x = 140, y = 200)

    #파트 1 입력 칸
    #평일 파트 1
    part1_label = Label(frame1, text = '파트 1', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    part1_label.place(x = 20, y = 350)

    part1_entry_start = Entry(frame1, width = 16, justify = 'center')
    part1_entry_start.place(x= 150, y = 350)
    part1_entry_start.insert(0, "시작 시간") #시작시간 / 종료시간 안내는 파트 1 버튼에서만 수행

    part1_entry_end = Entry(frame1, width= 16, justify= 'center')
    part1_entry_end.place(x = 150, y = 385)
    part1_entry_end.insert(0, "종료 시간")

    #급여 입력 칸
    part1_text_cost = Text(frame1, width = 10, height = 2, font = 12)
    part1_text_cost.place(x = 278, y = 360)
    part1_text_cost.insert(1.0, "급여 입력")

    #주말 파트 1
    part1_entry_start_week = Entry(frame1, width = 16, justify= 'center')
    part1_entry_start_week.place(x = 378, y = 350)

    part1_entry_end_week = Entry(frame1, width = 16, justify=  'center')
    part1_entry_end_week.place(x = 378, y = 385)

    #급여 입력 칸
    part1_text_cost_week = Text(frame1, width = 10, height = 2, font = 12)
    part1_text_cost_week.place(x = 506, y = 360)

    #파트 2 입력 칸
    #평일 파트 2
    part2_label = Label(frame1, text = '파트 2', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    part2_label.place(x = 20, y = 450)

    part2_entry_start = Entry(frame1, width = 16, justify= 'center')
    part2_entry_start.place(x = 150, y = 450)

    part2_entry_end = Entry(frame1, width = 16, justify= 'center')
    part2_entry_end.place(x = 150, y = 485)

    #급여 입력 칸
    part2_text_cost = Text(frame1, width = 10, height = 2, font = 12)
    part2_text_cost.place(x = 278, y = 460)

    #주말 파트 2
    part2_entry_start_week = Entry(frame1, width = 16, justify= 'center')
    part2_entry_start_week.place(x = 378, y = 450)

    part2_entry_end_week = Entry(frame1, width = 16, justify= 'center')
    part2_entry_end_week.place(x = 378, y = 485)

    #급여 입력 칸
    part2_text_cost_week = Text(frame1, width = 10, height = 2, font = 12)
    part2_text_cost_week.place(x = 506, y = 460)

    #파트 3 입력 칸
    #평일 파트 3
    part3_label = Label(frame1, text = '파트 3', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    part3_label.place(x = 20, y = 550)

    part3_entry_start = Entry(frame1, width = 16, justify= 'center')
    part3_entry_start.place(x = 150, y = 550)

    part3_entry_end = Entry(frame1, width = 16, justify= 'center')
    part3_entry_end.place(x = 150, y = 585)

    #급여 입력 칸
    part3_text_cost = Text(frame1, width = 10, height = 2, font = 12)
    part3_text_cost.place(x = 278, y = 560)

    #주말 파트 3
    part3_entry_start_week = Entry(frame1, width = 16, justify= 'center')
    part3_entry_start_week.place(x = 378, y = 550)

    part3_entry_end_week = Entry(frame1, width = 16, justify= 'center')
    part3_entry_end_week.place(x = 378, y = 585)

    #급여 입력 칸
    part3_text_cost_week = Text(frame1, width = 10, height = 2, font = 12)
    part3_text_cost_week.place(x = 506, y = 560)

    #파트 4 입력 칸
    #평일 파트 4
    part3_label = Label(frame1, text = '파트 4', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    part3_label.place(x = 20, y = 650)

    part3_entry_start = Entry(frame1, width = 16, justify= 'center')
    part3_entry_start.place(x = 150, y = 650)

    part3_entry_end = Entry(frame1, width = 16, justify= 'center')
    part3_entry_end.place(x = 150, y = 685)

    #급여 입력 칸
    part4_text_cost = Text(frame1, width = 10, height = 2, font = 12)
    part4_text_cost.place(x = 278, y = 660)

    #주말 파트 4
    part3_entry_start_week = Entry(frame1, width = 16, justify= 'center')
    part3_entry_start_week.place(x = 378, y = 650)

    part3_entry_end_week = Entry(frame1, width = 16, justify= 'center')
    part3_entry_end_week.place(x = 378, y = 685)

    #급여 입력 칸
    part4_text_cost_week = Text(frame1, width = 10, height = 2, font = 12)
    part4_text_cost_week.place(x = 506, y = 660)

    """
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
    """



    tk.mainloop()