class Solution:
    def addBinary(self, a: str, b: str) -> str:
        indexZeros=0
        aux= other= ''
        if len(a)> len(b):
            indexZeros= len(a)-len(b) 
            aux= b  
            other= a  
        else:
            indexZeros= len(b)-len(a) 
            aux= a 
            other= b

        while(indexZeros>0):
            indexZeros-=1
            aux= '0'+aux
        
        carry= 0
        result=''
        print(len(other)-1)
        for i in range(len(other)-1, -1, -1):
            sum = carry+int(aux[i])+int(other[i])
            result= str(sum%2)+ result
            carry= sum//2

        if carry:
            result= "1"+result

        return result

solution= Solution()
print(solution.addBinary("11", "1"))
            