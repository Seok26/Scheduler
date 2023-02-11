from tkinter import *
import pickle

global worker1_name

#저장 후 종료
def save_exit():
    exit()

def get_result():
    global worker1_name
    stat_file = open("stat", "rb")
    stat = pickle.load(stat_file)
    stat_file.close()

    stat_super_file = open("stat_super", "rb")
    stat_super = pickle.load(stat_super_file)
    stat_super_file.close()

    stat_str = ""
    for name, count in stat_super.items():
        temp = "이름 : " + name + "(SV)   |||||||| 근무 횟수 : " + str(count) + " 회"
        stat_str += temp
        stat_str += '\n'

    for name, count in stat.items():
        temp = "이름 : " + name + " |||||||| 근무 횟수 : " + str(count) + " 회"
        stat_str += temp
        stat_str += '\n'



    worker1_name.insert("1.0", stat_str)


#프로그램 시작
def start_cost():
    global worker1_name
    #####################################################
    ####################UI 작성 시작######################
    #####################################################
    tk = Tk()
    tk.title("Part Timer Scheduler") #제목
    tk.geometry("1280x900+100+100") #Window 크기 설정
    tk.resizable(True, True) #Window 크기 조절 여부(상하, 좌우)


    #통계 조회 버튼
    title_label = Label(tk, text = '통계 조회', relief = 'raised', bd = 2, width = 30, height = 5, font = 20)
    title_label.pack(side='top')

    #저장 후 종료
    exit_button = Button(tk, text = '뒤로 가기', command = save_exit, width = 13, bg = 'white', height = 2, padx = 10, pady = 10)
    exit_button.place(x = 1100, y = 35)

    #통계 조회
    stat_button = Button(tk, text = '조회', command = get_result, width = 13, bg = 'white', height = 2, padx = 10, pady = 10)
    stat_button.place(x = 900, y = 35)

    #시스템 UI
    """
    name_label = Label(tk, text = '정보', relief = 'raised', bd = 2, width = 15, height = 3, font = 15)
    name_label.place(x = 100, y = 150)

    
    cost_label = Label(tk, text = '급여', relief = 'raised', bd = 2, width = 15, height = 3, font = 15)
    cost_label.place(x = 250, y = 150)

    name_label2 = Label(tk, text = '이름', relief = 'raised', bd = 2, width = 15, height = 3, font = 15)
    name_label2.place(x = 850, y = 150)

    cost_label2 = Label(tk, text = '급여', relief = 'raised', bd = 2, width = 15, height = 3, font = 15)
    cost_label2.place(x = 1000, y = 150)
    """

    #이름 / 급여 시작
    #1번 직원
    worker1_name = Text(tk,  relief = 'solid', bd = 3, width = 100, height = 20, font = ("", 15,"bold"))
    worker1_name.place(x = 100, y = 220)


    """
    worker1_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker1_cost.place(x = 250, y = 220)
    worker1_cost.insert(1.0, "급 여")

    #2번 직원
    
    worker2_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker2_name.place(x = 100, y = 300)

    worker2_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker2_cost.place(x = 250, y = 300)

    #3번 직원
    worker3_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker3_name.place(x = 100, y = 380)

    worker3_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker3_cost.place(x = 250, y = 380)

    #4번 직원
    worker4_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker4_name.place(x = 100, y = 460)

    worker4_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker4_cost.place(x = 250, y = 460)

    #5번 직원
    worker5_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker5_name.place(x = 100, y = 540)

    worker5_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker5_cost.place(x = 250, y = 540)

    #6번 직원
    worker6_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker6_name.place(x = 100, y = 620)

    worker6_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker6_cost.place(x = 250, y = 620)

    #7번 직원
    worker7_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker7_name.place(x = 100, y = 700)

    worker7_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker7_cost.place(x = 250, y = 700)

    #8번 직원
    worker8_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker8_name.place(x = 100, y = 780)

    worker8_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker8_cost.place(x = 250, y = 780)

    #오른쪽
    #9번 직원
    worker9_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker9_name.place(x = 850, y = 220)

    worker9_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker9_cost.place(x = 1000, y = 220)

    #10번 직원
    worker10_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker10_name.place(x = 850, y = 300)

    worker10_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker10_cost.place(x = 1000, y = 300)

    #11번 직원
    worker11_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker11_name.place(x = 850, y = 380)

    worker11_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker11_cost.place(x = 1000, y = 380)

    #12번 직원
    worker12_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker12_name.place(x = 850, y = 460)

    worker12_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker12_cost.place(x = 1000, y = 460)

    #13번 직원
    worker13_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker13_name.place(x = 850, y = 540)

    worker13_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker13_cost.place(x = 1000, y = 540)

    #14번 직원
    worker14_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker14_name.place(x = 850, y = 620)

    worker14_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker14_cost.place(x = 1000, y = 620)

    #15번 직원
    worker15_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker15_name.place(x = 850, y = 700)

    worker15_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker15_cost.place(x = 1000, y = 700)

    #16번 직원
    worker16_name = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker16_name.place(x = 850, y = 780)

    worker16_cost = Text(tk,  relief = 'solid', bd = 3, width = 12, height = 2, font = ("", 15,"bold"))
    worker16_cost.place(x = 1000, y = 780)
    #####################################################
    ####################UI 작성 종료######################
    #####################################################
    """
    tk.mainloop()