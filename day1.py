# 문자열 다루기
#LEETCODE 125 Valid Palindrome
# def ispalindrome():
#     string = input()
#     lst = []
#     for char in string :
#         if char.isalnum() :
#             lst.append(char.lower())
#     return lst == lst[::-1] 
# print(ispalindrome())
#LEETCODE 344 Reverse String
# def reverse_string():
#     lst = list(input())
#     return lst[::-1]
#LEETCODE 937 Reorder Log Files
# def reorder_log_files(logs):
#     letter, digit = [] ,[]
#     for log in logs :
#         if log[1].isdigit():
#             digit.append(log)
#         else : 
#             letter.append(log)
#     letter.sort(key = lambda x : (x.split()[1:],x.split()[0]))
#     return letter + digit
#LEETCODE 819 Most common Word
# import collections
# def most_common_word(paragraph,banned):
#     words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
#     counts = collections.Counter(words)
#     return counts.most_common(1)[0][0]
#LEETCODE 49 Group Anagrams    
# import collections
# def group_anagram(words):
#     dic = collections.defaultdict(list)
#     for word in words :
#         dic[''.join(sorted(word))].append(word)
#     return list(dic.values())
#LEETCODE 5 Longest Palindrome Substring
# def LPS(s : str):
#     if len(s) <2 or s != s[::-1]:
#         return s
#     def expand(left,right):
#         while left >=0 and right <len(s) and s[left] == s[right] :
#             left -=1
#             right +=1 
#         return s[left + 1: right]
#     result = ""
#     for i in range(len(s)-1):
#         result = max(result,expand(i,i+1),expand(i,i+2),key=len)
#     return result
    