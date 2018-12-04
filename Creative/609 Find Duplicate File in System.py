# Url: https://leetcode.com/problems/find-duplicate-file-in-system/
# Related Topics:
# String HashTable

# Example:
# Input:
# ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
# Output:  
# [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

# Creative Thinking
# Follow-up beyond contest:
# Imagine you are given a real file system, how will you search files? DFS or BFS?
# If the file content is very large (GB level), how will you modify your solution?
# If you can only read the file by 1kb each time, how will you modify your solution?
# What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
# How to make sure the duplicated files you find are not false positive?


from collections import defaultdict
class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content2files = defaultdict(list)
        for line in paths:
            directory, files = line.split(' ', 1)
            for file in files.split(' '):
                filename, content = file[:-1].split('(')
                filename = directory + '/' + filename
                content2files[content].append(filename)
        return [files for files in content2files.values() if len(files) > 1]
            