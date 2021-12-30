def longestPalindrome(s):
    left= 0

    palin_list = []
    while(left!=len(s)):
        right = len(s)
        while(left<right):
            tmp = s[left:right] # 슬라이싱에서 step을 -1로 지정하면 따로 변수에 넣어줘야하나보다..
            if s[left:right] == tmp[::-1]:
                palin_list.append(s[left:right])

            right -= 1
        left += 1

    print(max(palin_list, key=len))
    


s = "babad"
#    dabab

longestPalindrome(s)