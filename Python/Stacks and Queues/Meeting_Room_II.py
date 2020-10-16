# meeting Rooms II 
# Using Min-heap 
# Time Complexity: O(NlogN)
# Author: Pavan Kumar Paluri
# Leetcode Question: https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) ==0:
            return 0
        # Sort based on the start times of the meetings 
        intervals = sorted(intervals, key=lambda x:x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] < free_rooms[0]:
                # current room is busy 
                heapq.heappush(free_rooms, intervals[i][1])
            elif intervals[i][0] >= free_rooms[0]:
                # A meeting room is available 
                heapq.heappop(free_rooms)
                heapq.heappush(free_rooms, intervals[i][1])
        return len(free_rooms)
