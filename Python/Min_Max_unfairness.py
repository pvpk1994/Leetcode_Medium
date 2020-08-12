# Source: HackerRank
# Author: Pavan Kumar Paluri
# Question: https://www.youtube.com/redirect?q=https%3A%2F%2Fwww.hackerrank.com%2Fchallenges%2Fangry-children%2Fproblem%3Fh_l%3Dinterview%26playlist_slugs%255B%255D%3Dinterview-preparation-kit%26playlist_slugs%255B%255D%3Dgreedy-algorithms&v=SB4fbNHwavY&redir_token=QUFFLUhqbnI1ajEyeUFxdi1FaElkcVZ4SFhRaEdGSGNzZ3xBQ3Jtc0tsRG96bUNRR25XbWFOVDZ6R3pBZUhzUFNCUVlmaE5EaEtkcVdJTWZBXzFXdzU4enIyQXJOMlhUYTRsTjZ5RXdJMnQwTHZ6TVo3OFNZcG1MMW5UZTM3NUhiZ25XZkU1WGZJRDNZWkpuNUpsSERXLVpSbw%3D%3D&event=video_description

# Complete the maxMin function below.
def maxMin(k, arr):
    arr = sorted(arr)
    answer = math.inf
    for i in range(0, len(arr), 1):
        if i+k-1 < len(arr):
            answer = min(answer, arr[i+k-1]-arr[i])
    return answer
