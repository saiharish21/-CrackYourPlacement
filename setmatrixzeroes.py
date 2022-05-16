class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # for i in range(0,len(matrix)):
        #     for j in range(0,len(matrix[0])):
        #         if matrix[i][j]==0:
        #             matrix[0][j]=0
        #             matrix[i][0]=0
        # for i in range(0,len(matrix)):
        #     if matrix[i][0]==0:
        #         for j in range(1,len(matrix[0])):
        #             matrix[i][j]=0
        # for i in range(0,len(matrix[0])):
        #     if matrix[0][i]==0:
        #         for j in range(1,len(matrix)):
        #             matrix[j][i]=0
                
        rs=set()
        cs=set()
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==0:
                    rs.add(i)
                    cs.add(j)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if i in rs or j in cs:
                    matrix[i][j]=0
        """
        Do not return anything, modify matrix in-place instead.
