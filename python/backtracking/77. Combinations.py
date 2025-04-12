

class solution:
    def __init__(self):
        self.res = []
        self.tracking = [] #processing result
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtracking(1,n,k)
        return res


    def backtracking(self, start:int,n:int,k:int):
        #end condition:
        if len(self.tracking) == k:
            self.res.append(self.tracking.copy())

        #start backtracking
        for i in range(start, n + 1):
            self.tracking.append(i)

            self.backtracking(i + 1, n,k)

            self.tracking.pop()