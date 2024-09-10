'''
Day-3

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

'''Solution:'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        dic = {}
        MaxLen = 0
        Start_index = 0
        for i in range(n):
            if s[i] in dic and dic[s[i]] >= Start_index:
                Start_index = dic[s[i]] + 1
            dic[s[i]] = i
            MaxLen = max(MaxLen, i - Start_index + 1)
        return MaxLen
