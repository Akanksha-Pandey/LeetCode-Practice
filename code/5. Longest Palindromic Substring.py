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
    Test("babad", "aba"),
    Test("cbbd", "bb")
]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        mid = len(s)//2
        left = mid
        right = mid
        while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
            left = left - 1
            right = right + 1
        first = s[left : right+1]        
        left = mid - 1
        right = mid
        while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
            left = left - 1
            right = right + 1
        second = s[left : right+1]
        return first if len(first) > len(second) else second
        

def main():
    RunTests(testcases)	

if __name__ == "__main__":
    main()        
