from tkinter import *


def save_exit():
    exit()

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

    #직원 정보 입력
    name_label2 = Label(frame2, text = '직원 정보 입력', relief = 'raised', bd = 2, width = 20, height = 4, font = 20)
    name_label2.place(x = 220, y = 100)

    announce_label2 = Label(frame2, text = '근무 가능한 파트에 체크하세요', relief = 'groove', bd = 2, width = 40, height = 3, font = 15)
    announce_label2.place(x = 140, y = 200)

    """
    =======================================================
    직원 정보 입력 UI 시작
    =======================================================
    """
    #1번 직원 입력 값
    worker_text = Text(frame2, width = 13, height = 1, font = 12)
    worker_text.place(x = 50, y = 270)
    worker_text.insert(1.0, '이름 입력')

    part1_check_1 = IntVar()
    part1_checkbox_1 = Checkbutton(frame2, text = '파트 1', variable=part1_check_1)
    part1_checkbox_1.place(x = 38, y = 295)

    part2_check_1 = IntVar()
    part2_checkbox_1 = Checkbutton(frame2, text = '파트 2', variable=part2_check_1)
    part2_checkbox_1.place(x = 105, y = 295)

    part3_check_1 = IntVar()
    part3_checkbox_1 = Checkbutton(frame2, text = '파트 3', variable=part3_check_1)
    part3_checkbox_1.place(x = 38, y = 325)

    part4_check_1 = IntVar()
    part4_checkbox_1 = Checkbutton(frame2, text = '파트 4', variable=part4_check_1)
    part4_checkbox_1.place(x = 105, y = 325)

    #관리자 여부 판단
    check_super_1 = IntVar()
    checkbox_super_1 = Checkbutton(frame2, text = '관리자', variable = check_super_1)
    checkbox_super_1.place(x = 70, y = 355)

    #2번 직원 입력 값
    worker2_text = Text(frame2, width = 13, height = 1, font = 12)
    worker2_text.place(x = 50, y = 385)

    part1_check_2 = IntVar()
    part1_checkbox_2 = Checkbutton(frame2, text = '파트 1', variable=part1_check_2)
    part1_checkbox_2.place(x = 38, y = 410)

    part2_check_2 = IntVar()
    part2_checkbox_2 = Checkbutton(frame2, text = '파트 2', variable=part2_check_2)
    part2_checkbox_2.place(x = 105, y = 410)

    part3_check_2 = IntVar()
    part3_checkbox_2 = Checkbutton(frame2, text = '파트 3', variable=part3_check_2)
    part3_checkbox_2.place(x = 38, y = 440)

    part4_check_2 = IntVar()
    part4_checkbox_2 = Checkbutton(frame2, text = '파트 4', variable=part4_check_2)
    part4_checkbox_2.place(x = 105, y = 440)

    #관리자 여부 판단
    check_super_2 = IntVar()
    checkbox_super_2 = Checkbutton(frame2, text = '관리자', variable = check_super_2)
    checkbox_super_2.place(x = 70, y = 470)

    #3번 직원 입력 값
    worker3_text = Text(frame2, width = 13, height = 1, font = 12)
    worker3_text.place(x = 50, y = 500)

    part1_check_3 = IntVar()
    part1_checkbox_3 = Checkbutton(frame2, text = '파트 1', variable=part1_check_3)
    part1_checkbox_3.place(x = 38, y = 525)

    part2_check_3 = IntVar()
    part2_checkbox_3 = Checkbutton(frame2, text = '파트 2', variable=part2_check_3)
    part2_checkbox_3.place(x = 105, y = 525)

    part3_check_3 = IntVar()
    part3_checkbox_3 = Checkbutton(frame2, text = '파트 3', variable=part3_check_3)
    part3_checkbox_3.place(x = 38, y = 555)

    part4_check_3 = IntVar()
    part4_checkbox_3 = Checkbutton(frame2, text = '파트 4', variable=part4_check_3)
    part4_checkbox_3.place(x = 105, y = 555)

    #관리자 여부 판단
    check_super_3 = IntVar()
    checkbox_super_3 = Checkbutton(frame2, text = '관리자', variable = check_super_3)
    checkbox_super_3.place(x = 70, y = 585)

    #4번 직원 입력 값
    worker4_text = Text(frame2, width = 13, height = 1, font = 12)
    worker4_text.place(x = 50, y = 615)

    part1_check_4 = IntVar()
    part1_checkbox_4 = Checkbutton(frame2, text = '파트 1', variable=part1_check_4)
    part1_checkbox_4.place(x = 38, y = 640)

    part2_check_4 = IntVar()
    part2_checkbox_4 = Checkbutton(frame2, text = '파트 2', variable=part2_check_4)
    part2_checkbox_4.place(x = 105, y = 640)

    part3_check_4 = IntVar()
    part3_checkbox_4 = Checkbutton(frame2, text = '파트 3', variable=part3_check_4)
    part3_checkbox_4.place(x = 38, y = 670)

    part4_check_4 = IntVar()
    part4_checkbox_4 = Checkbutton(frame2, text = '파트 4', variable=part4_check_4)
    part4_checkbox_4.place(x = 105, y = 670)

    #관리자 여부 판단
    check_super_4 = IntVar()
    checkbox_super_4 = Checkbutton(frame2, text = '관리자', variable = check_super_4)
    checkbox_super_4.place(x = 70, y = 700)

    #5번 직원 입력 값
    worker5_text = Text(frame2, width = 13, height = 1, font = 12)
    worker5_text.place(x = 200, y = 270)


    part1_check_5 = IntVar()
    part1_checkbox_5 = Checkbutton(frame2, text = '파트 1', variable=part1_check_5)
    part1_checkbox_5.place(x = 188, y = 295)

    part2_check_5 = IntVar()
    part2_checkbox_5 = Checkbutton(frame2, text = '파트 2', variable=part2_check_5)
    part2_checkbox_5.place(x = 255, y = 295)

    part3_check_5 = IntVar()
    part3_checkbox_5 = Checkbutton(frame2, text = '파트 3', variable=part3_check_5)
    part3_checkbox_5.place(x = 188, y = 325)

    part4_check_5 = IntVar()
    part4_checkbox_5 = Checkbutton(frame2, text = '파트 4', variable=part4_check_5)
    part4_checkbox_5.place(x = 255, y = 325)

    check_super_5 = IntVar()
    checkbox_super_5 = Checkbutton(frame2, text = '관리자', variable = check_super_5)
    checkbox_super_5.place(x = 220, y = 355)

    #6번 직원 입력 값
    worker6_text = Text(frame2, width = 13, height = 1, font = 12)
    worker6_text.place(x = 200, y = 385)

    part1_check_6 = IntVar()
    part1_checkbox_6 = Checkbutton(frame2, text = '파트 1', variable=part1_check_6)
    part1_checkbox_6.place(x = 188, y = 410)

    part2_check_6 = IntVar()
    part2_checkbox_6 = Checkbutton(frame2, text = '파트 2', variable=part2_check_6)
    part2_checkbox_6.place(x = 255, y = 410)

    part3_check_6 = IntVar()
    part3_checkbox_6 = Checkbutton(frame2, text = '파트 3', variable=part3_check_6)
    part3_checkbox_6.place(x = 188, y = 440)

    part4_check_6 = IntVar()
    part4_checkbox_6 = Checkbutton(frame2, text = '파트 4', variable=part4_check_6)
    part4_checkbox_6.place(x = 255, y = 440)

    #7번 직원 입력 값
    worker7_text = Text(frame2, width = 13, height = 1, font = 12)
    worker7_text.place(x = 200, y = 500)

    part1_check_7 = IntVar()
    part1_checkbox_7 = Checkbutton(frame2, text = '파트 1', variable=part1_check_7)
    part1_checkbox_7.place(x = 188, y = 525)

    part2_check_7 = IntVar()
    part2_checkbox_7 = Checkbutton(frame2, text = '파트 2', variable=part2_check_7)
    part2_checkbox_7.place(x = 255, y = 525)

    part3_check_7 = IntVar()
    part3_checkbox_7 = Checkbutton(frame2, text = '파트 3', variable=part3_check_7)
    part3_checkbox_7.place(x = 188, y = 555)

    part4_check_7 = IntVar()
    part4_checkbox_7 = Checkbutton(frame2, text = '파트 4', variable=part4_check_7)
    part4_checkbox_7.place(x = 255, y = 555)

    check_super_7 = IntVar()
    checkbox_super_7 = Checkbutton(frame2, text = '관리자', variable = check_super_7)
    checkbox_super_7.place(x = 220, y = 585)

    #8번 직원 입력 값
    worker8_text = Text(frame2, width = 13, height = 1, font = 12)
    worker8_text.place(x = 200, y = 615)

    part1_check_8 = IntVar()
    part1_checkbox_8 = Checkbutton(frame2, text = '파트 1', variable=part1_check_8)
    part1_checkbox_8.place(x = 188, y = 640)

    part2_check_8 = IntVar()
    part2_checkbox_8 = Checkbutton(frame2, text = '파트 2', variable=part2_check_8)
    part2_checkbox_8.place(x = 255, y = 640)

    part3_check_8 = IntVar()
    part3_checkbox_8 = Checkbutton(frame2, text = '파트 3', variable=part3_check_8)
    part3_checkbox_8.place(x = 188, y = 670)

    part4_check_8 = IntVar()
    part4_checkbox_8 = Checkbutton(frame2, text = '파트 4', variable=part4_check_8)
    part4_checkbox_8.place(x = 255, y = 670)

    check_super_8 = IntVar()
    checkbox_super_8 = Checkbutton(frame2, text = '관리자', variable = check_super_8)
    checkbox_super_8.place(x = 220, y = 700)

    #9번 직원 입력 값
    worker9_text = Text(frame2, width = 13, height = 1, font = 12)
    worker9_text.place(x = 350, y = 270)

    part1_check_9 = IntVar()
    part1_checkbox_9 = Checkbutton(frame2, text = '파트 1', variable=part1_check_9)
    part1_checkbox_9.place(x = 328, y = 295)

    part2_check_9 = IntVar()
    part2_checkbox_9 = Checkbutton(frame2, text = '파트 2', variable=part2_check_9)
    part2_checkbox_9.place(x = 405, y = 295)

    part3_check_9 = IntVar()
    part3_checkbox_9 = Checkbutton(frame2, text = '파트 3', variable=part3_check_9)
    part3_checkbox_9.place(x = 328, y = 325)

    part4_check_9 = IntVar()
    part4_checkbox_9 = Checkbutton(frame2, text = '파트 4', variable=part4_check_9)
    part4_checkbox_9.place(x = 405, y = 325)

    check_super_9 = IntVar()
    checkbox_super_9 = Checkbutton(frame2, text = '관리자', variable = check_super_9)
    checkbox_super_9.place(x = 370, y = 355)

    #10번 직원 입력 값
    worker10_text = Text(frame2, width = 13, height = 1, font = 12)
    worker10_text.place(x = 350, y = 385)

    part1_check_10 = IntVar()
    part1_checkbox_10 = Checkbutton(frame2, text = '파트 1', variable=part1_check_10)
    part1_checkbox_10.place(x = 328, y = 410)

    part2_check_10 = IntVar()
    part2_checkbox_10 = Checkbutton(frame2, text = '파트 2', variable=part2_check_10)
    part2_checkbox_10.place(x = 405, y = 410)

    part3_check_10 = IntVar()
    part3_checkbox_10 = Checkbutton(frame2, text = '파트 3', variable=part3_check_10)
    part3_checkbox_10.place(x = 328, y = 440)

    part4_check_10 = IntVar()
    part4_checkbox_10 = Checkbutton(frame2, text = '파트 4', variable=part4_check_10)
    part4_checkbox_10.place(x = 405, y = 440)

    check_super_10 = IntVar()
    checkbox_super_10 = Checkbutton(frame2, text = '관리자', variable = check_super_10)
    checkbox_super_10.place(x = 370, y = 470)

    #11번 직원 입력 값
    worker11_text = Text(frame2, width = 13, height = 1, font = 12)
    worker11_text.place(x = 350, y = 500)

    part1_check_11 = IntVar()
    part1_checkbox_11 = Checkbutton(frame2, text = '파트 1', variable=part1_check_11)
    part1_checkbox_11.place(x = 328, y = 525)

    part2_check_11 = IntVar()
    part2_checkbox_11 = Checkbutton(frame2, text = '파트 2', variable=part2_check_11)
    part2_checkbox_11.place(x = 405, y = 525)

    part3_check_11 = IntVar()
    part3_checkbox_11 = Checkbutton(frame2, text = '파트 3', variable=part3_check_11)
    part3_checkbox_11.place(x = 328, y = 555)

    part4_check_11 = IntVar()
    part4_checkbox_11 = Checkbutton(frame2, text = '파트 4', variable=part4_check_11)
    part4_checkbox_11.place(x = 405, y = 555)

    check_super_11 = IntVar()
    checkbox_super_11 = Checkbutton(frame2, text = '관리자', variable = check_super_11)
    checkbox_super_11.place(x = 370, y = 585)

    #12번 직원 입력 값
    worker12_text = Text(frame2, width = 13, height = 1, font = 12)
    worker12_text.place(x = 350, y = 615)

    part1_check_12 = IntVar()
    part1_checkbox_12 = Checkbutton(frame2, text = '파트 1', variable=part1_check_12)
    part1_checkbox_12.place(x = 328, y = 640)

    part2_check_12 = IntVar()
    part2_checkbox_12 = Checkbutton(frame2, text = '파트 2', variable=part2_check_12)
    part2_checkbox_12.place(x = 405, y = 640)

    part3_check_12 = IntVar()
    part3_checkbox_12 = Checkbutton(frame2, text = '파트 3', variable=part3_check_12)
    part3_checkbox_12.place(x = 328, y = 670)

    part4_check_12 = IntVar()
    part4_checkbox_12 = Checkbutton(frame2, text = '파트 4', variable=part4_check_12)
    part4_checkbox_12.place(x = 405, y = 670)

    check_super_12 = IntVar()
    checkbox_super_12 = Checkbutton(frame2, text = '관리자', variable = check_super_12)
    checkbox_super_12.place(x = 370, y = 700)

    #8번 직원 입력 값
    worker8_text = Text(frame2, width = 13, height = 1, font = 12)
    worker8_text.place(x = 200, y = 615)

    part1_check_8 = IntVar()
    part1_checkbox_8 = Checkbutton(frame2, text = '파트 1', variable=part1_check_8)
    part1_checkbox_8.place(x = 188, y = 640)

    part2_check_8 = IntVar()
    part2_checkbox_8 = Checkbutton(frame2, text = '파트 2', variable=part2_check_8)
    part2_checkbox_8.place(x = 255, y = 640)

    part3_check_8 = IntVar()
    part3_checkbox_8 = Checkbutton(frame2, text = '파트 3', variable=part3_check_8)
    part3_checkbox_8.place(x = 188, y = 670)

    part4_check_8 = IntVar()
    part4_checkbox_8 = Checkbutton(frame2, text = '파트 4', variable=part4_check_8)
    part4_checkbox_8.place(x = 255, y = 670)

    check_super_8 = IntVar()
    checkbox_super_8 = Checkbutton(frame2, text = '관리자', variable = check_super_8)
    checkbox_super_8.place(x = 220, y = 700)

    #13번 직원 입력 값
    worker13_text = Text(frame2, width = 13, height = 1, font = 12)
    worker13_text.place(x = 500, y = 270)

    part1_check_13 = IntVar()
    part1_checkbox_13 = Checkbutton(frame2, text = '파트 1', variable=part1_check_13)
    part1_checkbox_13.place(x = 478, y = 295)

    part2_check_13 = IntVar()
    part2_checkbox_13 = Checkbutton(frame2, text = '파트 2', variable=part2_check_13)
    part2_checkbox_13.place(x = 555, y = 295)

    part3_check_13 = IntVar()
    part3_checkbox_13 = Checkbutton(frame2, text = '파트 3', variable=part3_check_13)
    part3_checkbox_13.place(x = 478, y = 325)

    part4_check_13 = IntVar()
    part4_checkbox_13 = Checkbutton(frame2, text = '파트 4', variable=part4_check_13)
    part4_checkbox_13.place(x = 555, y = 325)

    check_super_13 = IntVar()
    checkbox_super_13 = Checkbutton(frame2, text = '관리자', variable = check_super_13)
    checkbox_super_13.place(x = 520, y = 355)

    #14번 직원 입력 값
    worker14_text = Text(frame2, width = 13, height = 1, font = 12)
    worker14_text.place(x = 500, y = 385)

    part1_check_14 = IntVar()
    part1_checkbox_14 = Checkbutton(frame2, text = '파트 1', variable=part1_check_14)
    part1_checkbox_14.place(x = 478, y = 410)

    part2_check_14 = IntVar()
    part2_checkbox_14 = Checkbutton(frame2, text = '파트 2', variable=part2_check_14)
    part2_checkbox_14.place(x = 555, y = 410)

    part3_check_14 = IntVar()
    part3_checkbox_14 = Checkbutton(frame2, text = '파트 3', variable=part3_check_14)
    part3_checkbox_14.place(x = 478, y = 440)

    part4_check_14 = IntVar()
    part4_checkbox_14 = Checkbutton(frame2, text = '파트 4', variable=part4_check_14)
    part4_checkbox_14.place(x = 555, y = 440)

    check_super_14 = IntVar()
    checkbox_super_14 = Checkbutton(frame2, text = '관리자', variable = check_super_14)
    checkbox_super_14.place(x = 520, y = 470)

    #15번 직원 입력 값
    worker15_text = Text(frame2, width = 13, height = 1, font = 12)
    worker15_text.place(x = 500, y = 500)

    part1_check_15 = IntVar()
    part1_checkbox_15 = Checkbutton(frame2, text = '파트 1', variable=part1_check_15)
    part1_checkbox_15.place(x = 478, y = 525)

    part2_check_15 = IntVar()
    part2_checkbox_15 = Checkbutton(frame2, text = '파트 2', variable=part2_check_15)
    part2_checkbox_15.place(x = 555, y = 525)

    part3_check_15 = IntVar()
    part3_checkbox_15 = Checkbutton(frame2, text = '파트 3', variable=part3_check_15)
    part3_checkbox_15.place(x = 478, y = 555)

    part4_check_15 = IntVar()
    part4_checkbox_15 = Checkbutton(frame2, text = '파트 4', variable=part4_check_15)
    part4_checkbox_15.place(x = 555, y = 555)

    check_super_15 = IntVar()
    checkbox_super_15 = Checkbutton(frame2, text = '관리자', variable = check_super_15)
    checkbox_super_15.place(x = 520, y = 585)

    #16번 직원 입력 값
    worker16_text = Text(frame2, width = 13, height = 1, font = 12)
    worker16_text.place(x = 500, y = 615)

    part1_check_16 = IntVar()
    part1_checkbox_16 = Checkbutton(frame2, text = '파트 1', variable=part1_check_16)
    part1_checkbox_16.place(x = 478, y = 640)

    part2_check_16 = IntVar()
    part2_checkbox_16 = Checkbutton(frame2, text = '파트 2', variable=part2_check_16)
    part2_checkbox_16.place(x = 555, y = 640)

    part3_check_16 = IntVar()
    part3_checkbox_16 = Checkbutton(frame2, text = '파트 3', variable=part3_check_16)
    part3_checkbox_16.place(x = 478, y = 670)

    part4_check_16 = IntVar()
    part4_checkbox_16 = Checkbutton(frame2, text = '파트 4', variable=part4_check_16)
    part4_checkbox_16.place(x = 555, y = 670)

    check_super_16 = IntVar()
    checkbox_super_16 = Checkbutton(frame2, text = '관리자', variable = check_super_16)
    checkbox_super_16.place(x = 520, y = 700)

    #저장 후 종료
    exit_button = Button(frame2, text = '저장 후 종료', command = save_exit, width = 10, bg = 'white', height = 2, padx = 10, pady = 10)
    exit_button.place(x = 500, y = 30)

    tk.mainloop()

