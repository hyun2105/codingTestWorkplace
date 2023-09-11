# def solutin(s):
#     dic = {"zero" : 0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,
#           "eight":8,"nine":9}
#     string = s
    
#     for i in dic :
#         if i in string :
#             string = string.replace(i,str(dic[i]))
#     return int(string)

#
# def solution(s) :
#     res = ""
#     cnt = 1
#     lst = []
#     answer = []
#     while cnt <= len(s):
#         for i in range(0,len(s),cnt):
#             lst.append(s[i:i+cnt])
#         check = 1
#         for i in range(0,len(lst)-1):
#             if lst[i] == lst[i+1] :
#                 check +=1
#             elif lst[i] != lst[i+1] :
#                 if check != 1 :
#                     res += str(check)
#                 res +=lst[i]
#                 check = 1     
#             if i == len(lst)-2 :
#                 if check != 1 :
#                     res += str(check)
#         res += lst[-1] 
#         answer.append(len(res))
#         lst = []
#         res = ""
#         cnt +=1         
    
#     return min(answer)     
# print(solution("xababcdcdababcdcd"))