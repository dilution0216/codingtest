class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # 1. 2D 행렬을 1D 리스트로 변환
        flat_list = [num for row in grid for num in row]
        
        # 2. 리스트를 정렬
        flat_list.sort()
        
        # 3. 음수의 개수 세기
        negative_count = sum(1 for num in flat_list if num < 0)
        
        return negative_count

        