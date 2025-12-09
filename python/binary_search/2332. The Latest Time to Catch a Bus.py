class Solution:
    '''
    思路小结（你原本的想法，其实已经是对的）：
    1. 排序 buses 和 passengers，按时间顺序模拟上车。
    2. 用 i 指针扫乘客，for 循环扫每一辆 bus：
        - 条件：乘客到达时间 <= bus 时间，且当前车没满，就让乘客上车。
        - 如果是最后一辆车，记录：
            - last_board_time：这辆车最后一个上车乘客的到达时间
            - seats_remaining：最后一辆车剩余座位
    3. 最后一辆车没满：
        - 理论最晚到达时间 = 最后一辆车发车时间 last_buses_time
       最后一辆车满了：
        - 理论最晚到达时间 = last_board_time - 1
    4. 再从这个时间往前找一个没有乘客到达的时间（while time in passenger_set: time -= 1）
    '''
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        passenger_set = set(passengers)

        last_buses_time = buses[-1]
        last_board_time = -1            # 最后一辆车最后一个上车乘客时间
        seats_remaining = capacity      # 最后一辆车剩余座位数（初始是满的）

        i = 0
        n = len(passengers)

        # 模拟每辆车
        for bus in buses:
            cur_seats = capacity
            # ✅ 这里要用 <=，乘客可以在发车时间点到达
            while cur_seats > 0 and i < n and passengers[i] <= bus:
                if bus == last_buses_time:
                    last_board_time = passengers[i]     # 记录最后一辆车的最后上车时间
                    seats_remaining -= 1               # 最后一辆车少一个空位

                i += 1           # 这个乘客上车
                cur_seats -= 1   # 当前这辆车空位减一

        # 判断最后一辆车是否满
        if seats_remaining > 0:
            # 没满：你可以卡在最后一辆车发车的那个时间点
            time = last_buses_time
        else:
            # 已满：你必须比最后一个上车的人更早到
            time = last_board_time - 1

        # 不能和任何乘客同一时间到达，要一直往前退，注意要用while
        while time in passenger_set:
            time -= 1

        return time