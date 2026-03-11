def find_everyone_available(slots, total_range):
    """
    slots: List[List[int]], 格式为 [[start1, end1], [start2, end2], ...]
    total_range: [total_start, total_end] 整个考查的时间范围
    """
    if not slots:
        return [total_range]

    # 1. 按照开始时间进行排序 O(N log N)
    slots.sort(key=lambda x: x[0])

    # 2. 合并重叠的忙碌区间
    merged_busy = []
    for current in slots:
        if not merged_busy or current[0] > merged_busy[-1][1]:
            # 没有重叠，直接添加
            merged_busy.append(current)
        else:
            # 有重叠，更新当前最后一个区间的结束时间
            merged_busy[-1][1] = max(merged_busy[-1][1], current[1])

    # 3. 在合并后的忙碌区间之间寻找空闲时间 (Gaps)
    free_time = []
    curr_start = total_range[0]

    for busy_start, busy_end in merged_busy:
        if busy_start > curr_start:
            # 忙碌开始前有一段空闲
            free_time.append([curr_start, busy_start])
        # 更新下一次空闲可能开始的时间
        curr_start = max(curr_start, busy_end)

    # 4. 检查最后一段
    if curr_start < total_range[1]:
        free_time.append([curr_start, total_range[1]])

    return free_time

# 测试用例
# 人 A 忙: [1, 3], [6, 7]
# 人 B 忙: [2, 4], [8, 10]
# 总范围: [0, 12]
# 输出应该是: [[0, 1], [4, 6], [7, 8], [10, 12]]