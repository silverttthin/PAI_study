import collections
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()

        for char in paragraph:
            if char.isalnum() or char == " " : pass
            else : paragraph = paragraph.replace(char, "") # 생각대로 안되면 항상 in-place여부 확인해보기
        # 알파벳과 공백만 남김.
        para_list = paragraph.split()
        counter = collections.Counter(para_list)
        for ban in banned:
            del counter[ban]
        a,b=counter.most_common(1)[0]
        
        return a

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"] # ban은 여러 개일수도 있음.
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"] # 해당 테케는 오답. 리스트 나누는 과정에서 처리 미흡. replace에서 null이 아니라 공백으로 바꿔서 정답받음..


a=Solution()
a.mostCommonWord(paragraph, banned)