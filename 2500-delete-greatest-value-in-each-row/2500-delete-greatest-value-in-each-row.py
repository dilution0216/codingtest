class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        answer = 0
    
        while grid and grid[0]:
            # 1 각 행의 가장 큰 값을 삭제하고, 이 값들을 저장
            deleted_values = []
            for row in grid:
                max_val = max(row)
                row.remove(max_val)
                deleted_values.append(max_val)
            
            # 2: 저장된 값들 중 가장 큰 값을 answer에 추가
            answer += max(deleted_values)
        
        return answer
        