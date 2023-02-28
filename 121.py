# n = input()
n = 180

def get_result(n):
    nums = []
    for i in range(2, int(n ** (0.5)) + 1):
        print(i,"i")
        while n % i == 0:
            nums.append(str(i))
            n = n / i
    if n != 1:
        nums.append(str(n))
    nums.sort()
    for c in range(len(nums)):
        print(nums[c], end=" ")


get_result(n)