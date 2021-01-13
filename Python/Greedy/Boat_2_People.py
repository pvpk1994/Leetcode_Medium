# Calculate the number of boats required to carry people based on the weights of the people and the wieghing limit of the boat
# Leetcode Question: https://leetcode.com/problems/boats-to-save-people/
# Time Complexity: O(NlogN) and Space Complexity: O(1)

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Atmost 2 people to travel on boat
        people = sorted(people)
        # Heaviest person can be paired with lightest person and if it still exceeds limit, 
        # heaviest person cannot share boat with anyone: so heaviest person has to have his own boat
        # so, the lightest person will then be paired with next heaviest person and so on...
        light = 0
        heavy = len(people)-1
        num_boats =0
        while light <= heavy:
            num_boats +=1
            # check for heavy-light pair 
            if people[heavy]+people[light] <= limit:
                # they can fit, so a boat has been assigned to them 
                light += 1
            heavy -= 1
        return num_boats
