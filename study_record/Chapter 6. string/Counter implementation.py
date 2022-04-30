import collections 


s = "Bob hit a ball, the hit BALL flew far after it was hit"

counts = collections.Counter(s)

print(counts) # 문자열인 경우 문자열의 구성요소인 문자들의 개수들을 카운트하는 Counter 객체를 확인할 수 있음.

s_words = collections.Counter(s.split())

print(s_words)