# 2022 카카오 주차요금계산

def solution(fees, records):
    answer = []
    result = {}
    time_last = 23 * 60 + 59

    for r in records:
        time_string, number, action = r.split()
        hour, minute = map(int, time_string.split(":"))
        time = hour * 60 + minute

        d = {}
        d["time"] = time
        d["action"] = action

        total_time = 0
        if result.get(number):
            total_time = result.get(number).get("total_time")
        if action == "OUT":
            time_p = result.get(number).get("time")
            time_diff = time - time_p
            total_time += time_diff
        d["total_time"] = total_time
            
        result[number] = d
    
    result_list = []
    for k, v in result.items():
        if v.get("action") == "IN":
            time_total = v.get("total_time") + (time_last - v.get("time"))
        else:
            time_total = v.get("total_time")
        fee = cal_price(time_total, fees)
        result_list.append([k, fee])
    
    result_list.sort(key=lambda x: int(x[0]))
    answer = [x[1] for x in result_list]

    return answer

def cal_price(time, fees):
    
    if time <= fees[0]:
        return fees[1]
    
    time_minus = time - fees[0]
    time_q = time_minus // fees[2]
    time_r = time_minus % fees[2]
    
    if time_r:
        time_q += 1
    
    return fees[1] + time_q * fees[3]


solution([180, 5000, 10, 600],
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
)
