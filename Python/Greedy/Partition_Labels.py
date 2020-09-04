# Create Partition labels 
# leetcode question: https://leetcode.com/problems/partition-labels/
# Author: Pavan Kumar Paluri

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # last-seen hash_map
        last_seen = {c:i for i,c in enumerate(S)}
        j =0
        anchor =0
        answer = []
        for i,c in enumerate(S):
            j = max(j, last_seen[c])
            # if i != j : keep going on ...
            if i == j:
                answer.append(i-anchor+1)
                anchor = j+1
        return answer
