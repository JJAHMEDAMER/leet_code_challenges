'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''




from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    prefix = min(strs)
    for x in range(len(strs)):
        for y in range(len(prefix)):
            if prefix[y] != strs[x][y]: 
                prefix = prefix[:y]
                break
    return prefix




solution = longestCommonPrefix(["flower","flow","flight"])
print(solution)

solution = longestCommonPrefix(["dog","racecar","car"])
print(solution)

solution = longestCommonPrefix(["ab", "a"])
print(solution)

solution = longestCommonPrefix(["aaa", "aa", "aaa"])
print(solution)

solution = longestCommonPrefix(["reflower","flow","flight"])
print(solution)