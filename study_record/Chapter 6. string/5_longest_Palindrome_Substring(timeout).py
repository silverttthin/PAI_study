# def longestPalindrome(s):
#     left= 0

#     palin_list = []
#     while(left!=len(s)):
#         right = len(s)
#         while(left<right):
#             tmp = s[left:right] # 슬라이싱에서 step을 -1로 지정하면 따로 변수에 넣어줘야하나보다..
#             if s[left:right] == tmp[::-1]:
#                 palin_list.append(s[left:right])

#             right -= 1
#         left += 1

#     print(max(palin_list, key=len))
    
# s = "babad"


# longestPalindrome(s)

def longestPalindrome(s) :
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left, right) :
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result

s= "babad"
print(longestPalindrome(s))