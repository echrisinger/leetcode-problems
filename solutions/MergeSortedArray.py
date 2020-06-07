class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m-1
        i2 = n-1
        m_i = m+n-1
        
        while i1 >= 0 or i2 >= 0:
            if i1 < 0:
                nums1[m_i] = nums2[i2]
                i2 -= 1
                m_i -= 1
            elif i2 < 0 or nums1[i1] >= nums2[i2]:
                nums1[m_i] = nums1[i1]
                i1 -= 1
                m_i -= 1
            else:
                nums1[m_i] = nums2[i2]
                i2 -= 1
                m_i -= 1

