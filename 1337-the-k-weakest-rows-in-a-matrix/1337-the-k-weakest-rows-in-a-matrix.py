class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 1. 각 행의 병사 수를 센다.
        soldier_counts = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
                else:
                    break  # 행렬의 조건에 따라 1 이후는 모두 0이므로 더 이상 셀 필요가 없음
            soldier_counts.append((i, count))
        
        # 2. 병사 수를 기준으로 정렬 (병사 수가 같으면 행 번호로 정렬)
        sorted_rows = sorted(soldier_counts, key=lambda x: (x[1], x[0]))
        
        # 3. 가장 약한 k개의 행의 인덱스를 반환
        weakest_rows = []
        for i in range(k):
            weakest_rows.append(sorted_rows[i][0])
        
        return weakest_rows