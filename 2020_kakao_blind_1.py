# 문자열 압축
# 2020 KAKAO BLIND RECRUITMENT
# 제한사항
# s의 길이는 1 이상 1,000 이하입니다.
# s는 알파벳 소문자로만 이루어져 있습니다.
# 입출력 예
# s	result
# "aabbaccc"	7
# "ababcdcdababcdcd"	9
# "abcabcdede"	8
# "abcabcabcabcdededededede"	14
# "xababcdcdababcdcd"	17
def solution(s) :
    res = ""
    cnt = 1
    lst = []
    answer = []
    while cnt <= len(s):
        for i in range(0,len(s),cnt):
            lst.append(s[i:i+cnt])
        check = 1
        for i in range(0,len(lst)-1):
            if lst[i] == lst[i+1] :
                check +=1
            elif lst[i] != lst[i+1] :
                if check != 1 :
                    res += str(check)
                res +=lst[i]
                check = 1     
            if i == len(lst)-2 :
                if check != 1 :
                    res += str(check)
        res += lst[-1] 
        answer.append(len(res))
        lst = []
        res = ""
        cnt +=1         
    
    return min(answer)     
print(solution("xababcdcdababcdcd"))