# linear
#LEET CODE 1 .Two sum
# def two_sum(nums : list , target : int):
#     for i in nums :
#         if target - i in nums :
#             return [nums.index(i) , nums.index(target-i)]
# print(two_sum([2,7,11,15],9))      
#LEET CODE 42 .Trapping Rain Water
# def trapping_rain_water(water : list):
#     max_height = max(water)
#     max_index = water.index(max_height)
#     max_left = water[0]
#     max_right = water[-1]
#     answer = 0
#     for i in range(max_index) : 
#         max_left = max(max_left,water[i])
#         answer += max_left - water[i]
#     for i in reversed(range(max_index,len(water))):
#         max_right = max(max_right,water[i])
#         answer += max_right - water[i]
#     return answer 
# print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
# LEET CODE 15 3Sum
# def threeSum(nums) :
#         res = []
#         nums.sort()
        
#         for i, a in enumerate(nums):
#             # same value as before so continue
#             if i > 0 and a == nums[i-1]:
#                 continue
                
#             l,r = i+1, len(nums)-1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -=1
#                 elif threeSum < 0:
#                     l+= 1
#                 else:
#                     res.append([a,nums[l],nums[r]])
#                     l += 1
#                     while nums[l] == nums[l-1] and l<r:
#                         l+= 1
#         return res
# print(threeSum([-1,0,1,2,-1,-4]))
    
