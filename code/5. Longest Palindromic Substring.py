from typing import List

class Test:
    def __init__(self, s : str, expected):
        self.s = s
        self.expected = expected
    
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

		
###################################################################
# Solution class and main function
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
###################################################################

testcases = [ 
    Test("babad", "bab"),
    Test("cbbd", "bb")
]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        length = 0
        for i in range(len(s)):
            

def main():
    RunTests(testcases)	

if __name__ == "__main__":
    main()        
