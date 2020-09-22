# Car pooling using (Bucket Sort + Greedy Approach)
# Author: Pavan Kumar Paluri

class Solution:
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # greedy approach - time complexity O(NlogN)
        timeline = []
        for trip in trips:
            timeline.append([trip[1], trip[0]])
            timeline.append([trip[2], -trip[0]]) # - to indicate passenger offboarding
        
        # now timeline has all the desired boarding and offboarding details
        timeline = sorted(timeline)
        
        filled_capacity  =0
        # Since timeline is sorted based on the travel start times and end times
        for time, capacity_change in timeline:
            filled_capacity += capacity_change
            if filled_capacity > capacity:
                return False
        # if here: trips were legal
        return True
        '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # greedy approach
        timeline = [0]*1001
        for trip in trips:
            timeline[trip[1]] += trip[0]
            # offboarding passengers 
            timeline[trip[2]] -= trip[0]
        
        # if here: all the passengers have boarded and offboarded
        dynamic_capacity = 0
        for trip in timeline:
            dynamic_capacity += trip
            if dynamic_capacity > capacity:
                return False 
        return True 
