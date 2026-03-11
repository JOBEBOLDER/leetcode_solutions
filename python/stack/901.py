#time:O1
#space:ON
class StockSpanner:

    def __init__(self):
        self.stack = [] #current_price , prev_span

    def next(self, price: int) -> int:
        cur_span = 1
        while self.stack and self.stack[-1][0] <= price:
            pre_price,pre_span = self.stack.pop()
            cur_span += pre_span
        self.stack.append((price,cur_span))
        return cur_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
'''
1. 时间复杂度：均摊 $O(1)$ (Amortized $O(1)$)虽然单次调用 next 时，while 循环可能会执行多次（比如价格一直涨，一口气弹出栈里好几天的记录），
但从长期来看：每个元素最多入栈一次。每个元素最多出栈一次。如果你调用了 $n$ 次 next，那么总的 pop 操作次数绝对不会超过 $n$ 次。
平均下来，每次 next 消耗的时间就是 $O(1)$。这在算法中被称为“均摊时间复杂度”。

2. 空间复杂度：$O(n)$这里的空间复杂度不是 $O(1)$，而是 $O(n)$。
原因：在最坏的情况下
（例如股票价格一直在下跌，如 [100, 90, 80, 70...]），while 循环永远不会触发，所有的价格都会被存在栈里。栈的大小会随着 next 调用次数的增加而线性增长。

'''