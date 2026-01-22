from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        aux=nums1[:m]
        m0= 0
        n0= 0
        k=0
        while( m0<m and n0<n):
            if aux[m0]<nums2[n0]:
                nums1[k]= aux[m0]
                m0+=1
            else:
                nums1[k]= nums2[n0]
                n0+=1
            k+=1
        while( m0 < m ):
            nums1[k]=aux[m0]
            m0+=1
            k+=1
        while( n0 < n ):
            nums1[k]= nums2[n0]
            n0+=1
            k+=1
        return nums1
    
solution = Solution()
print(solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
