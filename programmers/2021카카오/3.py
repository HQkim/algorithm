import math


def oranize_records_to_dict(fees, records):
    records_dict = {}                               # 입출차 내역을 기록할 딕셔너리
    for r in records:
        # records에서 기록시간, 차량번호, 상태(IN/OUT)불러옴
        time, car_num, status = r.split()
        # 00:00분을 기준으로 몇분 경과했는지로 기록시간을 변환
        time = int(time[:2]) * 60 + int(time[3:])

        if records_dict.get(car_num):                       # 기존 기록이 있다면
            if status == "OUT":
                time_in, status_in, total_time = records_dict[car_num]
                time_diff = time - time_in
                records_dict[car_num] = [
                    time, status, total_time + time_diff]
            else:
                records_dict[car_num][:2] = [time, status]
        else:                                               # 기존 기록이 없다면
            records_dict[car_num] = [time, status, 0]

    for key, value in records_dict.items():                 # 입차후 출차된 내역이 없는 경우 처리
        time, status, total_time = value
        if status == "IN":
            time_diff = 23*60 + 59 - time
            records_dict[key] = [time, status, total_time + time_diff]

    return records_dict


def solution(fees, records):

    # key=차량번호, value=[최종기록시간(분), 최종상태(IN/OUT), 최종누적시간]
    records_dict = oranize_records_to_dict(fees, records)

    # 차량 번호 작은순으로 정렬
    car_nums = list(records_dict.keys())
    car_nums.sort(key=lambda x: int(x))

    # 요금 계산
    answer = []
    for car_num in car_nums:
        total_time = records_dict[car_num][2]
        if total_time <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + math.ceil((total_time-fees[0]) / fees[2]) * fees[3]
        answer.append(fee)

    return answer


solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
         "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
