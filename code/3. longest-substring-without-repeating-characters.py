from typing import List

class Test:
    def __init__(self, s : str, expected : int):
        self.s = s
        self.expected = expected
    
    def ToString(self) -> str:
        return 's: "' + self.s + '"'
    
    def IsCorrect(self, answer : List[int]) -> bool:
        return answer == self.expected

def RunTests(testcases) -> None:
    s = Solution()
    i = 1
    for test in testcases:
        answer = s.lengthOfLongestSubstring(test.s)
        if test.IsCorrect(answer):
            print(f"Test #{i} passed!")
        else:    
            print(f"Test #{i} FAILED!")
            print(f"\t{test.ToString()}, Solution : {answer} should be {test.expected}")
        i+=1

###################################################################
# Solution class and main function
###################################################################

testcases = [ 
    Test("abcabcbb", 3),
    Test("bbbbb", 1),
    Test("pwwkew", 3),
]

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapCharToIndex = {}
        startIdx = 0
        maxLength = 0
        for i in range(len(s)):
            if s[i] in mapCharToIndex and mapCharToIndex[s[i]] >= startIdx:
                maxLength = max(maxLength, i - startIdx)
                startIdx = mapCharToIndex[s[i]] + 1
            mapCharToIndex[s[i]] = i
        return max(maxLength, len(s) - startIdx)

def main():
    RunTests(testcases)
        
if __name__ == "__main__":
    main()