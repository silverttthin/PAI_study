class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        numeric_list = [] #숫자 로그만을 담을 리스트
        idx=0
        for log in logs:
            tmp_list = log.split()

            if tmp_list[1].isnumeric() :  # 숫자는 어차피 입력순이고 문자 뒤에 있으므로 따로 뺴줘서 나중에 문자정렬 결과물 뒤에 붙이기
                numeric_list.append(log)
                del logs[idx]
            idx += 1

        numeric_list.sort() # 같은 숫자인 경우 구분자 기준 정렬
#--------------------------------------------------------------------------------- 문자 정렬 + 같은경우 구분자 정렬 생각못해내고 ㅈㅈ


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
a = Solution()
a.reorderLogFiles(logs)
