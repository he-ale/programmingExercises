class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        aux = {}
        left = 0
        maxLen = 0

        for right in range(len(s)):
            if s[right] in aux:
                left = max(left, aux[s[right]] + 1)
            aux[s[right]] = right
            maxLen = max(maxLen, right - left + 1)

        return maxLen


solution= Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("abcade"))
print(solution.lengthOfLongestSubstring("cdd"))
print(solution.lengthOfLongestSubstring("asjrgapa"))