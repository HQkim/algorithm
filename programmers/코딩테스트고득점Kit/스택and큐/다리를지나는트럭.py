from collections import deque
def solution(bridge_length, weight, truck_weights):

    bridge = [0] * bridge_length
    bridge_queue = deque(bridge)
    truck_queue = deque(truck_weights)

    t = 0
    bridge_weight = 0
    while True:
        t += 1
        bridge_queue.insert(0,0)
        out = bridge_queue.pop()
        bridge_weight -= out
        if truck_queue:
            if truck_queue[0] + bridge_weight <= weight:
                bridge_queue[0] = truck_queue.popleft()
                bridge_weight += bridge_queue[0]
        if not truck_queue and bridge_weight == 0:
            break

    return t

print(solution(100, 100, [10]))