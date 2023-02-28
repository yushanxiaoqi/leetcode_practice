class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        l = 0
        r = 0
        temp =0
        lenth=n+1
        if not nums:
            return 0
        while r < n:
            if temp < target:
                temp +=nums[r]
                print(temp)

            while temp >= target:
                lenth = min(lenth,r-l)
                print(l,r)
                l +=1
                temp-=nums[l]
            r+=1
        if  lenth== n +1 :
            return 0
        return lenth

s = Solution()
a=7
b= [2,3,1,2,4,3]
s.minSubArrayLen(a,b)