class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        top=0
        bottom=n-1
        while top<bottom:
            for col in range(n):
                temp=matrix[top][col]
                matrix[top][col]=matrix[bottom][col]
                matrix[bottom][col]=temp
            top+=1
            bottom-=1 
        for i in range(n):
            for j in range(i,n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        return matrix