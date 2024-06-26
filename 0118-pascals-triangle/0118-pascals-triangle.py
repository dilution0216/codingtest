class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        for i in range(numRows):
            row = [0] *(i+1)
            row[0],row[-1] = 1,1
        
            for j in range(1,len(row)-1):
                row[j]=tri[i-1][j-1] + tri[i-1][j]
            tri.append(row)
    
        return tri