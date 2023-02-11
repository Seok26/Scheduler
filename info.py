from tkinter import *
import pickle


#
#UI 변수 글로벌 선언
#파트 부분
global part1_entry_start
global part1_entry_end
global part1_text_cost
global part2_entry_start
global part2_entry_end
global part2_text_cost
global part3_entry_start
global part3_entry_end
global part3_text_cost
global part4_entry_start
global part4_entry_end
global part4_text_cost

#직원정보
#1번
global worker_text
global part1_check_1
global part1_checkbox_1
global part2_check_1
global part2_checkbox_1
global part3_check_1
global part3_checkbox_1
global part4_check_1
global part4_checkbox_1
global check_super_1
global checkbox_super_1
#2번
global worker2_text
global part1_check_2
global part1_checkbox_2
global part2_check_2
global part2_checkbox_2
global part3_check_2
global part3_checkbox_2
global part4_check_2
global part4_checkbox_2
global check_super_2
global checkbox_super_2
#3번
global worker3_text
global part1_check_3
global part1_checkbox_3
global part2_check_3
global part2_checkbox_3
global part3_check_3
global part3_checkbox_3
global part4_check_3
global part4_checkbox_3
global check_super_3
global checkbox_super_3
#4번
global worker4_text
global part1_check_4
global part1_checkbox_4
global part2_check_4
global part2_checkbox_4
global part3_check_4
global part3_checkbox_4
global part4_check_4
global part4_checkbox_4
global check_super_4
global checkbox_super_4
#5번
global worker5_text
global part1_check_5
global part1_checkbox_5
global part2_check_5
global part2_checkbox_5
global part3_check_5
global part3_checkbox_5
global part4_check_5
global part4_checkbox_5
global check_super_5
global checkbox_super_5
#6번
global worker6_text
global part1_check_6
global part1_checkbox_6
global part2_check_6
global part2_checkbox_6
global part3_check_6
global part3_checkbox_6
global part4_check_6
global part4_checkbox_6
global check_super_6
global checkbox_super_6
#7번
global worker7_text
global part1_check_7
global part1_checkbox_7
global part2_check_7
global part2_checkbox_7
global part3_check_7
global part3_checkbox_7
global part4_check_7
global part4_checkbox_7
global check_super_7
global checkbox_super_7
#8번
global worker8_text
global part1_check_8
global part1_checkbox_8
global part2_check_8
global part2_checkbox_8
global part3_check_8
global part3_checkbox_8
global part4_check_8
global part4_checkbox_8
global check_super_8
global checkbox_super_8
#9번
global worker9_text
global part1_check_9
global part1_checkbox_9
global part2_check_9
global part2_checkbox_9
global part3_check_9
global part3_checkbox_9
global part4_check_9
global part4_checkbox_9
global check_super_9
global checkbox_super_9
#10번
global worker10_text
global part1_check_10
global part1_checkbox_10
global part2_check_10
global part2_checkbox_10
global part3_check_10
global part3_checkbox_10
global part4_check_10
global part4_checkbox_10
global check_super_10
global checkbox_super_10
#11번
global worker11_text
global part1_check_11
global part1_checkbox_11
global part2_check_11
global part2_checkbox_11
global part3_check_11
global part3_checkbox_11
global part4_check_11
global part4_checkbox_11
global check_super_11
global checkbox_super_11
#12번
global worker12_text
global part1_check_12
global part1_checkbox_12
global part2_check_12
global part2_checkbox_12
global part3_check_12
global part3_checkbox_12
global part4_check_12
global part4_checkbox_12
global check_super_12
global checkbox_super_12
#13번
global worker13_text
global part1_check_13
global part1_checkbox_13
global part2_check_13
global part2_checkbox_13
global part3_check_13
global part3_checkbox_13
global part4_check_13
global part4_checkbox_13
global check_super_13
global checkbox_super_13
#14번
global worker14_text
global part1_check_14
global part1_checkbox_14
global part2_check_14
global part2_checkbox_14
global part3_check_14
global part3_checkbox_14
global part4_check_14
global part4_checkbox_14
global check_super_14
global checkbox_super_14
#15번
global worker15_text
global part1_check_15
global part1_checkbox_15
global part2_check_15
global part2_checkbox_15
global part3_check_15
global part3_checkbox_15
global part4_check_15
global part4_checkbox_15
global check_super_15
global checkbox_super_15
#16번
global worker16_text
global part1_check_16
global part1_checkbox_16
global part2_check_16
global part2_checkbox_16
global part3_check_16
global part3_checkbox_16
global part4_check_16
global part4_checkbox_16
global check_super_16
global checkbox_super_16


#02.05 추가(체크박스 값을 대신할 변수)
worker1_part1 = 0
worker1_part2 = 0
worker1_part3 = 0
worker1_part4 = 0
worker1_super = 0
worker2_part1 = 0
worker2_part2 = 0
worker2_part3 = 0
worker2_part4 = 0
worker2_super = 0
worker3_part1 = 0
worker3_part2 = 0
worker3_part3 = 0
worker3_part4 = 0
worker3_super = 0
worker4_part1 = 0
worker4_part2 = 0
worker4_part3 = 0
worker4_part4 = 0
worker4_super = 0
worker5_part1 = 0
worker5_part2 = 0
worker5_part3 = 0
worker5_part4 = 0
worker5_super = 0
worker6_part1 = 0
worker6_part2 = 0
worker6_part3 = 0
worker6_part4 = 0
worker6_super = 0
worker7_part1 = 0
worker7_part2 = 0
worker7_part3 = 0
worker7_part4 = 0
worker7_super = 0
worker8_part1 = 0
worker8_part2 = 0
worker8_part3 = 0
worker8_part4 = 0
worker8_super = 0
worker9_part1 = 0
worker9_part2 = 0
worker9_part3 = 0
worker9_part4 = 0
worker9_super = 0
worker10_part1 = 0
worker10_part2 = 0
worker10_part3 = 0
worker10_part4 = 0
worker10_super = 0
worker11_part1 = 0
worker11_part2 = 0
worker11_part3 = 0
worker11_part4 = 0
worker11_super = 0
worker12_part1 = 0
worker12_part2 = 0
worker12_part3 = 0
worker12_part4 = 0
worker12_super = 0
worker13_part1 = 0
worker13_part2 = 0
worker13_part3 = 0
worker13_part4 = 0
worker13_super = 0
worker14_part1 = 0
worker14_part2 = 0
worker14_part3 = 0
worker14_part4 = 0
worker14_super = 0
worker15_part1 = 0
worker15_part2 = 0
worker15_part3 = 0
worker15_part4 = 0
worker15_super = 0
worker16_part1 = 0
worker16_part2 = 0
worker16_part3 = 0
worker16_part4 = 0
worker16_super = 0
#02.05 추가 끝

#파트번호 / 직원번호
def checkbox_check(idx, number):
    global worker1_part1
    global worker1_part2
    global worker1_part3
    global worker1_part4
    global worker1_super
    global worker2_part1
    global worker2_part2
    global worker2_part3
    global worker2_part4
    global worker2_super
    global worker3_part1
    global worker3_part2
    global worker3_part3
    global worker3_part4
    global worker3_super
    global worker4_part1
    global worker4_part2
    global worker4_part3
    global worker4_part4
    global worker4_super
    global worker5_part1
    global worker5_part2
    global worker5_part3
    global worker5_part4
    global worker5_super
    global worker6_part1
    global worker6_part2
    global worker6_part3
    global worker6_part4
    global worker6_super
    global worker7_part1
    global worker7_part2
    global worker7_part3
    global worker7_part4
    global worker7_super
    global worker8_part1
    global worker8_part2
    global worker8_part3
    global worker8_part4
    global worker8_super
    global worker9_part1
    global worker9_part2
    global worker9_part3
    global worker9_part4
    global worker9_super
    global worker10_part1
    global worker10_part2
    global worker10_part3
    global worker10_part4
    global worker10_super
    global worker11_part1
    global worker11_part2
    global worker11_part3
    global worker11_part4
    global worker11_super
    global worker12_part1
    global worker12_part2
    global worker12_part3
    global worker12_part4
    global worker12_super
    global worker13_part1
    global worker13_part2
    global worker13_part3
    global worker13_part4
    global worker13_super
    global worker14_part1
    global worker14_part2
    global worker14_part3
    global worker14_part4
    global worker14_super
    global worker15_part1
    global worker15_part2
    global worker15_part3
    global worker15_part4
    global worker15_super
    global worker16_part1
    global worker16_part2
    global worker16_part3
    global worker16_part4
    global worker16_super

    if number == 1:
        if idx == 1:
            worker1_part1 = 1
        elif idx == 2:
            worker1_part2 = 1
        elif idx == 3:
            worker1_part3 = 1
        elif idx == 4:
            worker1_part4 = 1
        else:
            worker1_super = 1
    elif number == 2:
        if idx == 1:
            worker2_part1 = 1
        elif idx == 2:
            worker2_part2 = 1
        elif idx == 3:
            worker2_part3 = 1
        elif idx == 4:
            worker2_part4 = 1
        else:
            worker2_super = 1
    elif number == 3:
        if idx == 1:
            worker3_part1 = 1
        elif idx == 2:
            worker3_part2 = 1
        elif idx == 3:
            worker3_part3 = 1
        elif idx == 4:
            worker3_part4 = 1
        else:
            worker3_super = 1
    elif number == 4:
        if idx == 1:
            worker4_part1 = 1
        elif idx == 2:
            worker4_part2 = 1
        elif idx == 3:
            worker4_part3 = 1
        elif idx == 4:
            worker4_part4 = 1
        else:
            worker4_super = 1
    elif number == 5:
        if idx == 1:
            worker5_part1 = 1
        elif idx == 2:
            worker5_part2 = 1
        elif idx == 3:
            worker5_part3 = 1
        elif idx == 4:
            worker5_part4 = 1
        else:
            worker5_super = 1
    elif number == 6:
        if idx == 1:
            worker6_part1 = 1
        elif idx == 2:
            worker6_part2 = 1
        elif idx == 3:
            worker6_part3 = 1
        elif idx == 4:
            worker6_part4 = 1
        else:
            worker6_super = 1
    elif number == 7:
        if idx == 1:
            worker7_part1 = 1
        elif idx == 2:
            worker7_part2 = 1
        elif idx == 3:
            worker7_part3 = 1
        elif idx == 4:
            worker7_part4 = 1
        else:
            worker7_super = 1
    elif number == 8:
        if idx == 1:
            worker8_part1 = 1
        elif idx == 2:
            worker8_part2 = 1
        elif idx == 3:
            worker8_part3 = 1
        elif idx == 4:
            worker8_part4 = 1
        else:
            worker8_super = 1
    elif number == 9:
        if idx == 1:
            worker9_part1 = 1
        elif idx == 2:
            worker9_part2 = 1
        elif idx == 3:
            worker9_part3 = 1
        elif idx == 4:
            worker9_part4 = 1
        else:
            worker9_super = 1
    elif number == 10:
        if idx == 1:
            worker10_part1 = 1
        elif idx == 2:
            worker10_part2 = 1
        elif idx == 3:
            worker10_part3 = 1
        elif idx == 4:
            worker10_part4 = 1
        else:
            worker10_super = 1
    elif number == 11:
        if idx == 1:
            worker11_part1 = 1
        elif idx == 2:
            worker11_part2 = 1
        elif idx == 3:
            worker11_part3 = 1
        elif idx == 4:
            worker11_part4 = 1
        else:
            worker11_super = 1
    elif number == 12:
        if idx == 1:
            worker12_part1 = 1
        elif idx == 2:
            worker12_part2 = 1
        elif idx == 3:
            worker12_part3 = 1
        elif idx == 4:
            worker12_part4 = 1
        else:
            worker12_super = 1
    elif number == 13:
        if idx == 1:
            worker13_part1 = 1
        elif idx == 2:
            worker13_part2 = 1
        elif idx == 3:
            worker13_part3 = 1
        elif idx == 4:
            worker13_part4 = 1
        else:
            worker13_super = 1
    elif number == 14:
        if idx == 1:
            worker14_part1 = 1
        elif idx == 2:
            worker14_part2 = 1
        elif idx == 3:
            worker14_part3 = 1
        elif idx == 4:
            worker14_part4 = 1
        else:
            worker14_super = 1
    elif number == 15:
        if idx == 1:
            worker15_part1 = 1
        elif idx == 2:
            worker15_part2 = 1
        elif idx == 3:
            worker15_part3 = 1
        elif idx == 4:
            worker15_part4 = 1
        else:
            worker15_super = 1
    else:
        if idx == 1:
            worker16_part1 = 1
        elif idx == 2:
            worker16_part2 = 1
        elif idx == 3:
            worker16_part3 = 1
        elif idx == 4:
            worker16_part4 = 1
        else:
            worker16_super = 1


#파일 저장 후 종료
def save_exit():
    global part1_entry_start
    global part1_entry_end
    global part1_text_cost
    global part2_entry_start
    global part2_entry_end
    global part2_text_cost
    global part3_entry_start
    global part3_entry_end
    global part3_text_cost
    global part4_entry_start
    global part4_entry_end
    global part4_text_cost
    global worker_text
    global worker2_text
    global worker3_text
    global worker4_text
    global worker5_text
    global worker6_text
    global worker7_text
    global worker8_text
    global worker9_text
    global worker10_text
    global worker11_text
    global worker12_text
    global worker13_text
    global worker14_text
    global worker15_text
    global worker16_text
    global worker1_part1
    global worker1_part2
    global worker1_part3
    global worker1_part4
    global worker1_super
    global worker2_part1
    global worker2_part2
    global worker2_part3
    global worker2_part4
    global worker2_super
    global worker3_part1
    global worker3_part2
    global worker3_part3
    global worker3_part4
    global worker3_super
    global worker4_part1
    global worker4_part2
    global worker4_part3
    global worker4_part4
    global worker4_super
    global worker5_part1
    global worker5_part2
    global worker5_part3
    global worker5_part4
    global worker5_super
    global worker6_part1
    global worker6_part2
    global worker6_part3
    global worker6_part4
    global worker6_super
    global worker7_part1
    global worker7_part2
    global worker7_part3
    global worker7_part4
    global worker7_super
    global worker8_part1
    global worker8_part2
    global worker8_part3
    global worker8_part4
    global worker8_super
    global worker9_part1
    global worker9_part2
    global worker9_part3
    global worker9_part4
    global worker9_super
    global worker10_part1
    global worker10_part2
    global worker10_part3
    global worker10_part4
    global worker10_super
    global worker11_part1
    global worker11_part2
    global worker11_part3
    global worker11_part4
    global worker11_super
    global worker12_part1
    global worker12_part2
    global worker12_part3
    global worker12_part4
    global worker12_super
    global worker13_part1
    global worker13_part2
    global worker13_part3
    global worker13_part4
    global worker13_super
    global worker14_part1
    global worker14_part2
    global worker14_part3
    global worker14_part4
    global worker14_super
    global worker15_part1
    global worker15_part2
    global worker15_part3
    global worker15_part4
    global worker15_super
    global worker16_part1
    global worker16_part2
    global worker16_part3
    global worker16_part4
    global worker16_super



    #데이터를 저장할 리스트 선언
    #index 0의 데이터는 저장시 필요한 구분
    part_info = [] #파트 정보
    part_info.append("part")
    worker_info = [] #직원 정보
    worker_info.append("worker")
    super_info = [] #관리자 정보 length가 0이면 일반 모드라고 판단
    super_info.append("super")

    ##########################################################
    ##################데이터 불러오기 시작#########################
    ##########################################################
    #파트 저장
    if part1_entry_start.get() != '':
        part_info.append([part1_entry_start.get(), part1_entry_end.get(), part1_text_cost.get(1.0, "end").replace("\n", "")])
    if part2_entry_start.get() != '':
        part_info.append([part2_entry_start.get(), part2_entry_end.get(), part2_text_cost.get(1.0, "end").replace("\n", "")])
    if part3_entry_start.get() != '':
        part_info.append([part3_entry_start.get(), part3_entry_end.get(), part3_text_cost.get(1.0, "end").replace("\n", "")])
    if part4_entry_start.get() != '':
        part_info.append([part4_entry_start.get(), part4_entry_end.get(), part4_text_cost.get(1.0, "end").replace("\n", "")])

    #직원 정보 저장 시작
    #관리자면 관리자로 저장 아니면 일반 직원
    if worker_text.get(1.0, "end") != "\n":
        if worker1_super == 1:
            super_info.append([worker_text.get(1.0, "end").replace("\n", ""), worker1_part1, worker1_part2, worker1_part3, worker1_part4])
        else:
            worker_info.append([worker_text.get(1.0, "end").replace("\n", ""), worker1_part1, worker1_part2, worker1_part3, worker1_part4])
    if worker2_text.get(1.0, "end") != "\n":
        if worker2_super == 1:
            super_info.append([worker2_text.get(1.0, "end").replace("\n", ""), worker2_part1, worker2_part2, worker2_part3, worker2_part4])
        else:
            worker_info.append([worker2_text.get(1.0, "end").replace("\n", ""), worker2_part1, worker2_part2, worker2_part3, worker2_part4])
    if worker3_text.get(1.0, "end") != "\n":
        if worker3_super == 1:
            super_info.append([worker3_text.get(1.0, "end").replace("\n", ""), worker3_part1, worker3_part2, worker3_part3, worker3_part4])
        else:
            worker_info.append([worker3_text.get(1.0, "end").replace("\n", ""), worker3_part1, worker3_part2, worker3_part3, worker3_part4])
    if worker4_text.get(1.0, "end") != "\n":
        if worker4_super == 1:
            super_info.append([worker4_text.get(1.0, "end").replace("\n", ""), worker4_part1, worker4_part2, worker4_part3, worker4_part4])
        else:
            worker_info.append([worker4_text.get(1.0, "end").replace("\n", ""), worker4_part1, worker4_part2, worker4_part3, worker4_part4])
    if worker5_text.get(1.0, "end") != "\n":
        if worker5_super == 1:
            super_info.append([worker5_text.get(1.0, "end").replace("\n", ""), worker5_part1, worker5_part2, worker5_part3, worker5_part4])
        else:
            worker_info.append([worker5_text.get(1.0, "end").replace("\n", ""), worker5_part1, worker5_part2, worker5_part3, worker5_part4])
    if worker6_text.get(1.0, "end") != "\n":
        if worker6_super == 1:
            super_info.append([worker6_text.get(1.0, "end").replace("\n", ""), worker6_part1, worker6_part2, worker6_part3, worker6_part4])
        else:
            worker_info.append([worker6_text.get(1.0, "end").replace("\n", ""), worker6_part1, worker6_part2, worker6_part3, worker6_part4])
    if worker7_text.get(1.0, "end") != "\n":
        if worker7_super == 1:
            super_info.append([worker7_text.get(1.0, "end").replace("\n", ""), worker7_part1, worker7_part2, worker7_part3, worker7_part4])
        else:
            worker_info.append([worker7_text.get(1.0, "end").replace("\n", ""), worker7_part1, worker7_part2, worker7_part3, worker7_part4])
    if worker8_text.get(1.0, "end") != "\n":
        if worker8_super == 1:
            super_info.append([worker8_text.get(1.0, "end").replace("\n", ""), worker8_part1, worker8_part2, worker8_part3, worker8_part4])
        else:
            worker_info.append([worker8_text.get(1.0, "end").replace("\n", ""), worker8_part1, worker8_part2, worker8_part3, worker8_part4])
    if worker9_text.get(1.0, "end") != "\n":
        if worker9_super == 1:
            super_info.append([worker9_text.get(1.0, "end").replace("\n", ""), worker9_part1, worker9_part2, worker9_part3, worker9_part4])
        else:
            worker_info.append([worker9_text.get(1.0, "end").replace("\n", ""), worker9_part1, worker9_part2, worker9_part3, worker9_part4])
    if worker10_text.get(1.0, "end") != "\n":
        if worker10_super == 1:
            super_info.append([worker10_text.get(1.0, "end").replace("\n", ""), worker10_part1, worker10_part2, worker10_part3, worker10_part4])
        else:
            worker_info.append([worker10_text.get(1.0, "end").replace("\n", ""), worker10_part1, worker10_part2, worker10_part3, worker10_part4])
    if worker11_text.get(1.0, "end") != "\n":
        if worker11_super == 1:
            super_info.append([worker11_text.get(1.0, "end").replace("\n", ""), worker11_part1, worker11_part2, worker11_part3, worker11_part4])
        else:
            worker_info.append([worker11_text.get(1.0, "end").replace("\n", ""), worker11_part1, worker11_part2, worker11_part3, worker11_part4])
    if worker12_text.get(1.0, "end") != "\n":
        if worker12_super == 1:
            super_info.append([worker12_text.get(1.0, "end").replace("\n", ""), worker12_part1, worker12_part2, worker12_part3, worker12_part4])
        else:
            worker_info.append([worker12_text.get(1.0, "end").replace("\n", ""), worker12_part1, worker12_part2, worker12_part3, worker12_part4])
    if worker13_text.get(1.0, "end") != "\n":
        if worker13_super == 1:
            super_info.append([worker13_text.get(1.0, "end").replace("\n", ""), worker13_part1, worker13_part2, worker13_part3, worker13_part4])
        else:
            worker_info.append([worker13_text.get(1.0, "end").replace("\n", ""), worker13_part1, worker13_part2, worker13_part3, worker13_part4])
    if worker14_text.get(1.0, "end") != "\n":
        if worker14_super == 1:
            super_info.append([worker14_text.get(1.0, "end").replace("\n", ""), worker14_part1, worker14_part2, worker14_part3, worker14_part4])
        else:
            worker_info.append([worker14_text.get(1.0, "end").replace("\n", ""), worker14_part1, worker14_part2, worker14_part3, worker14_part4])
    if worker15_text.get(1.0, "end") != "\n":
        if worker15_super == 1:
            super_info.append([worker15_text.get(1.0, "end").replace("\n", ""), worker15_part1, worker15_part2, worker15_part3, worker15_part4])
        else:
            worker_info.append([worker15_text.get(1.0, "end").replace("\n", ""), worker15_part1, worker15_part2, worker15_part3, worker15_part4])
    if worker16_text.get(1.0, "end") != "\n":
        if worker16_super == 1:
            super_info.append([worker16_text.get(1.0, "end").replace("\n", ""), worker16_part1, worker16_part2, worker16_part3, worker16_part4])
        else:
            worker_info.append([worker16_text.get(1.0, "end").replace("\n", ""), worker16_part1, worker16_part2, worker16_part3, worker16_part4])
    ##########################################################
    ##################데이터 불러오기 끝#########################
    ##########################################################
    #파일로 데이터 저장
    part_file = open("part_info", "wb")
    pickle.dump(part_info, part_file)
    part_file.close()

    worker_file = open("worker_info", "wb")
    pickle.dump(worker_info, worker_file)
    worker_file.close()

    if len(super_info) != 1:
        super_file = open("super_info", "wb")
        pickle.dump(super_info, super_file)
        super_file.close()
    exit()


def set_cost_all():
    global part1_entry_start
    global part1_text_cost
    global part2_entry_start
    global part2_text_cost
    global part3_entry_start
    global part3_text_cost
    global part4_entry_start
    global part4_text_cost

    if part2_entry_start.get() != "" :
        part2_text_cost.insert(1.0, part1_text_cost.get("1.0", "end"))

    if part3_entry_start.get() != "" :
        part3_text_cost.insert(1.0, part1_text_cost.get("1.0", "end"))

    if part4_entry_start.get() != "" :
        part4_text_cost.insert(1.0, part1_text_cost.get("1.0", "end"))




#프로그램 시작
def start_info():
    global part1_entry_start
    global part1_entry_end
    global part1_text_cost
    global part2_entry_start
    global part2_entry_end
    global part2_text_cost
    global part3_entry_start
    global part3_entry_end
    global part3_text_cost
    global part4_entry_start
    global part4_entry_end
    global part4_text_cost
    global worker_text
    global worker2_text
    global worker3_text
    global worker4_text
    global worker5_text
    global worker6_text
    global worker7_text
    global worker8_text
    global worker9_text
    global worker10_text
    global worker11_text
    global worker12_text
    global worker13_text
    global worker14_text
    global worker15_text
    global worker16_text
    #####################################################
    ####################UI 작성 시작######################
    #####################################################
    tk = Tk()
    tk.title("Part Timer Scheduler") #제목
    tk.geometry("1280x800+100+100") #Window 크기 설정
    tk.resizable(True, True) #Window 크기 조절 여부(상하, 좌우)


    #프레임1 : 파트 및 급여 정보 입력
    frame1 = Frame(tk, relief = 'solid', bd = 2)
    frame1.pack(side = 'left', fill = 'both', expand=True)

    #프레임2 : 직원 정보 입력
    frame2 = Frame(tk, relief = "solid", bd = 2)
    frame2.pack(side="right", fill= "both", expand = True)

    #가이드 UI
    title_label = Label(frame1, text = '아르바이트 정보 입력', relief = 'raised', bd = 2, width = 30, height = 5, font = 20)
    title_label.place(x = 0, y = 0)

    name_label = Label(frame1, text = '파트 정보 입력', relief = 'raised', bd = 2, width = 20, height = 4, font = 20)
    name_label.place(x = 220, y = 100)

    weekday_label = Label(frame1, text = '시간 및 급여', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    weekday_label.place(x = 150, y = 275)

    """
    weekend_label = Label(frame1, text = '주말', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    weekend_label.place(x = 380, y = 275)
    """

    costset_button = Button(frame1, text = '급여 일괄 적용', overrelief= "solid", command = set_cost_all, bg = 'white', width = 12, height = 2, font = 12)
    costset_button.place(x = 15, y = 285)

    announce_label = Label(frame1, text = '사용하지 않는 파트 칸은 비워두세요.', relief = 'groove', bd = 2, width = 40, height = 3, font = 15)
    announce_label.place(x = 140, y = 200)

    #파트 1 입력 칸
    #평일 파트 1
    part1_label = Label(frame1, text = '파트 1', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    part1_label.place(x = 20, y = 350)

    #시작 시간
    part1_entry_start = Entry(frame1, width = 16, justify = 'center')
    part1_entry_start.place(x= 150, y = 350)
    part1_entry_start.insert(0, "시작 시간") #시작시간 / 종료시간 안내는 파트 1 버튼에서만 수행

    #종료 시간
    part1_entry_end = Entry(frame1, width= 16, justify= 'center')
    part1_entry_end.place(x = 150, y = 385)
    part1_entry_end.insert(0, "종료 시간")

    #급여 입력 칸
    part1_text_cost = Text(frame1, width = 10, height = 2, font = 12)
    part1_text_cost.place(x = 278, y = 360)
    part1_text_cost.insert(1.0, "급여 입력")

    #주말 파트 1(02.04 주말 파트 주석처리되었음 : 직원 정보 입력 시 평일 / 주말 파트 구분 필요)
    """
    part1_entry_start_week = Entry(frame1, width = 16, justify= 'center')
    part1_entry_start_week.place(x = 378, y = 350)

    part1_entry_end_week = Entry(frame1, width = 16, justify=  'center')
    part1_entry_end_week.place(x = 378, y = 385)

    part1_text_cost_week = Text(frame1, width = 10, height = 2, font = 12)
    part1_text_cost_week.place(x = 506, y = 360)
    """

    #파트 2 입력 칸
    #평일 파트 2
    part2_label = Label(frame1, text = '파트 2', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    part2_label.place(x = 20, y = 450)

    part2_entry_start = Entry(frame1, width = 16, justify= 'center')
    part2_entry_start.place(x = 150, y = 450)

    part2_entry_end = Entry(frame1, width = 16, justify= 'center')
    part2_entry_end.place(x = 150, y = 485)

    part2_text_cost = Text(frame1, width = 10, height = 2, font = 12)
    part2_text_cost.place(x = 278, y = 460)

    #주말 파트 2
    """
    part2_entry_start_week = Entry(frame1, width = 16, justify= 'center')
    part2_entry_start_week.place(x = 378, y = 450)

    part2_entry_end_week = Entry(frame1, width = 16, justify= 'center')
    part2_entry_end_week.place(x = 378, y = 485)

    part2_text_cost_week = Text(frame1, width = 10, height = 2, font = 12)
    part2_text_cost_week.place(x = 506, y = 460)
    """

    #파트 3 입력 칸
    #평일 파트 3
    part3_label = Label(frame1, text = '파트 3', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    part3_label.place(x = 20, y = 550)

    part3_entry_start = Entry(frame1, width = 16, justify= 'center')
    part3_entry_start.place(x = 150, y = 550)

    part3_entry_end = Entry(frame1, width = 16, justify= 'center')
    part3_entry_end.place(x = 150, y = 585)

    part3_text_cost = Text(frame1, width = 10, height = 2, font = 12)
    part3_text_cost.place(x = 278, y = 560)

    #주말 파트 3
    """
    part3_entry_start_week = Entry(frame1, width = 16, justify= 'center')
    part3_entry_start_week.place(x = 378, y = 550)

    part3_entry_end_week = Entry(frame1, width = 16, justify= 'center')
    part3_entry_end_week.place(x = 378, y = 585)

    part3_text_cost_week = Text(frame1, width = 10, height = 2, font = 12)
    part3_text_cost_week.place(x = 506, y = 560)
    """

    #파트 4 입력 칸
    #평일 파트 4
    part4_label = Label(frame1, text = '파트 4', relief = 'raised', bd = 2, width = 12, height = 3, font = 15)
    part4_label.place(x = 20, y = 650)

    part4_entry_start = Entry(frame1, width = 16, justify= 'center')
    part4_entry_start.place(x = 150, y = 650)

    part4_entry_end = Entry(frame1, width = 16, justify= 'center')
    part4_entry_end.place(x = 150, y = 685)

    part4_text_cost = Text(frame1, width = 10, height = 2, font = 12)
    part4_text_cost.place(x = 278, y = 660)

    #주말 파트 4
    """
    part3_entry_start_week = Entry(frame1, width = 16, justify= 'center')
    part3_entry_start_week.place(x = 378, y = 650)

    part3_entry_end_week = Entry(frame1, width = 16, justify= 'center')
    part3_entry_end_week.place(x = 378, y = 685)

    part4_text_cost_week = Text(frame1, width = 10, height = 2, font = 12)
    part4_text_cost_week.place(x = 506, y = 660)
    """

    #프레임 2 직원 정보 입력
    name_label2 = Label(frame2, text = '직원 정보 입력', relief = 'raised', bd = 2, width = 20, height = 4, font = 20)
    name_label2.place(x = 220, y = 100)

    announce_label2 = Label(frame2, text = '근무 가능한 파트에 체크하세요', relief = 'groove', bd = 2, width = 40, height = 3, font = 15)
    announce_label2.place(x = 140, y = 200)

    #1번 직원 이름
    worker_text = Text(frame2, width = 13, height = 1, font = 12)
    worker_text.place(x = 50, y = 270)
    worker_text.insert(1.0, '이름 입력')

    #파트 체크박스
    part1_check_1 = IntVar()
    part1_checkbox_1 = Checkbutton(frame2, text = '파트 1', variable=part1_check_1, command= lambda : checkbox_check(1, 1))
    part1_checkbox_1.place(x = 38, y = 295)

    part2_check_1 = IntVar()
    part2_checkbox_1 = Checkbutton(frame2, text = '파트 2', variable=part2_check_1, command= lambda : checkbox_check(2, 1))
    part2_checkbox_1.place(x = 105, y = 295)

    part3_check_1 = IntVar()
    part3_checkbox_1 = Checkbutton(frame2, text = '파트 3', variable=part3_check_1, command= lambda : checkbox_check(3, 1))
    part3_checkbox_1.place(x = 38, y = 325)

    part4_check_1 = IntVar()
    part4_checkbox_1 = Checkbutton(frame2, text = '파트 4', variable=part4_check_1, command= lambda : checkbox_check(4, 1))
    part4_checkbox_1.place(x = 105, y = 325)

    #관리자 여부 판단
    check_super_1 = IntVar()
    checkbox_super_1 = Checkbutton(frame2, text = '관리자', variable = check_super_1, command= lambda : checkbox_check(5, 1))
    checkbox_super_1.place(x = 70, y = 355)

    #2번 직원 입력 값
    worker2_text = Text(frame2, width = 13, height = 1, font = 12)
    worker2_text.place(x = 50, y = 385)

    #파트 체크박스
    part1_check_2 = IntVar()
    part1_checkbox_2 = Checkbutton(frame2, text = '파트 1', variable=part1_check_2, command= lambda : checkbox_check(1, 2))
    part1_checkbox_2.place(x = 38, y = 410)

    part2_check_2 = IntVar()
    part2_checkbox_2 = Checkbutton(frame2, text = '파트 2', variable=part2_check_2, command= lambda : checkbox_check(2, 2))
    part2_checkbox_2.place(x = 105, y = 410)

    part3_check_2 = IntVar()
    part3_checkbox_2 = Checkbutton(frame2, text = '파트 3', variable=part3_check_2, command= lambda : checkbox_check(3, 2))
    part3_checkbox_2.place(x = 38, y = 440)

    part4_check_2 = IntVar()
    part4_checkbox_2 = Checkbutton(frame2, text = '파트 4', variable=part4_check_2, command= lambda : checkbox_check(4, 2))
    part4_checkbox_2.place(x = 105, y = 440)

    #관리자 여부 판단
    check_super_2 = IntVar()
    checkbox_super_2 = Checkbutton(frame2, text = '관리자', variable = check_super_2, command= lambda : checkbox_check(5, 2))
    checkbox_super_2.place(x = 70, y = 470)

    #3번 직원 입력 값
    worker3_text = Text(frame2, width = 13, height = 1, font = 12)
    worker3_text.place(x = 50, y = 500)

    #파트 체크박스
    part1_check_3 = IntVar()
    part1_checkbox_3 = Checkbutton(frame2, text = '파트 1', variable=part1_check_3, command= lambda : checkbox_check(1, 3))
    part1_checkbox_3.place(x = 38, y = 525)

    part2_check_3 = IntVar()
    part2_checkbox_3 = Checkbutton(frame2, text = '파트 2', variable=part2_check_3, command= lambda : checkbox_check(2, 3))
    part2_checkbox_3.place(x = 105, y = 525)

    part3_check_3 = IntVar()
    part3_checkbox_3 = Checkbutton(frame2, text = '파트 3', variable=part3_check_3, command= lambda : checkbox_check(3, 3))
    part3_checkbox_3.place(x = 38, y = 555)

    part4_check_3 = IntVar()
    part4_checkbox_3 = Checkbutton(frame2, text = '파트 4', variable=part4_check_3, command= lambda : checkbox_check(4, 3))
    part4_checkbox_3.place(x = 105, y = 555)

    #관리자 여부 판단
    check_super_3 = IntVar()
    checkbox_super_3 = Checkbutton(frame2, text = '관리자', variable = check_super_3, command= lambda : checkbox_check(5, 3))
    checkbox_super_3.place(x = 70, y = 585)

    #4번 직원 입력 값
    worker4_text = Text(frame2, width = 13, height = 1, font = 12)
    worker4_text.place(x = 50, y = 615)

    #파트 체크박스
    part1_check_4 = IntVar()
    part1_checkbox_4 = Checkbutton(frame2, text = '파트 1', variable=part1_check_4, command= lambda : checkbox_check(1, 4))
    part1_checkbox_4.place(x = 38, y = 640)

    part2_check_4 = IntVar()
    part2_checkbox_4 = Checkbutton(frame2, text = '파트 2', variable=part2_check_4, command= lambda : checkbox_check(2, 4))
    part2_checkbox_4.place(x = 105, y = 640)

    part3_check_4 = IntVar()
    part3_checkbox_4 = Checkbutton(frame2, text = '파트 3', variable=part3_check_4, command= lambda : checkbox_check(3, 4))
    part3_checkbox_4.place(x = 38, y = 670)

    part4_check_4 = IntVar()
    part4_checkbox_4 = Checkbutton(frame2, text = '파트 4', variable=part4_check_4, command= lambda : checkbox_check(4, 4))
    part4_checkbox_4.place(x = 105, y = 670)

    #관리자 여부 판단
    check_super_4 = IntVar()
    checkbox_super_4 = Checkbutton(frame2, text = '관리자', variable = check_super_4, command= lambda : checkbox_check(5, 4))
    checkbox_super_4.place(x = 70, y = 700)

    #5번 직원 입력 값
    worker5_text = Text(frame2, width = 13, height = 1, font = 12)
    worker5_text.place(x = 200, y = 270)

    #파트 체크박스
    part1_check_5 = IntVar()
    part1_checkbox_5 = Checkbutton(frame2, text = '파트 1', variable=part1_check_5, command= lambda : checkbox_check(1, 5))
    part1_checkbox_5.place(x = 188, y = 295)

    part2_check_5 = IntVar()
    part2_checkbox_5 = Checkbutton(frame2, text = '파트 2', variable=part2_check_5, command= lambda : checkbox_check(2, 5))
    part2_checkbox_5.place(x = 255, y = 295)

    part3_check_5 = IntVar()
    part3_checkbox_5 = Checkbutton(frame2, text = '파트 3', variable=part3_check_5, command= lambda : checkbox_check(3, 5))
    part3_checkbox_5.place(x = 188, y = 325)

    part4_check_5 = IntVar()
    part4_checkbox_5 = Checkbutton(frame2, text = '파트 4', variable=part4_check_5, command= lambda : checkbox_check(4, 5))
    part4_checkbox_5.place(x = 255, y = 325)

    #관리자 여부 판단
    check_super_5 = IntVar()
    checkbox_super_5 = Checkbutton(frame2, text = '관리자', variable = check_super_5, command= lambda : checkbox_check(5, 5))
    checkbox_super_5.place(x = 220, y = 355)

    #6번 직원 입력 값
    worker6_text = Text(frame2, width = 13, height = 1, font = 12)
    worker6_text.place(x = 200, y = 385)

    #파트 체크박스
    part1_check_6 = IntVar()
    part1_checkbox_6 = Checkbutton(frame2, text = '파트 1', variable= part1_check_6, command= lambda : checkbox_check(1, 6))
    part1_checkbox_6.place(x = 188, y = 410)

    part2_check_6 = IntVar()
    part2_checkbox_6 = Checkbutton(frame2, text = '파트 2', variable=part2_check_6, command= lambda : checkbox_check(2, 6))
    part2_checkbox_6.place(x = 255, y = 410)

    part3_check_6 = IntVar()
    part3_checkbox_6 = Checkbutton(frame2, text = '파트 3', variable=part3_check_6, command= lambda : checkbox_check(3, 6))
    part3_checkbox_6.place(x = 188, y = 440)

    part4_check_6 = IntVar()
    part4_checkbox_6 = Checkbutton(frame2, text = '파트 4', variable=part4_check_6, command= lambda : checkbox_check(4, 6))
    part4_checkbox_6.place(x = 255, y = 440)

    #관리자 여부 판단
    check_super_6 = IntVar()
    checkbox_super_6 = Checkbutton(frame2, text = '관리자', variable = check_super_6, command= lambda : checkbox_check(5, 6))
    checkbox_super_6.place(x = 220, y = 470)

    #7번 직원 입력 값
    worker7_text = Text(frame2, width = 13, height = 1, font = 12)
    worker7_text.place(x = 200, y = 500)

    #파트 체크박스
    part1_check_7 = IntVar()
    part1_checkbox_7 = Checkbutton(frame2, text = '파트 1', variable=part1_check_7, command= lambda : checkbox_check(1, 7))
    part1_checkbox_7.place(x = 188, y = 525)

    part2_check_7 = IntVar()
    part2_checkbox_7 = Checkbutton(frame2, text = '파트 2', variable=part2_check_7, command= lambda : checkbox_check(2, 7))
    part2_checkbox_7.place(x = 255, y = 525)

    part3_check_7 = IntVar()
    part3_checkbox_7 = Checkbutton(frame2, text = '파트 3', variable=part3_check_7, command= lambda : checkbox_check(3, 7))
    part3_checkbox_7.place(x = 188, y = 555)

    part4_check_7 = IntVar()
    part4_checkbox_7 = Checkbutton(frame2, text = '파트 4', variable=part4_check_7, command= lambda : checkbox_check(4, 7))
    part4_checkbox_7.place(x = 255, y = 555)

    #관리자 여부 판단
    check_super_7 = IntVar()
    checkbox_super_7 = Checkbutton(frame2, text = '관리자', variable = check_super_7, command= lambda : checkbox_check(5, 7))
    checkbox_super_7.place(x = 220, y = 585)

    #8번 직원 입력 값
    worker8_text = Text(frame2, width = 13, height = 1, font = 12)
    worker8_text.place(x = 200, y = 615)

    #파트 체크박스
    part1_check_8 = IntVar()
    part1_checkbox_8 = Checkbutton(frame2, text = '파트 1', variable=part1_check_8, command= lambda : checkbox_check(1, 8))
    part1_checkbox_8.place(x = 188, y = 640)

    part2_check_8 = IntVar()
    part2_checkbox_8 = Checkbutton(frame2, text = '파트 2', variable=part2_check_8, command= lambda : checkbox_check(2, 8))
    part2_checkbox_8.place(x = 255, y = 640)

    part3_check_8 = IntVar()
    part3_checkbox_8 = Checkbutton(frame2, text = '파트 3', variable=part3_check_8, command= lambda : checkbox_check(3, 8))
    part3_checkbox_8.place(x = 188, y = 670)

    part4_check_8 = IntVar()
    part4_checkbox_8 = Checkbutton(frame2, text = '파트 4', variable=part4_check_8, command= lambda : checkbox_check(4, 8))
    part4_checkbox_8.place(x = 255, y = 670)

    #관리자 여부 판단
    check_super_8 = IntVar()
    checkbox_super_8 = Checkbutton(frame2, text = '관리자', variable = check_super_8, command= lambda : checkbox_check(5, 8))
    checkbox_super_8.place(x = 220, y = 700)

    #9번 직원 입력 값
    worker9_text = Text(frame2, width = 13, height = 1, font = 12)
    worker9_text.place(x = 350, y = 270)

    #파트 체크박스
    part1_check_9 = IntVar()
    part1_checkbox_9 = Checkbutton(frame2, text = '파트 1', variable=part1_check_9, command= lambda : checkbox_check(1, 9))
    part1_checkbox_9.place(x = 328, y = 295)

    part2_check_9 = IntVar()
    part2_checkbox_9 = Checkbutton(frame2, text = '파트 2', variable=part2_check_9, command= lambda : checkbox_check(2, 9))
    part2_checkbox_9.place(x = 405, y = 295)

    part3_check_9 = IntVar()
    part3_checkbox_9 = Checkbutton(frame2, text = '파트 3', variable=part3_check_9, command= lambda : checkbox_check(3, 9))
    part3_checkbox_9.place(x = 328, y = 325)

    part4_check_9 = IntVar()
    part4_checkbox_9 = Checkbutton(frame2, text = '파트 4', variable=part4_check_9, command= lambda : checkbox_check(4, 9))
    part4_checkbox_9.place(x = 405, y = 325)

    #관리자 여부 판단
    check_super_9 = IntVar()
    checkbox_super_9 = Checkbutton(frame2, text = '관리자', variable = check_super_9, command= lambda : checkbox_check(5, 9))
    checkbox_super_9.place(x = 370, y = 355)

    #10번 직원 입력 값
    worker10_text = Text(frame2, width = 13, height = 1, font = 12)
    worker10_text.place(x = 350, y = 385)

    #파트 체크박스
    part1_check_10 = IntVar()
    part1_checkbox_10 = Checkbutton(frame2, text = '파트 1', variable=part1_check_10, command= lambda : checkbox_check(1, 10))
    part1_checkbox_10.place(x = 328, y = 410)

    part2_check_10 = IntVar()
    part2_checkbox_10 = Checkbutton(frame2, text = '파트 2', variable=part2_check_10, command= lambda : checkbox_check(2, 10))
    part2_checkbox_10.place(x = 405, y = 410)

    part3_check_10 = IntVar()
    part3_checkbox_10 = Checkbutton(frame2, text = '파트 3', variable=part3_check_10, command= lambda : checkbox_check(3, 10))
    part3_checkbox_10.place(x = 328, y = 440)

    part4_check_10 = IntVar()
    part4_checkbox_10 = Checkbutton(frame2, text = '파트 4', variable=part4_check_10, command= lambda : checkbox_check(4, 10))
    part4_checkbox_10.place(x = 405, y = 440)

    #관리자 여부 판단
    check_super_10 = IntVar()
    checkbox_super_10 = Checkbutton(frame2, text = '관리자', variable = check_super_10, command= lambda : checkbox_check(5, 10))
    checkbox_super_10.place(x = 370, y = 470)

    #11번 직원 입력 값
    worker11_text = Text(frame2, width = 13, height = 1, font = 12)
    worker11_text.place(x = 350, y = 500)

    #파트 체크박스
    part1_check_11 = IntVar()
    part1_checkbox_11 = Checkbutton(frame2, text = '파트 1', variable=part1_check_11, command= lambda : checkbox_check(1, 11))
    part1_checkbox_11.place(x = 328, y = 525)

    part2_check_11 = IntVar()
    part2_checkbox_11 = Checkbutton(frame2, text = '파트 2', variable=part2_check_11, command= lambda : checkbox_check(2, 11))
    part2_checkbox_11.place(x = 405, y = 525)

    part3_check_11 = IntVar()
    part3_checkbox_11 = Checkbutton(frame2, text = '파트 3', variable=part3_check_11, command= lambda : checkbox_check(3, 11))
    part3_checkbox_11.place(x = 328, y = 555)

    part4_check_11 = IntVar()
    part4_checkbox_11 = Checkbutton(frame2, text = '파트 4', variable=part4_check_11, command= lambda : checkbox_check(4, 11))
    part4_checkbox_11.place(x = 405, y = 555)

    #관리자 여부 판단
    check_super_11 = IntVar()
    checkbox_super_11 = Checkbutton(frame2, text = '관리자', variable = check_super_11, command= lambda : checkbox_check(5, 11))
    checkbox_super_11.place(x = 370, y = 585)

    #12번 직원 입력 값
    worker12_text = Text(frame2, width = 13, height = 1, font = 12)
    worker12_text.place(x = 350, y = 615)

    #파트 체크박스
    part1_check_12 = IntVar()
    part1_checkbox_12 = Checkbutton(frame2, text = '파트 1', variable=part1_check_12, command= lambda : checkbox_check(1, 12))
    part1_checkbox_12.place(x = 328, y = 640)

    part2_check_12 = IntVar()
    part2_checkbox_12 = Checkbutton(frame2, text = '파트 2', variable=part2_check_12, command= lambda : checkbox_check(2, 12))
    part2_checkbox_12.place(x = 405, y = 640)

    part3_check_12 = IntVar()
    part3_checkbox_12 = Checkbutton(frame2, text = '파트 3', variable=part3_check_12, command= lambda : checkbox_check(3, 12))
    part3_checkbox_12.place(x = 328, y = 670)

    part4_check_12 = IntVar()
    part4_checkbox_12 = Checkbutton(frame2, text = '파트 4', variable=part4_check_12, command= lambda : checkbox_check(4, 12))
    part4_checkbox_12.place(x = 405, y = 670)

    #관리자 여부 판단
    check_super_12 = IntVar()
    checkbox_super_12 = Checkbutton(frame2, text = '관리자', variable = check_super_12, command= lambda : checkbox_check(5, 12))
    checkbox_super_12.place(x = 370, y = 700)

    #13번 직원 입력 값
    worker13_text = Text(frame2, width = 13, height = 1, font = 12)
    worker13_text.place(x = 500, y = 270)

    #파트 체크박스
    part1_check_13 = IntVar()
    part1_checkbox_13 = Checkbutton(frame2, text = '파트 1', variable=part1_check_13, command= lambda : checkbox_check(1, 13))
    part1_checkbox_13.place(x = 478, y = 295)

    part2_check_13 = IntVar()
    part2_checkbox_13 = Checkbutton(frame2, text = '파트 2', variable=part2_check_13, command= lambda : checkbox_check(2, 13))
    part2_checkbox_13.place(x = 555, y = 295)

    part3_check_13 = IntVar()
    part3_checkbox_13 = Checkbutton(frame2, text = '파트 3', variable=part3_check_13, command= lambda : checkbox_check(3, 13))
    part3_checkbox_13.place(x = 478, y = 325)

    part4_check_13 = IntVar()
    part4_checkbox_13 = Checkbutton(frame2, text = '파트 4', variable=part4_check_13, command= lambda : checkbox_check(4, 13))
    part4_checkbox_13.place(x = 555, y = 325)

    #관리자 여부 판단
    check_super_13 = IntVar()
    checkbox_super_13 = Checkbutton(frame2, text = '관리자', variable = check_super_13, command= lambda : checkbox_check(5, 13))
    checkbox_super_13.place(x = 520, y = 355)

    #14번 직원 입력 값
    worker14_text = Text(frame2, width = 13, height = 1, font = 12)
    worker14_text.place(x = 500, y = 385)

    #파트 체크박스
    part1_check_14 = IntVar()
    part1_checkbox_14 = Checkbutton(frame2, text = '파트 1', variable=part1_check_14, command= lambda : checkbox_check(1, 14))
    part1_checkbox_14.place(x = 478, y = 410)

    part2_check_14 = IntVar()
    part2_checkbox_14 = Checkbutton(frame2, text = '파트 2', variable=part2_check_14, command= lambda : checkbox_check(2, 14))
    part2_checkbox_14.place(x = 555, y = 410)

    part3_check_14 = IntVar()
    part3_checkbox_14 = Checkbutton(frame2, text = '파트 3', variable=part3_check_14, command= lambda : checkbox_check(3, 14))
    part3_checkbox_14.place(x = 478, y = 440)

    part4_check_14 = IntVar()
    part4_checkbox_14 = Checkbutton(frame2, text = '파트 4', variable=part4_check_14, command= lambda : checkbox_check(4, 14))
    part4_checkbox_14.place(x = 555, y = 440)

    #관리자 여부 판단
    check_super_14 = IntVar()
    checkbox_super_14 = Checkbutton(frame2, text = '관리자', variable = check_super_14, command= lambda : checkbox_check(5, 14))
    checkbox_super_14.place(x = 520, y = 470)

    #15번 직원 입력 값
    worker15_text = Text(frame2, width = 13, height = 1, font = 12)
    worker15_text.place(x = 500, y = 500)

    #파트 체크박스
    part1_check_15 = IntVar()
    part1_checkbox_15 = Checkbutton(frame2, text = '파트 1', variable=part1_check_15, command= lambda : checkbox_check(1, 15))
    part1_checkbox_15.place(x = 478, y = 525)

    part2_check_15 = IntVar()
    part2_checkbox_15 = Checkbutton(frame2, text = '파트 2', variable=part2_check_15, command= lambda : checkbox_check(2, 15))
    part2_checkbox_15.place(x = 555, y = 525)

    part3_check_15 = IntVar()
    part3_checkbox_15 = Checkbutton(frame2, text = '파트 3', variable=part3_check_15, command= lambda : checkbox_check(3, 15))
    part3_checkbox_15.place(x = 478, y = 555)

    part4_check_15 = IntVar()
    part4_checkbox_15 = Checkbutton(frame2, text = '파트 4', variable=part4_check_15, command= lambda : checkbox_check(4, 15))
    part4_checkbox_15.place(x = 555, y = 555)

    #관리자 여부 판단
    check_super_15 = IntVar()
    checkbox_super_15 = Checkbutton(frame2, text = '관리자', variable = check_super_15, command= lambda : checkbox_check(5, 15))
    checkbox_super_15.place(x = 520, y = 585)

    #16번 직원 입력 값
    worker16_text = Text(frame2, width = 13, height = 1, font = 12)
    worker16_text.place(x = 500, y = 615)

    #파트 체크박스
    part1_check_16 = IntVar()
    part1_checkbox_16 = Checkbutton(frame2, text = '파트 1', variable=part1_check_16, command= lambda : checkbox_check(1, 16))
    part1_checkbox_16.place(x = 478, y = 640)

    part2_check_16 = IntVar()
    part2_checkbox_16 = Checkbutton(frame2, text = '파트 2', variable=part2_check_16, command= lambda : checkbox_check(2, 16))
    part2_checkbox_16.place(x = 555, y = 640)

    part3_check_16 = IntVar()
    part3_checkbox_16 = Checkbutton(frame2, text = '파트 3', variable=part3_check_16, command= lambda : checkbox_check(3, 16))
    part3_checkbox_16.place(x = 478, y = 670)

    part4_check_16 = IntVar()
    part4_checkbox_16 = Checkbutton(frame2, text = '파트 4', variable=part4_check_16, command= lambda : checkbox_check(4, 16))
    part4_checkbox_16.place(x = 555, y = 670)

    #관리자 여부 판단
    check_super_16 = IntVar()
    checkbox_super_16 = Checkbutton(frame2, text = '관리자', variable = check_super_16, command= lambda : checkbox_check(5, 16))
    checkbox_super_16.place(x = 520, y = 700)

    #종료 버튼
    exit_button = Button(frame2, text = '종료', command = save_exit, width = 10, bg = 'white', height = 2, padx = 10, pady = 10)
    exit_button.place(x = 500, y = 30)
    #####################################################
    ####################UI 작성 종료######################
    #####################################################

    tk.mainloop()

