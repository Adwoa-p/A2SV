class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2 == 0:
            multiple=n
            return multiple
        multiple = 2*n 
        return  multiple
