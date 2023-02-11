from tkinter import *
import pickle
import random

global count_worker
global max_worker
global mon_part1
global mon_part2
global mon_part3
global mon_part4
global tue_part1
global tue_part2
global tue_part3
global tue_part4
global wed_part1
global wed_part2
global wed_part3
global wed_part4
global thu_part1
global thu_part2
global thu_part3
global thu_part4
global fri_part1
global fri_part2
global fri_part3
global fri_part4
global sat_part1
global sat_part2
global sat_part3
global sat_part4
global sun_part1
global sun_part2
global sun_part3
global sun_part4

#저장 후 종료
def save_exit():
    exit()

#시간표 조회 시작
def get_result():
    global count_worker
    global max_worker
    global mon_part1
    global mon_part2
    global mon_part3
    global mon_part4
    global tue_part1
    global tue_part2
    global tue_part3
    global tue_part4
    global wed_part1
    global wed_part2
    global wed_part3
    global wed_part4
    global thu_part1
    global thu_part2
    global thu_part3
    global thu_part4
    global fri_part1
    global fri_part2
    global fri_part3
    global fri_part4
    global sat_part1
    global sat_part2
    global sat_part3
    global sat_part4
    global sun_part1
    global sun_part2
    global sun_part3
    global sun_part4

    people = int(max_worker.get("1.0", "end")) # 파트 당 최저 근무 인원
    people -= 1 # 아래 계산식 오류로 인해 조정

    count = int(count_worker.get("1.0", "end")) #주당 최대 근무 회수

    #파일 파싱 시작
    part_file = open("part_info", "rb")
    part_info = pickle.load(part_file)
    part_file.close()

    worker_file = open("worker_info", "rb")
    worker_info = pickle.load(worker_file)
    worker_file.close()

    is_super = False
    try:
        super_file = open("super_info", "rb")
        super_info = pickle.load(super_file)
        super_file.close()
        is_super = True
    except:
        print("")

    #주당 근무 회수 체크
    work_count = {}
    for i in range(1, len(worker_info)):
        work_count[worker_info[i][0]] = 0

    work_count_super = {}
    for i in range(1, len(super_info)):
        work_count_super[super_info[i][0]] = 0

    part1_mon = []
    part2_mon = []
    part3_mon = []
    part4_mon = []
    part1_tue = []
    part2_tue = []
    part3_tue = []
    part4_tue = []
    part1_wed = []
    part2_wed = []
    part3_wed = []
    part4_wed = []
    part1_thr = []
    part2_thr = []
    part3_thr = []
    part4_thr = []
    part1_fri = []
    part2_fri = []
    part3_fri = []
    part4_fri = []
    part1_sat = []
    part2_sat = []
    part3_sat = []
    part4_sat = []
    part1_sun = []
    part2_sun = []
    part3_sun = []
    part4_sun = []

    part1_mon_super = []
    part2_mon_super = []
    part3_mon_super = []
    part4_mon_super = []
    part1_tue_super = []
    part2_tue_super = []
    part3_tue_super = []
    part4_tue_super = []
    part1_wed_super = []
    part2_wed_super = []
    part3_wed_super = []
    part4_wed_super = []
    part1_thr_super = []
    part2_thr_super = []
    part3_thr_super = []
    part4_thr_super = []
    part1_fri_super = []
    part2_fri_super = []
    part3_fri_super = []
    part4_fri_super = []
    part1_sat_super = []
    part2_sat_super = []
    part3_sat_super = []
    part4_sat_super = []
    part1_sun_super = []
    part2_sun_super = []
    part3_sun_super = []
    part4_sun_super = []

    part1_max = 0
    part2_max = 0
    part3_max = 0
    part4_max = 0


    for i in  range(1, len(worker_info)):
        if worker_info[i][1] == 1:
            part1_max += 1

        if worker_info[i][2] == 1:
            part2_max += 1

        if worker_info[i][3] == 1:
            part3_max += 1

        if worker_info[i][4] == 1:
            part4_max += 1

    #아르바이트 시간표 작성 시작
    #파트 1
    #월
    while True:
        check = part1_max - len(part1_mon)
        if (len(part1_mon) == people) or check == 0:
            break
        #관리자 시작
        if is_super and len(part1_mon_super) == 0:
            candidate_super = []
            for i in range(1, len(super_info)):
                if super_info[i][1] == 1 and super_info[i][0] not in part1_mon_super and super_info[i][0] not in part2_mon_super and super_info[i][0] not in part3_mon_super and super_info[i][0] not in part4_mon_super:
                    candidate_super.append(super_info[i][0])
            get_super = random.randint(0, len(candidate_super) - 1)
            part1_mon_super.append(candidate_super[get_super])
            work_count_super[candidate_super[get_super]] += 1

        #일반 아르바이트 생 시작
        #후보자 선정
        candidate = []
        for i in range(1, len(worker_info)):
            if worker_info[i][1] == 1 and worker_info[i][0] not in part1_mon and worker_info[i][0] not in part2_mon and worker_info[i][0] not in part3_mon and worker_info[i][0] not in part4_mon \
                    and work_count[worker_info[i][0]] <= count:
                candidate.append(worker_info[i][0])

        get_worker = random.randint(0, len(candidate) - 1)
        part1_mon.append(candidate[get_worker])
        work_count[candidate[get_worker]] += 1
    #화
    while True:
        check = part1_max - len(part1_tue)
        if (len(part1_tue) == people) or check == 0:
            break
        #관리자 시작
        if is_super and len(part1_tue_super) == 0:
            candidate_super = []
            for i in range(1, len(super_info)):
                if super_info[i][1] == 1 and super_info[i][0] not in part1_tue_super and super_info[i][0] not in part2_tue_super and super_info[i][0] not in part3_tue_super and super_info[i][0] not in part4_tue_super:
                    candidate_super.append(super_info[i][0])
            get_super = random.randint(0, len(candidate_super) - 1)
            part1_tue_super.append(candidate_super[get_super])
            work_count_super[candidate_super[get_super]] += 1

        #후보자 선정
        candidate = []
        for i in range(1, len(worker_info)):
            if worker_info[i][1] == 1 and worker_info[i][0] not in part1_tue and worker_info[i][0] not in part2_tue and worker_info[i][0] not in part3_tue and worker_info[i][0] not in part4_tue \
                    and work_count[worker_info[i][0]] <= count:
                candidate.append(worker_info[i][0])

        get_worker = random.randint(0, len(candidate) - 1)
        part1_tue.append(candidate[get_worker])
        work_count[candidate[get_worker]] += 1

    #수
    while True:
        check = part1_max - len(part1_wed)
        if (len(part1_wed) == people) or check == 0:
            break
        #관리자 시작
        if is_super and len(part1_wed_super) == 0:
            candidate_super = []
            for i in range(1, len(super_info)):
                if super_info[i][1] == 1 and super_info[i][0] not in part1_wed_super and super_info[i][0] not in part2_wed_super and super_info[i][0] not in part3_wed_super and super_info[i][0] not in part4_wed_super:
                    candidate_super.append(super_info[i][0])
            get_super = random.randint(0, len(candidate_super) - 1)
            part1_wed_super.append(candidate_super[get_super])
            work_count_super[candidate_super[get_super]] += 1

        #후보자 선정
        candidate = []
        for i in range(1, len(worker_info)):
            if worker_info[i][1] == 1 and worker_info[i][0] not in part1_wed and worker_info[i][0] not in part2_wed and worker_info[i][0] not in part3_wed and worker_info[i][0] not in part4_wed \
                    and work_count[worker_info[i][0]] <= count:
                candidate.append(worker_info[i][0])

        get_worker = random.randint(0, len(candidate) - 1)
        part1_wed.append(candidate[get_worker])
        work_count[candidate[get_worker]] += 1

        #목
    while True:
        check = part1_max - len(part1_thr)
        if (len(part1_thr) == people) or check == 0:
            break
        #관리자 시작
        if is_super and len(part1_thr_super) == 0:
            candidate_super = []
            for i in range(1, len(super_info)):
                if super_info[i][1] == 1 and super_info[i][0] not in part1_thr_super and super_info[i][0] not in part2_thr_super and super_info[i][0] not in part3_thr_super and super_info[i][0] not in part4_thr_super:
                    candidate_super.append(super_info[i][0])
            get_super = random.randint(0, len(candidate_super) - 1)
            part1_thr_super.append(candidate_super[get_super])
            work_count_super[candidate_super[get_super]] += 1

        #후보자 선정
        candidate = []
        for i in range(1, len(worker_info)):
            if worker_info[i][1] == 1 and worker_info[i][0] not in part1_thr and worker_info[i][0] not in part2_thr and worker_info[i][0] not in part3_thr and worker_info[i][0] not in part4_thr \
                    and work_count[worker_info[i][0]] <= count:
                candidate.append(worker_info[i][0])

        get_worker = random.randint(0, len(candidate) - 1)
        part1_thr.append(candidate[get_worker])
        work_count[candidate[get_worker]] += 1

        #금
    while True:
        check = part1_max - len(part1_fri)
        if (len(part1_fri) == people) or check == 0:
            break
        #관리자 시작
        if is_super and len(part1_fri_super) == 0:
            candidate_super = []
            for i in range(1, len(super_info)):
                if super_info[i][1] == 1 and super_info[i][0] not in part1_fri_super and super_info[i][0] not in part2_fri_super and super_info[i][0] not in part3_fri_super and super_info[i][0] not in part4_fri_super:
                    candidate_super.append(super_info[i][0])
            get_super = random.randint(0, len(candidate_super) - 1)
            part1_fri_super.append(candidate_super[get_super])
            work_count_super[candidate_super[get_super]] += 1

        #후보자 선정
        candidate = []
        for i in range(1, len(worker_info)):
            if worker_info[i][1] == 1 and worker_info[i][0] not in part1_fri and worker_info[i][0] not in part2_fri and worker_info[i][0] not in part3_fri and worker_info[i][0] not in part4_fri \
                    and work_count[worker_info[i][0]] <= count:
                candidate.append(worker_info[i][0])

        get_worker = random.randint(0, len(candidate) - 1)
        part1_fri.append(candidate[get_worker])
        work_count[candidate[get_worker]] += 1

        #토
    while True:
        check = part1_max - len(part1_sat)
        if (len(part1_sat) == people) or check == 0:
            break
        #관리자 시작
        if is_super and len(part1_sat_super) == 0:
            candidate_super = []
            for i in range(1, len(super_info)):
                if super_info[i][1] == 1 and super_info[i][0] not in part1_sat_super and super_info[i][0] not in part2_sat_super and super_info[i][0] not in part3_sat_super and super_info[i][0] not in part4_sat_super:
                    candidate_super.append(super_info[i][0])
            get_super = random.randint(0, len(candidate_super) - 1)
            part1_sat_super.append(candidate_super[get_super])
            work_count_super[candidate_super[get_super]] += 1

        #후보자 선정
        candidate = []
        for i in range(1, len(worker_info)):
            if worker_info[i][1] == 1 and worker_info[i][0] not in part1_sat and worker_info[i][0] not in part2_sat and worker_info[i][0] not in part3_sat and worker_info[i][0] not in part4_sat \
                    and work_count[worker_info[i][0]] <= count:
                candidate.append(worker_info[i][0])

        get_worker = random.randint(0, len(candidate) - 1)
        part1_sat.append(candidate[get_worker])
        work_count[candidate[get_worker]] += 1

        #일
    while True:
        check = part1_max - len(part1_sun)
        if (len(part1_sun) == people) or check == 0:
            break
        #관리자 시작
        if is_super and len(part1_sun_super) == 0:
            candidate_super = []
            for i in range(1, len(super_info)):
                if super_info[i][1] == 1 and super_info[i][0] not in part1_sun_super and super_info[i][0] not in part2_sun_super and super_info[i][0] not in part3_sun_super and super_info[i][0] not in part4_sun_super:
                    candidate_super.append(super_info[i][0])
            get_super = random.randint(0, len(candidate_super) - 1)
            part1_sun_super.append(candidate_super[get_super])
            work_count_super[candidate_super[get_super]] += 1

        #후보자 선정
        candidate = []
        for i in range(1, len(worker_info)):
            if worker_info[i][1] == 1 and worker_info[i][0] not in part1_sun and worker_info[i][0] not in part2_sun and worker_info[i][0] not in part3_sun and worker_info[i][0] not in part4_sun \
                    and work_count[worker_info[i][0]] <= count:
                candidate.append(worker_info[i][0])

        get_worker = random.randint(0, len(candidate) - 1)
        part1_sun.append(candidate[get_worker])
        work_count[candidate[get_worker]] += 1

    #파트 2
    if len(part_info) >= 3:
        #월
        while True:
            check = part2_max - len(part2_mon)
            if (len(part2_mon) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part2_mon_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][2] == 1 and super_info[i][0] not in part1_mon_super and super_info[i][0] not in part2_mon_super and super_info[i][0] not in part3_mon_super and super_info[i][0] not in part4_mon_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part2_mon_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][2] == 1 and worker_info[i][0] not in part1_mon and worker_info[i][0] not in part2_mon and worker_info[i][0] not in part3_mon and worker_info[i][0] not in part4_mon \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part2_mon.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #화
        while True:
            check = part2_max - len(part2_tue)
            if (len(part2_tue) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part2_tue_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][2] == 1 and super_info[i][0] not in part1_tue_super and super_info[i][0] not in part2_tue_super and super_info[i][0] not in part3_tue_super and super_info[i][0] not in part4_tue_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part2_tue_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][2] == 1 and worker_info[i][0] not in part1_tue and worker_info[i][0] not in part2_tue and worker_info[i][0] not in part3_tue and worker_info[i][0] not in part4_tue \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part2_tue.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #수
        while True:
            check = part2_max - len(part2_wed)
            if (len(part2_wed) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part2_wed_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][2] == 1 and super_info[i][0] not in part1_wed_super and super_info[i][0] not in part2_wed_super and super_info[i][0] not in part3_wed_super and super_info[i][0] not in part4_wed_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part2_wed_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][2] == 1 and worker_info[i][0] not in part1_wed and worker_info[i][0] not in part2_wed and worker_info[i][0] not in part3_wed and worker_info[i][0] not in part4_wed \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part2_wed.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #목
        while True:
            check = part2_max - len(part2_thr)
            if (len(part2_thr) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part2_thr_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][2] == 1 and super_info[i][0] not in part1_thr_super and super_info[i][0] not in part2_thr_super and super_info[i][0] not in part3_thr_super and super_info[i][0] not in part4_thr_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part2_thr_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][2] == 1 and worker_info[i][0] not in part1_thr and worker_info[i][0] not in part2_thr and worker_info[i][0] not in part3_thr and worker_info[i][0] not in part4_thr \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part2_thr.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #금
        while True:
            check = part2_max - len(part2_fri)
            if (len(part2_fri) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part2_fri_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][2] == 1 and super_info[i][0] not in part1_fri_super and super_info[i][0] not in part2_fri_super and super_info[i][0] not in part3_fri_super and super_info[i][0] not in part4_fri_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part2_fri_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][2] == 1 and worker_info[i][0] not in part1_fri and worker_info[i][0] not in part2_fri and worker_info[i][0] not in part3_fri and worker_info[i][0] not in part4_fri \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part2_fri.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #토
        while True:
            check = part2_max - len(part2_sat)
            if (len(part2_sat) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part2_sat_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][2] == 1 and super_info[i][0] not in part1_sat_super and super_info[i][0] not in part2_sat_super and super_info[i][0] not in part3_sat_super and super_info[i][0] not in part4_sat_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part2_sat_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][2] == 1 and worker_info[i][0] not in part1_sat and worker_info[i][0] not in part2_sat and worker_info[i][0] not in part3_sat and worker_info[i][0] not in part4_sat \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part2_sat.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #일
        while True:
            check = part2_max - len(part2_sun)
            if (len(part2_sun) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part2_sun_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][2] == 1 and super_info[i][0] not in part1_sun_super and super_info[i][0] not in part2_sun_super and super_info[i][0] not in part3_sun_super and super_info[i][0] not in part4_sun_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part2_sun_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][2] == 1 and worker_info[i][0] not in part1_sun and worker_info[i][0] not in part2_sun and worker_info[i][0] not in part3_sun and worker_info[i][0] not in part4_sun \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part2_sun.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1


    #파트 3
    if len(part_info) >= 4:
        #월
        while True:
            check = part3_max - len(part3_mon)
            if (len(part3_mon) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part3_mon_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][3] == 1 and super_info[i][0] not in part1_mon_super and super_info[i][0] not in part2_mon_super and super_info[i][0] not in part3_mon_super and super_info[i][0] not in part4_mon_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part3_mon_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][3] == 1 and worker_info[i][0] not in part1_mon and worker_info[i][0] not in part2_mon and worker_info[i][0] not in part3_mon and worker_info[i][0] not in part4_mon \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part3_mon.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #화
        while True:
            check = part3_max - len(part3_tue)
            if (len(part3_tue) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part3_tue_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][3] == 1 and super_info[i][0] not in part1_tue_super and super_info[i][0] not in part2_tue_super and super_info[i][0] not in part3_tue_super and super_info[i][0] not in part4_tue_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part3_tue_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][3] == 1 and worker_info[i][0] not in part1_tue and worker_info[i][0] not in part2_tue and worker_info[i][0] not in part3_tue and worker_info[i][0] not in part4_tue \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part3_tue.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #수
        while True:
            check = part3_max - len(part3_wed)
            if (len(part3_wed) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part3_wed_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][3] == 1 and super_info[i][0] not in part1_wed_super and super_info[i][0] not in part2_wed_super and super_info[i][0] not in part3_wed_super and super_info[i][0] not in part4_wed_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part3_wed_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][3] == 1 and worker_info[i][0] not in part1_wed and worker_info[i][0] not in part2_wed and worker_info[i][0] not in part3_wed and worker_info[i][0] not in part4_wed \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part3_wed.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #목
        while True:
            check = part3_max - len(part3_thr)
            if (len(part3_thr) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part3_thr_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][3] == 1 and super_info[i][0] not in part1_thr_super and super_info[i][0] not in part2_thr_super and super_info[i][0] not in part3_thr_super and super_info[i][0] not in part4_thr_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part3_thr_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][3] == 1 and worker_info[i][0] not in part1_thr and worker_info[i][0] not in part2_thr and worker_info[i][0] not in part3_thr and worker_info[i][0] not in part4_thr \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part3_thr.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #금
        while True:
            check = part3_max - len(part3_fri)
            if (len(part3_fri) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part3_fri_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][3] == 1 and super_info[i][0] not in part1_fri_super and super_info[i][0] not in part2_fri_super and super_info[i][0] not in part3_fri_super and super_info[i][0] not in part4_fri_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part3_fri_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][3] == 1 and worker_info[i][0] not in part1_fri and worker_info[i][0] not in part2_fri and worker_info[i][0] not in part3_fri and worker_info[i][0] not in part4_fri \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part3_fri.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #토
        while True:
            check = part3_max - len(part3_sat)
            if (len(part3_sat) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part3_sat_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][3] == 1 and super_info[i][0] not in part1_sat_super and super_info[i][0] not in part2_sat_super and super_info[i][0] not in part3_sat_super and super_info[i][0] not in part4_sat_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part3_sat_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][3] == 1 and worker_info[i][0] not in part1_sat and worker_info[i][0] not in part2_sat and worker_info[i][0] not in part3_sat and worker_info[i][0] not in part4_sat \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part3_sat.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #일
        while True:
            check = part3_max - len(part3_sun)
            if (len(part3_sun) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part3_sun_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][3] == 1 and super_info[i][0] not in part1_sun_super and super_info[i][0] not in part2_sun_super and super_info[i][0] not in part3_sun_super and super_info[i][0] not in part4_sun_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part3_sun_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][3] == 1 and worker_info[i][0] not in part1_sun and worker_info[i][0] not in part2_sun and worker_info[i][0] not in part3_sun and worker_info[i][0] not in part4_sun \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part3_sun.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1



    #파트 4
    if len(part_info) >= 5:
        #월
        while True:
            check = part4_max - len(part4_mon)
            if (len(part4_mon) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part4_mon_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][4] == 1 and super_info[i][0] not in part1_mon_super and super_info[i][0] not in part2_mon_super and super_info[i][0] not in part3_mon_super and super_info[i][0] not in part4_mon_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part4_mon_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][4] == 1 and worker_info[i][0] not in part1_mon and worker_info[i][0] not in part2_mon and worker_info[i][0] not in part3_mon and worker_info[i][0] not in part4_mon \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part4_mon.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #화
        while True:
            check = part4_max - len(part4_tue)
            if (len(part4_tue) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part4_tue_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][4] == 1 and super_info[i][0] not in part1_tue_super and super_info[i][0] not in part2_tue_super and super_info[i][0] not in part3_tue_super and super_info[i][0] not in part4_tue_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part4_tue_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][4] == 1 and worker_info[i][0] not in part1_tue and worker_info[i][0] not in part2_tue and worker_info[i][0] not in part3_tue and worker_info[i][0] not in part4_tue \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part4_tue.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #수
        while True:
            check = part4_max - len(part4_wed)
            if (len(part4_wed) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part4_wed_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][4] == 1 and super_info[i][0] not in part1_wed_super and super_info[i][0] not in part2_wed_super and super_info[i][0] not in part3_wed_super and super_info[i][0] not in part4_wed_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part4_wed_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][4] == 1 and worker_info[i][0] not in part1_wed and worker_info[i][0] not in part2_wed and worker_info[i][0] not in part3_wed and worker_info[i][0] not in part4_wed \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part4_wed.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #목
        while True:
            check = part4_max - len(part4_thr)
            if (len(part4_thr) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part4_thr_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][4] == 1 and super_info[i][0] not in part1_thr_super and super_info[i][0] not in part2_thr_super and super_info[i][0] not in part3_thr_super and super_info[i][0] not in part4_thr_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part4_thr_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][4] == 1 and worker_info[i][0] not in part1_thr and worker_info[i][0] not in part2_thr and worker_info[i][0] not in part3_thr and worker_info[i][0] not in part4_thr \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part4_thr.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #금
        while True:
            check = part4_max - len(part4_fri)
            if (len(part4_fri) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part4_fri_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][4] == 1 and super_info[i][0] not in part1_fri_super and super_info[i][0] not in part2_fri_super and super_info[i][0] not in part3_fri_super and super_info[i][0] not in part4_fri_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part4_fri_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][4] == 1 and worker_info[i][0] not in part1_fri and worker_info[i][0] not in part2_fri and worker_info[i][0] not in part3_fri and worker_info[i][0] not in part4_fri \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part4_fri.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #토
        while True:
            check = part4_max - len(part4_sat)
            if (len(part4_sat) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part4_sat_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][4] == 1 and super_info[i][0] not in part1_sat_super and super_info[i][0] not in part2_sat_super and super_info[i][0] not in part3_sat_super and super_info[i][0] not in part4_sat_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part4_sat_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][4] == 1 and worker_info[i][0] not in part1_sat and worker_info[i][0] not in part2_sat and worker_info[i][0] not in part3_sat and worker_info[i][0] not in part4_sat \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part4_sat.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

        #일
        while True:
            check = part4_max - len(part4_sun)
            if (len(part4_sun) == people) or check == 0:
                break
            #관리자 시작
            if is_super and len(part4_sun_super) == 0:
                candidate_super = []
                for i in range(1, len(super_info)):
                    if super_info[i][4] == 1 and super_info[i][0] not in part1_sun_super and super_info[i][0] not in part2_sun_super and super_info[i][0] not in part3_sun_super and super_info[i][0] not in part4_sun_super:
                        candidate_super.append(super_info[i][0])
                get_super = random.randint(0, len(candidate_super) - 1)
                part4_sun_super.append(candidate_super[get_super])
                work_count_super[candidate_super[get_super]] += 1

            #후보자 선정
            candidate = []
            for i in range(1, len(worker_info)):
                if worker_info[i][4] == 1 and worker_info[i][0] not in part1_sun and worker_info[i][0] not in part2_sun and worker_info[i][0] not in part3_sun and worker_info[i][0] not in part4_sun \
                        and work_count[worker_info[i][0]] <= count:
                    candidate.append(worker_info[i][0])

            get_worker = random.randint(0, len(candidate) - 1)
            part4_sun.append(candidate[get_worker])
            work_count[candidate[get_worker]] += 1

    #파트1
    #월
    part1_mon_text = ""
    for i in range(len(part1_mon_super)):
        part1_mon_text += part1_mon_super[i]
        part1_mon_text += '\n'

    for i in range(len(part1_mon)):
        part1_mon_text += part1_mon[i]
        part1_mon_text += '\n'
    mon_part1.insert("1.0", part1_mon_text)


    #화
    part1_tue_text = ""
    for i in range(len(part1_tue_super)):
        part1_tue_text += part1_tue_super[i]
        part1_tue_text += '\n'

    for i in range(len(part1_tue)):
        part1_tue_text += part1_tue[i]
        part1_tue_text += '\n'
    tue_part1.insert("1.0", part1_tue_text)

    #수
    part1_wed_text = ""
    for i in range(len(part1_wed_super)):
        part1_wed_text += part1_wed_super[i]
        part1_wed_text += '\n'

    for i in range(len(part1_wed)):
        part1_wed_text += part1_wed[i]
        part1_wed_text += '\n'
    wed_part1.insert("1.0", part1_wed_text)

    #목
    part1_thr_text = ""
    for i in range(len(part1_thr_super)):
        part1_thr_text += part1_thr_super[i]
        part1_thr_text += '\n'

    for i in range(len(part1_thr)):
        part1_thr_text += part1_thr[i]
        part1_thr_text += '\n'
    thu_part1.insert("1.0", part1_thr_text)

    #금
    part1_fri_text = ""
    for i in range(len(part1_fri_super)):
        part1_fri_text += part1_fri_super[i]
        part1_fri_text += '\n'

    for i in range(len(part1_fri)):
        part1_fri_text += part1_fri[i]
        part1_fri_text += '\n'
    fri_part1.insert("1.0", part1_fri_text)

    #토
    part1_sat_text = ""
    for i in range(len(part1_sat_super)):
        part1_sat_text += part1_sat_super[i]
        part1_sat_text += '\n'

    for i in range(len(part1_sat)):
        part1_sat_text += part1_sat[i]
        part1_sat_text += '\n'
    sat_part1.insert("1.0", part1_sat_text)

    #일
    part1_sun_text = ""
    for i in range(len(part1_sun_super)):
        part1_sun_text += part1_sun_super[i]
        part1_sun_text += '\n'

    for i in range(len(part1_sun)):
        part1_sun_text += part1_sun[i]
        part1_sun_text += '\n'
    sun_part1.insert("1.0", part1_sun_text)

    #파트2
    #월
    part2_mon_text = ""
    for i in range(len(part2_mon_super)):
        part2_mon_text += part2_mon_super[i]
        part2_mon_text += '\n'

    for i in range(len(part2_mon)):
        part2_mon_text += part2_mon[i]
        part2_mon_text += '\n'
    mon_part2.insert("1.0", part2_mon_text)


    #화
    part2_tue_text = ""
    for i in range(len(part2_tue_super)):
        part2_tue_text += part2_tue_super[i]
        part2_tue_text += '\n'

    for i in range(len(part2_tue)):
        part2_tue_text += part2_tue[i]
        part2_tue_text += '\n'
    tue_part2.insert("1.0", part2_tue_text)

    #수
    part2_wed_text = ""
    for i in range(len(part2_wed_super)):
        part2_wed_text += part2_wed_super[i]
        part2_wed_text += '\n'

    for i in range(len(part2_wed)):
        part2_wed_text += part2_wed[i]
        part2_wed_text += '\n'
    wed_part2.insert("1.0", part2_wed_text)

    #목
    part2_thr_text = ""
    for i in range(len(part2_thr_super)):
        part2_thr_text += part2_thr_super[i]
        part2_thr_text += '\n'

    for i in range(len(part2_thr)):
        part2_thr_text += part2_thr[i]
        part2_thr_text += '\n'
    thu_part2.insert("1.0", part2_thr_text)

    #금
    part2_fri_text = ""
    for i in range(len(part2_fri_super)):
        part2_fri_text += part2_fri_super[i]
        part2_fri_text += '\n'

    for i in range(len(part2_fri)):
        part2_fri_text += part2_fri[i]
        part2_fri_text += '\n'
    fri_part2.insert("1.0", part2_fri_text)

    #토
    part2_sat_text = ""
    for i in range(len(part2_sat_super)):
        part2_sat_text += part2_sat_super[i]
        part2_sat_text += '\n'

    for i in range(len(part2_sat)):
        part2_sat_text += part2_sat[i]
        part2_sat_text += '\n'
    sat_part2.insert("1.0", part2_sat_text)

    #일
    part2_sun_text = ""
    for i in range(len(part2_sun_super)):
        part2_sun_text += part2_sun_super[i]
        part2_sun_text += '\n'

    for i in range(len(part2_sun)):
        part2_sun_text += part2_sun[i]
        part2_sun_text += '\n'
    sun_part2.insert("1.0", part2_sun_text)

    #파트3
    #월
    part3_mon_text = ""
    for i in range(len(part3_mon_super)):
        part3_mon_text += part3_mon_super[i]
        part3_mon_text += '\n'

    for i in range(len(part3_mon)):
        part3_mon_text += part3_mon[i]
        part3_mon_text += '\n'
    mon_part3.insert("1.0", part3_mon_text)


    #화
    part3_tue_text = ""
    for i in range(len(part3_tue_super)):
        part3_tue_text += part3_tue_super[i]
        part3_tue_text += '\n'

    for i in range(len(part3_tue)):
        part3_tue_text += part3_tue[i]
        part3_tue_text += '\n'
    tue_part3.insert("1.0", part3_tue_text)

    #수
    part3_wed_text = ""
    for i in range(len(part3_wed_super)):
        part3_wed_text += part3_wed_super[i]
        part3_wed_text += '\n'

    for i in range(len(part3_wed)):
        part3_wed_text += part3_wed[i]
        part3_wed_text += '\n'
    wed_part3.insert("1.0", part3_wed_text)

    #목
    part3_thr_text = ""
    for i in range(len(part3_thr_super)):
        part3_thr_text += part3_thr_super[i]
        part3_thr_text += '\n'

    for i in range(len(part3_thr)):
        part3_thr_text += part3_thr[i]
        part3_thr_text += '\n'
    thu_part3.insert("1.0", part3_thr_text)

    #금
    part3_fri_text = ""
    for i in range(len(part3_fri_super)):
        part3_fri_text += part3_fri_super[i]
        part3_fri_text += '\n'

    for i in range(len(part3_fri)):
        part3_fri_text += part3_fri[i]
        part3_fri_text += '\n'
    fri_part3.insert("1.0", part3_fri_text)

    #토
    part3_sat_text = ""
    for i in range(len(part3_sat_super)):
        part3_sat_text += part3_sat_super[i]
        part3_sat_text += '\n'

    for i in range(len(part3_sat)):
        part3_sat_text += part3_sat[i]
        part3_sat_text += '\n'
    sat_part3.insert("1.0", part3_sat_text)

    #일
    part3_sun_text = ""
    for i in range(len(part3_sun_super)):
        part3_sun_text += part3_sun_super[i]
        part3_sun_text += '\n'

    for i in range(len(part3_sun)):
        part3_sun_text += part3_sun[i]
        part3_sun_text += '\n'
    sun_part3.insert("1.0", part3_sun_text)

    #파트4
    #월
    part4_mon_text = ""
    for i in range(len(part4_mon_super)):
        part4_mon_text += part4_mon_super[i]
        part4_mon_text += '\n'

    for i in range(len(part4_mon)):
        part4_mon_text += part4_mon[i]
        part4_mon_text += '\n'
    mon_part4.insert("1.0", part4_mon_text)


    #화
    part4_tue_text = ""
    for i in range(len(part4_tue_super)):
        part4_tue_text += part4_tue_super[i]
        part4_tue_text += '\n'

    for i in range(len(part4_tue)):
        part4_tue_text += part4_tue[i]
        part4_tue_text += '\n'
    tue_part4.insert("1.0", part4_tue_text)

    #수
    part4_wed_text = ""
    for i in range(len(part4_wed_super)):
        part4_wed_text += part4_wed_super[i]
        part4_wed_text += '\n'

    for i in range(len(part4_wed)):
        part4_wed_text += part4_wed[i]
        part4_wed_text += '\n'
    wed_part4.insert("1.0", part4_wed_text)

    #목
    part4_thr_text = ""
    for i in range(len(part4_thr_super)):
        part4_thr_text += part4_thr_super[i]
        part4_thr_text += '\n'

    for i in range(len(part4_thr)):
        part4_thr_text += part4_thr[i]
        part4_thr_text += '\n'
    thu_part4.insert("1.0", part4_thr_text)

    #금
    part4_fri_text = ""
    for i in range(len(part3_fri_super)):
        part4_fri_text += part3_fri_super[i]
        part4_fri_text += '\n'

    for i in range(len(part4_fri)):
        part4_fri_text += part4_fri[i]
        part4_fri_text += '\n'
    fri_part4.insert("1.0", part4_fri_text)

    #토
    part4_sat_text = ""
    for i in range(len(part4_sat_super)):
        part4_sat_text += part4_sat_super[i]
        part4_sat_text += '\n'

    for i in range(len(part4_sat)):
        part4_sat_text += part4_sat[i]
        part4_sat_text += '\n'
    sat_part4.insert("1.0", part4_sat_text)

    #일
    part4_sun_text = ""
    for i in range(len(part4_sun_super)):
        part4_sun_text += part4_sun_super[i]
        part4_sun_text += '\n'

    for i in range(len(part4_sun)):
        part4_sun_text += part4_sun[i]
        part4_sun_text += '\n'
    sun_part4.insert("1.0", part4_sun_text)

    stat_file = open("stat", "wb")
    pickle.dump(work_count, stat_file)
    stat_file.close()

    stat_super_file = open("stat_super", "wb")
    pickle.dump(work_count_super, stat_super_file)
    stat_super_file.close()


#프로그램 시작
def start_search():
    global max_worker
    global count_worker
    global mon_part1
    global mon_part2
    global mon_part3
    global mon_part4
    global tue_part1
    global tue_part2
    global tue_part3
    global tue_part4
    global wed_part1
    global wed_part2
    global wed_part3
    global wed_part4
    global thu_part1
    global thu_part2
    global thu_part3
    global thu_part4
    global fri_part1
    global fri_part2
    global fri_part3
    global fri_part4
    global sat_part1
    global sat_part2
    global sat_part3
    global sat_part4
    global sun_part1
    global sun_part2
    global sun_part3
    global sun_part4

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
    max_worker.insert(1.0, "파트 당 근무 인원")

    count_worker = Text(tk, width = 12, height = 2, font = 12, wrap = "word")
    count_worker.place(x = 20, y = 100)
    count_worker.insert(1.0, "주당 최대 근무")

    #시간표 조회 시작
    search_button = Button(tk, text = '시간표 조회', command = get_result, width = 13, bg = 'blue', fg = 'white', height = 2, padx = 10, pady = 10)
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
    #mon_part1.insert(1.0, "     오영석\n     김두현\n     김민석")

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


