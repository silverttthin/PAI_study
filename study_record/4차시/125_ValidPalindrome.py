class Solution(object):
    def isPalindrome(self, s):
        s= s.lower() #소문자화
        
        s_alnum = [] # 알파벳이나 숫자만을 담을 리스트
        for i in s:
            if i.isalnum(): s_alnum.append(i)
        
        if s_alnum == list(reversed(s_alnum)): return True # reversed만을 사용하면 에러떴음
        else: return False
        