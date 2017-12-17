"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ''
        history = ''
        for i in s:
            if i not in substring:
                substring += i
            else:
                if len(substring) > len(history):
                    history = substring

        if len(substring) > len(history):
            return len(substring)
        else:
            return len(history)


if __name__ == '__main__':
    input = [
        'abcabcbb',
        'bbbbb',
        'pwwkew',
        'dvdf',
        'jbpnbwwd'
    ]
    output = [
        3,
        1,
        3,
        3,
        4
    ]
    for i in range(len(input)):
        sol = Solution().lengthOfLongestSubstring(input[i])
        print(sol)
        print("solution is right" if sol == output[i] else "solution is wrong")
