'''

📌 中文题目描述

给定一组传感器日志数据，每条日志包含以下字段：
	•	time：时间戳（float，单位秒）
	•	sensor_id：传感器编号（string）
	•	temperature：温度读数（float）
	•	pressure：压力读数（float）

请实现一个函数：

def analyze(start_ts: float, end_ts: float, logs: list[dict]) -> dict:

函数接收：
	•	start_ts：时间窗口的起始时间
	•	end_ts：时间窗口的结束时间
	•	logs：传感器日志列表，每条日志为字典，包含 time, sensor_id, temperature, pressure

返回一个字典，包含两部分信息：
	1.	max_temperatures
	•	键：sensor_id
	•	值：该传感器在时间区间 [start_ts, end_ts] 内的最高温度
	2.	average_pressure_in_window
	•	时间区间 [start_ts, end_ts] 内所有记录的 平均压力（浮点数）
	•	如果区间内没有任何记录，返回 None


'''

def analyze(start_ts: float, end_ts: float, logs: list[dict]) -> dict:
    max_temps = {}        # 仅统计“窗口内”的每个传感器最高温度
    total_pressure = 0.0  # 窗口内压力总和
    count_pressure = 0    # 窗口内记录条数

    st, ed = start_ts, end_ts  # 局部绑定，轻微优化

    for record in logs:
        t = record['time']
        # ✅ 先时间过滤：不在 [st, ed] 内的记录全部忽略
        if not (st <= t <= ed):
            continue

        sid = record['sensor_id']
        temp = record['temperature']
        pressure = record['pressure']

        # 在窗口内：更新该传感器最高温度
        prev = max_temps.get(sid)
        if prev is None or temp > prev:
            max_temps[sid] = temp

        # 在窗口内：累加压力与计数
        total_pressure += pressure
        count_pressure += 1

    # 没有窗口内数据时，平均压力为 None
    avg_pressure = (total_pressure / count_pressure) if count_pressure > 0 else None

    return {
        'max_temperatures': max_temps,
        'average_pressure_in_window': avg_pressure
    }

#testcases:
logs = [
    {"time": 0.1, "sensor_id": "TS-01", "temperature": 355.3, "pressure": 1.2},
    {"time": 0.1, "sensor_id": "TS-02", "temperature": 344.4, "pressure": 1.1},
    {"time": 0.2, "sensor_id": "TS-01", "temperature": 410.0, "pressure": 1.5},
    {"time": 0.2, "sensor_id": "TS-02", "temperature": 405.2, "pressure": 1.4},
    {"time": 0.3, "sensor_id": "TS-01", "temperature": 525.3, "pressure": 2.1},
    {"time": 0.3, "sensor_id": "TS-02", "temperature": 515.1, "pressure": 2.0},
    {"time": 0.4, "sensor_id": "TS-01", "temperature": 510.0, "pressure": 1.9},
    {"time": 0.4, "sensor_id": "TS-02", "temperature": 505.5, "pressure": 1.8},
]

print(analyze(0.1, 0.3, logs))