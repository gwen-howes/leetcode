public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> seen = new HashSet<int>();
        for (int i=0; i<nums.Length; i++) {
            seen.Add(nums[i]);
        }
        return seen.Count != nums.Length;
        
    }
}