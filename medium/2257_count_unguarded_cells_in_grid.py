class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for i in guards:
            matrix[i[0]][i[1]]='G'
        for i in walls:
            matrix[i[0]][i[1]]='W'
        directions=[[0,-1],[0,1],[-1,0],[1,0]]
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]=='G':
                    for dx,dy in directions:
                        x,y=i+dx,j+dy
                        if (0<=x<m and 0<=y<n) and (matrix[x][y]==0 or matrix[x][y]==1):
                            while(0<=x<m and 0<=y<n):
                                if matrix[x][y]==0 or matrix[x][y]==1:
                                    matrix[x][y]=1
                                    x,y=x+dx,y+dy
                                else:
                                    break
        ans=0
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    ans+=1
        return ans