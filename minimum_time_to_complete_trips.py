'''
start at 1 and keep checking if the time we have is enough to complete the trips we want.

[1,2,10,1], total = 16
 
6 + 3 + 0 + 6


5

160 units of time 

Solution:
- use binary search to narrow down the search space of the units of time

if 10 units of time is not enough -> no need to check 1 - 9

lo -> 7
hi -> 7
mid -> 

Time -> n * (log (k))
Space -> O(1)

'''
from typing import List
class Solution:
    def minimumTime(self, time: List[int], total_trips: int) -> int:
        def is_time_enough(given_time: int) -> bool:
            actual_trips = 0
            for t in time:
                actual_trips += given_time//t
            return actual_trips >= total_trips
        
        left = 1
        right = max(time) * total_trips
        while left < right:
            mid = (left + right)//2
            if is_time_enough(mid):
                right = mid
            else:
                left = mid + 1
        return left
        