class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        for i in range(n//2):
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        for i in range((n-k)//2):
            nums[k+i], nums[n-1-i] = nums[n-1-i], nums[k+i]