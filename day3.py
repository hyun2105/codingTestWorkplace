# LEET CODE 561 ARRAY PARTITION 
# def array_partition(nums):
#     lst = sorted(nums)
#     sum = 0
#     min_lst = []
#     for i in lst :
#         min_lst.append(i) 
#         if len(min_lst) == 2: 
#             sum += min(min_lst)
#             min_lst = []
#     return sum
# print(array_partition([1,4,3,2]))    
# LEET CODE 121 best time to buy and sell stock
# def best_time_to_sell(nums):
#     res = []
    
#     for i in range(len(nums)-1):
#         res.append(max(nums[i+1:])-nums[i])   
#     return max(res)

# print(best_time_to_sell([7,1,5,3,6,4]))
