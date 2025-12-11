class Solution:
# 	•	Time: O(n log n)
# Sorting dominates.
# 	•	Space: O(1) extra space
# Two-pointer uses only constant memory.
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        total_boat = 0

        while left <= right:
            if people[left] + people[right] <=limit:
                left+=1
                right -= 1

            else: #if it's too heavy,then remove the heavy one
                right -= 1

            #no matter what the boat should always +=1 each round
            total_boat += 1

        return total_boat
