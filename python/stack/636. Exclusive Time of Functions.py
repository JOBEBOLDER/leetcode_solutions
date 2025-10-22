class Solution:
    #time:On
    #space:On
    #独占时间（Exclusive Time） 指的是函数实际执行的时间，不包括：

    # 被其他函数中断的时间
    # 等待的时间
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n # the output :the value at the ith index represents

        stack = [] #keep track of the FIFO sequency

        prev_time = 0

        for log in logs:
            #get every part of the element we need to process next
            parts = log.split(':')
            func_id = int(parts[0])
            action = parts[1]
            timestamp = int(parts[2])

            if action == 'start':
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                # 更新时间点为当前时间戳
                # 下次计算时间差将从这个时间点开始
                prev_time = timestamp

            else:
                result[stack.pop()] += timestamp - prev_time + 1

                # 更新时间点为 timestamp + 1
            # 为什么要 +1？
            # 因为当前时间单位已经被用完了，
            # 下一个函数（如果栈中还有）将从下一个时间单位开始
                prev_time = timestamp + 1

        return result

