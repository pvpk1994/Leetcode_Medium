# Asteroid Collisions
# Leetcode Medium Questions
# Author: Pavan Kumar Paluri

# Question: https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 0:
            return []
        stack = []
        for i in range(0, len(asteroids)):
            # Incoming asteroid should move towards left and the existing one on top has to move right
            while stack and asteroids[i]<0<stack[-1]:
                # right moving asteroid is smaller than left moving one
                if stack[-1] < abs(asteroids[i]):
                    stack.pop()
                    continue
                # Right moving asteroid is larger than left moving one:
                # Simply destory the left moving smaller one and continue
                elif stack[-1] > abs(asteroids[i]):
                    break
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
                break
            else:
                stack.append(asteroids[i])
        return stack
