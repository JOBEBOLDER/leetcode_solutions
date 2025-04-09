from typing import List

class Solution:
    '''time:On
    space:On
    '''
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            # Process current asteroid
            while stack and stack[-1] > 0 and a < 0:
                # Compare magnitudes
                if abs(stack[-1]) < abs(a):
                    stack.pop()  # Top asteroid explodes, keep checking
                    continue
                elif abs(stack[-1]) == abs(a):
                    stack.pop()  # Both explode
                    break
                else:
                    break  # Incoming asteroid explodes
            else:
                # No collision, push asteroid
                stack.append(a)

        return stack