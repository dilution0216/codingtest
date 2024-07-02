class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 결과를 담을 배열을 prices로 초기화
        answer = prices[:]
        stack = []
        
        # 배열을 순회하면서
        for i in range(len(prices)):
            # 스택이 비어있지 않고, 현재 가격이 스택의 마지막 가격보다 작거나 같으면
            while stack and prices[stack[-1]] >= prices[i]:
                # 해당 인덱스에 대한 할인을 현재 가격으로 적용
                index = stack.pop()
                answer[index] -= prices[i]
            # 현재 인덱스를 스택에 추가
            stack.append(i)
        
        return answer