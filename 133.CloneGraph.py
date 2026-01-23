from typing import List
from typing import Optional

###################################################################
# Solution class and main function
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
###################################################################

testcases = [ 
    Test([[2,4],[1,3],[2,4],[1,3]], [[2,4],[1,3],[2,4],[1,3]]),
    Test([[]], [[]]),
    Test([], [])
]

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


###################################################################
# boilerplate for testing
###################################################################

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Test:
    def __init__(self, s : List, expected : List):
        self.s = self.buildGraph(s)
        self.expected = expected
    
    def buildGraph(self, arr: List) -> Optional['Node']:
        
    
    def ToString(self) -> str:
        return 's: "' + self.s + '"'
    
    def IsCorrect(self, answer) -> bool:
        return answer == self.expected


def RunTests(testcases) -> None:
    s = Solution()
    i = 1
    for test in testcases:
        answer = s.longestPalindrome(test.s)
        if test.IsCorrect(answer):
            print(f"Test #{i} passed!")
        else:    
            print(f"Test #{i} FAILED!")
            print(f"\t{test.ToString()}, Solution : {answer} should be {test.expected}")
        i+=1


def main():
    RunTests(testcases)	

if __name__ == "__main__":
    main()        
