class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        pascalTriangle = [[1], [1, 1]]
        for i in range(2, numRows):
            ithList = [1]            # the ith list
            for j in range(1, i):
                ithList.append(pascalTriangle[-1][j - 1] + pascalTriangle[-1][j])
            ithList.append(1)
            pascalTriangle.append(ithList)
        
        return pascalTriangle
        

