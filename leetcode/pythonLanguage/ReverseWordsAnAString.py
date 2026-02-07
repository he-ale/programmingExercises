class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        word= ''
        for character in s:
            if (character == ' '):
                if(word!=''):
                    words.append(word)
                    word= ''
            else:
                word+=character
        words.append(word)
        words.reverse()
        return " ".join(words)
    
solution= Solution()

print(solution.reverseWords("the sky is blue"))
print(solution.reverseWords("  hello world  "))
print(solution.reverseWords("a good   example"))