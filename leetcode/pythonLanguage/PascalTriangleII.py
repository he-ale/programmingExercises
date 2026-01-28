from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        value = 1 
        row.append(value)
        
        for k in range(1, rowIndex + 1):
            value = value * (rowIndex - k + 1) // k  
            row.append(value)
        
        return row