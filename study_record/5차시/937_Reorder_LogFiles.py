class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # for log in logs:
        #     tmp_list = log.split()
        #     if tmp_list[1].
        logs.sort()
        print(logs)


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
a = Solution()
a.reorderLogFiles(logs)
