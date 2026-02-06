#LeetCode 42: https://leetcode.com/problems/trapping-rain-water/description/

class Solution:
    def trap(self, height):
        n = len(height)
        #next most largest element
        mostLStack = []
        nextMostL = [0]*n

        for i in range(n-1, -1, -1):
            while mostLStack and mostLStack[-1] <= height[i]:
                mostLStack.pop()
            
            if not mostLStack:
                nextMostL[i] = -1
            else:
                nextMostL[i] = mostLStack[0] #the bottom one
            
            mostLStack.append(height[i])

        #previous most largest element 
        prevLStack = []
        prevMostL = [0]*n

        for i in range(0, n):
            while prevLStack and prevLStack[-1] <= height[i]:
                prevLStack.pop()
            
            if not prevLStack:
                prevMostL[i] = -1
            else:
                prevMostL[i] = prevLStack[0] #the bottom one
            
            prevLStack.append(height[i])

        trapped_water = 0

        for i in range(1, n-1):
            prev_L = prevMostL[i]
            next_L = nextMostL[i]

            if prev_L > 0 and next_L > 0: #for ignoring which bars have no prev greater or next greater values
                trapped_water += min(prev_L, next_L) - height[i]
        
        return trapped_water
    
sol = Solution()
print(sol.trap([4,2,0,3,2,5]))