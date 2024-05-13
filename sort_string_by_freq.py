'''
Test cases:
tree -> eert, eetr
cccaaa -> cccaaa
Aabb -> bbAa
a -> a
ssabbbcccc111111 -> 111111ccccbbbssa


Solution:
- find the frequency of each character in the string and store those in a dictionary - N
- get the items of the dictionary and put them in a max heap - NlgN
- go over the heap and add to an array, the character * freq - NlgN
- return the array as a string - N


Time - NlgN
Space - N

tree

t: 1
r: 1
e: 2

(-2, e), (-1, t), (-1, r)

"ee", "t", "r" -> eetr

Solution:
- find the frequency of each character in the string and store those in a dictionary - N
- get the items of the dictionary and put them in a max heap - NlgN
- go over the heap and add to an array, the character * freq - NlgN
- return the array as a string - N

Or
- find the frequency of each character in the string and store those in a dictionary - N
- get the items of the dictionary and add them to an array so that the array remains sorted 
- go over the heap and add to an array, the character * freq
'''
from collections import defaultdict
import heapq
class Solution:
    def count_char_occurences(self, s: str) -> dict:
        char_freq = defaultdict(int)
        for char in s:
            char_freq[char] += 1
        return char_freq
    
    def frequencySort(self, s: str) -> str:
        char_freq = self.count_char_occurences(s)

        max_heap = []
        for k,v in char_freq.items():
            heapq.heappush(max_heap, (-v, k))
        
        result = []
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char*(-freq))
        
        return "".join(result)
        
        

        