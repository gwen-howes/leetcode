class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(len(nums)-1, 0, target, nums)

    def binarySearch(self, high: int, low: int, target: int, nums: List[int]) -> int:
        if high < low:
            return -1
        
        i = low + (high-low) //2

        if nums[i] == target:
            return i
        if nums[i] < target:
            return self.binarySearch(high, i+1, target, nums)
        if nums[i] > target:
            return self.binarySearch(i-1, low, target, nums)