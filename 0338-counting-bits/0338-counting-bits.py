class Solution:
    def countBits(self, n: int) -> List[int]:
        # result 리스트를 길이 n+1로 초기화하고, 모든 값을 0으로 설정
        result = [0] *(n+1)
        # 1부터 n까지 각 숫자 i 에 대해 2진수의 1의 개수를 계산
        # 
        for i in range(1, n + 1):
            # i >> 1은 i를 2로 나눈 값과 동일 (즉, 오른쪽으로 1 비트 이동)
            # i & 1은 i의 가장 오른쪽 비트가 1인지 0인지 확인
            result[i] = result[i >> 1] + (i & 1)
        
        # 최종 결과 반환
        return result
