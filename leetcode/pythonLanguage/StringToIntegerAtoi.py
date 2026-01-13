class Solution:
    def myAtoi(self, s: str) -> int:
        myAtoi= 0
        sign= 1
        i= 0
        while(s[i]==' '):
            i+=1
        if(i<len(s) and (s[i]=='-' or s[i]=='+')):
            if(s[i]=='-'):
                sign= -1
            i+=1
        while i< len(s) and ('0'<= s[i] <='9') :
            myAtoi= (myAtoi*10)+int(s[i])
            if sign * myAtoi > 2**31 - 1:
                return 2**31 - 1
            if sign * myAtoi < -2**31:
                return -2**31
            i+=1 
        return myAtoi * sign
    
solution= Solution()
print(solution.myAtoi('42'))
print(solution.myAtoi(' -42'))
print(solution.myAtoi('1337c0d3'))
print(solution.myAtoi('0-1'))
print(solution.myAtoi('words and 987'))
                   
