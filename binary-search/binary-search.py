class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        idx = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return idx