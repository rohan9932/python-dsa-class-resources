#used for figuring out next greater(back loop)/
#previous greater(forward loop) in an array

def monotonic_decreasing(nums):
    n = len(nums)
    stack = []
    res = [0]*n

    for i in range(n-1, -1, -1): #backward loop
        while stack and stack[-1] <= nums[i]:
            stack.pop() #pop the elements that don't fit the decreasing order

        if not stack:
            res[i] = -1 #no greater element at right
        else:
            res[i] = stack[-1] #the top element will be immediate greater

        stack.append(nums[i])

    return res

print(monotonic_decreasing([1, 3, 4, 2]))
