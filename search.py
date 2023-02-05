from tkinter import *
import pickle


#저장 후 종료
def save_exit():
    exit()


#프로그램 시작
def start_search():
    part_info = []
    worker_info = []
    super_info = []
    try:
        part_file = open("part_info", "rb")
        part_info = pickle.load(part_file)
        part_file.close()

        worker_file = open("worker_info", "rb")
        worker_info = pickle.load(worker_file)
        worker_file.close()

        try:
            super_file = open("super_info", "rb")
            super_info = pickle.load(super_file)
            super_file.close()
            print(super_info)
        except:
            print("관리자 정보가 없습니다.")
        print(part_info)
        print(worker_info)
    except:
        print("아르바이트 정보를 먼저 입력해주세요 !")


    #####################################################
    ####################UI 작성 시작######################
    #####################################################
    tk = Tk()
    tk.title("Part Timer Scheduler") #제목
    tk.geometry("1280x1000+100+100") #Window 크기 설정
    tk.resizable(True, True) #Window 크기 조절 여부(상하, 좌우)

    title_label = Label(tk, text = '시간표 조회', relief = 'raised', bd = 2, width = 30, height = 5, font = 20)
    title_label.pack(side='top')

    #파트 당 최대 근무 인원수 작성
    max_worker = Text(tk, width = 12, height = 2, font = 12, wrap = "word")
    max_worker.place(x = 20, y = 50)
    max_worker.insert(1.0, "인원 수")

    #시간표 조회 시작
    search_button = Button(tk, text = '시간표 조회', width = 13, bg = 'blue', fg = 'white', height = 2, padx = 10, pady = 10)
    search_button.place(x = 150, y = 35)

    #종료 버튼
    exit_button = Button(tk, text = '뒤로 가기', command = save_exit, width = 13, bg = 'white', height = 2, padx = 10, pady = 10)
    exit_button.place(x = 1100, y = 35)

    #파트 1 - 4 Label
    part1_label = Label(tk, text = '파트 1', relief = 'solid', bd = 2, width = 10, height = 8, font = 15)
    part1_label.place(x = 20, y = 220)

    part2_label = Label(tk, text = '파트 2', relief = 'solid', bd = 2, width = 10, height = 8, font = 15)
    part2_label.place(x = 20, y = 420)

    part3_label = Label(tk, text = '파트 3', relief = 'solid', bd = 2, width = 10, height = 8, font = 15)
    part3_label.place(x = 20, y = 620)

    part4_label = Label(tk, text = '파트 4', relief = 'solid', bd = 2, width = 10, height = 8, font = 15)
    part4_label.place(x = 20, y = 820)

    #요일 Label
    mon_label = Label(tk, text = '월', relief = 'raised', bd = 2, width = 10, height = 3, font = 10)
    mon_label.place(x = 200, y = 150)

    tue_label = Label(tk, text = '화', relief = 'raised', bd = 2, width = 10, height = 3, font = 10)
    tue_label.place(x = 350, y = 150)

    wed_label = Label(tk, text = '수', relief = 'raised', bd = 2, width = 10, height = 3, font = 10)
    wed_label.place(x = 500, y = 150)

    thu_label = Label(tk, text = '목', relief = 'raised', bd = 2, width = 10, height = 3, font = 10)
    thu_label.place(x = 650, y = 150)

    fri_label = Label(tk, text = '금', relief = 'raised', bd = 2, width = 10, height = 3, font = 10)
    fri_label.place(x = 800, y = 150)

    sat_label = Label(tk, text = '토', relief = 'raised', bg = 'blue', fg = 'white', bd = 2, width = 10, height = 3, font = 15)
    sat_label.place(x = 950, y = 150)

    sun_label = Label(tk, text = '일', relief = 'raised', bg = 'red', fg = 'white', bd = 2, width = 10, height = 3, font = 15)
    sun_label.place(x = 1100, y = 150)

    #근무인원 표시 Text
    # 파트 1
    mon_part1 = Text(tk, bg = 'white', relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    mon_part1.place(x = 185, y = 220)
    mon_part1.insert(1.0, "     오영석\n     김두현\n     김민석")

    tue_part1 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    tue_part1.place(x = 335, y = 220)

    wed_part1 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    wed_part1.place(x = 485, y = 220)

    thu_part1 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    thu_part1.place(x = 635, y = 220)

    fri_part1 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    fri_part1.place(x = 785, y = 220)

    sat_part1 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    sat_part1.place(x = 935, y = 220)

    sun_part1 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    sun_part1.place(x = 1085, y = 220)

    #파트 2
    mon_part2 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    mon_part2.place(x = 185, y = 420)
    mon_part2.insert(1.0, "     오영석\n     김두현\n     김민석")

    tue_part2 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    tue_part2.place(x = 335, y = 420)

    wed_part2 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    wed_part2.place(x = 485, y = 420)

    thu_part2 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    thu_part2.place(x = 635, y = 420)

    fri_part2 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    fri_part2.place(x = 785, y = 420)

    sat_part2 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    sat_part2.place(x = 935, y = 420)

    sun_part2 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    sun_part2.place(x = 1085, y = 420)

    #파트 3
    mon_part3 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    mon_part3.place(x = 185, y = 620)
    mon_part3.insert(1.0, "     오영석\n     김두현\n     김민석")

    tue_part3 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    tue_part3.place(x = 335, y = 620)

    wed_part3 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    wed_part3.place(x = 485, y = 620)

    thu_part3 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    thu_part3.place(x = 635, y = 620)

    fri_part3 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    fri_part3.place(x = 785, y = 620)

    sat_part3 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    sat_part3.place(x = 935, y = 620)

    sun_part3 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    sun_part3.place(x = 1085, y = 620)

    #파트 4
    mon_part4 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    mon_part4.place(x = 185, y = 820)
    mon_part4.insert(1.0, "     오영석\n     김두현\n     김민석")

    tue_part4 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    tue_part4.place(x = 335, y = 820)

    wed_part4 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    wed_part4.place(x = 485, y = 820)

    thu_part4 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    thu_part4.place(x = 635, y = 820)

    fri_part4 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    fri_part4.place(x = 785, y = 820)

    sat_part4 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    sat_part4.place(x = 935, y = 820)

    sun_part4 = Text(tk, relief = 'solid', bd = 4, width = 11, height = 6, font = ("", 15,"bold"))
    sun_part4.place(x = 1085, y = 820)
    tk.mainloop()
    #####################################################
    ####################UI 작성 종료######################
    #####################################################


