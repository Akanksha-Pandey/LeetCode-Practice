from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNumToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in mapNumToIndex:
                return [mapNumToIndex[target - nums[i]], i]
            mapNumToIndex[nums[i]] = i
        return []

class Test:
    def __init__(self, nums : List[int], target : int):
        self.nums = nums
        self.target = target
    
    def text(self):
        text = ""
        for num in self.nums:
            text = text + str(num) + ", "
        return "Nums: [" + text[:-2] + "], target: "+ str(self.target)

def main():
    s = Solution()
    testcases = [ Test([2,7,11,15], 9), 
    Test([3,2,4], 6), 
    Test([3,3], 6)]

    for test in testcases:
        answer = s.twoSum(test.nums, test.target)
        print(f"Test : {test.text()}, Solution : [{answer[0]},{answer[1]}]")

if __name__ == "__main__":
    main()