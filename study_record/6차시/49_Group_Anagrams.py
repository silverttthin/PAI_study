import collections
# defaultdict 연습문제
def groupAnagrams(strs):
    # 정렬해서 같은 결과값이 나오는 문자열들은 Anagrams이므로
    # 그것들끼리 같은 리스트에 담기
    tmp = collections.defaultdict(list)
    for word in strs : 
        
        sorted_word = ''.join(sorted(word)) # sorted 내장함수는 정렬 결과를 리스트로 줌
        tmp[sorted_word].append(word)
        
    ans = []
    for key in tmp:
        ans.append(tmp[key])

    print(ans)



strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)