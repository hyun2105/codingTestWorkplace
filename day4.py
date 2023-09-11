#  STACK AND QUEUE
# LEETCODE 20 Valid Parentheses
# def valid_parenthese(string : str):
#     stack = []
#     table=  {
#         ')' : '(',
#         '}' : '{',
#         ']' : '['
#     }
#     for char in string :
#         if char not in table:
#             stack.append(char)
#         elif not stack or table[char] != stack.pop():
#             return False
#     return len(stack) == 0 
# print(valid_parenthese("(){}[]"))
#LEETCODE 316 Remove Duplicate Letter 
def remove_duplicate_letter(string):
    stack = []
    sett = sorted(list(set(string)))
    print(sett)
    return 0
print(remove_duplicate_letter("bcabc"))

