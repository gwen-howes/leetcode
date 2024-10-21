class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}

        for num in nums:
            if hash_table.get(num, 0) == 1:
                return True
            else:
                hash_table[num] = 1
        
        return False