from typing import List

def RunTests(testcases) -> None:
    s = Solution()
    i = 1
    for test in testcases:
        answer = s.twoSum(test.nums, test.target)
        if test.IsCorrect(answer):
            print(f"Test #{i} passed!")
        else:    
            print(f"Test #{i} FAILED!")
            print(f"\t{test.ToString()}, Solution : [{answer[0]},{answer[1]}] should be {test.expected}")
        i+=1
class Test:
    def __init__(self, nums : List[int], target : int, expected : List[int]):
        self.nums = nums
        self.target = target
        self.expected = expected
    
    def ToString(self):
        text = ""
        for num in self.nums:
            text = text + str(num) + ", "
        return "nums: [" + text[:-2] + "], target: "+ str(self.target)
    
    def IsCorrect(self, answer : List[int]) -> bool:
        return sorted(answer) == sorted(self.expected)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNumToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in mapNumToIndex:
                return [mapNumToIndex[target - nums[i]], i]
            mapNumToIndex[nums[i]] = i
        return []

def main():
    testcases = [ 
        Test([2,7,11,15], 9, [0, 1]), 
        Test([3,2,4], 6, [1, 2]), 
        Test([3,3], 6, [0, 1])
        ]
    RunTests(testcases)
        
if __name__ == "__main__":
    main()