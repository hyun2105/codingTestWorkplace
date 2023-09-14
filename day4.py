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
# DFS 
def num_is_island(islands):
    def dfs(i,j):
        if i<0 or i>=len(islands) or j<0 or j>=len(islands) or islands[i][j] != 1 : return 
    
    count = 0
    for i in range(islands):
        for j in range(len(islands[0])):
            if islands[i][j] == 1:
                dfs(i,j)
                count +=1 
    return count 
print(num_is_island([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0]]))