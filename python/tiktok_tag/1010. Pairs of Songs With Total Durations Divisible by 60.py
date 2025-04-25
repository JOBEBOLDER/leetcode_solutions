class Solution:
    #time: O(n)
    #space: O(1)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        reminders = [0] * 60

        count = 0

        for t in time:
            r = t % 60 #calculate t reminders
            complement = (60-r) % 60
            
            #find another digit complement and add one
            count += reminders[complement]

            reminders[r] += 1
        return count
        