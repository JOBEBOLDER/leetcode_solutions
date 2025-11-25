
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

#「只要题里出现 id，要根据 id 找对象 → 条件反射写 dict」。
#每个对象有唯一 id → 以后你会拿着 id 去找对象 → 就自动写 dict。

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id2emp = {e.id: e for e in employees}

        def dfs(eid)->int:
            e_emp = id2emp[eid]
            total = e_emp.importance
            for sub_id in e_emp.subordinates:
                total += dfs(sub_id)
            return total
        return dfs(id)
            












'''
class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
        
    def __repr__(self):
        return f"Employee(id={self.id}, importance={self.importance}, subordinates={self.subordinates})"


# 构造输入
employees = [
    Employee(1, 5, [2, 3]),
    Employee(2, 3, []),
    Employee(3, 3, []),
]

# 字典推导式
e.id : e⬇️
意思是：
以员工的 id 当作 key
以这个员工对象本身当作 value

id2employee = {e.id: e for e in employees}

print("👉 id2employee 字典的真实结构：")
print(id2employee)
print()

print("👉 访问 id2employee[1] 得到的对象：")
print(id2employee[1])
print()

# 下面我们写 DFS，看它如何一步步走
def dfs(eid):
    print(f"\n🔍 dfs({eid}) 被调用")
    emp = id2employee[eid]
    print(f"   当前员工对象: {emp}")
    
    total = emp.importance
    print(f"   初始 importance = {total}")
    
    for sub_id in emp.subordinates:
        print(f"   遇到下属 {sub_id}，递归进入 dfs({sub_id})")
        total += dfs(sub_id)
        print(f"   dfs({sub_id}) 返回后，total = {total}")
    
    print(f"🔚 dfs({eid}) 返回 {total}")
    return total


# 从 id=1 开始 DFS
result = dfs(1)
print("\n🎉 最终结果 =", result)






'''
