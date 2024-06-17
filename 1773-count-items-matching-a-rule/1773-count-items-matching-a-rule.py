class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # type, color, name 의 인덱스는 순서대로 0,1,2
        # 1. rulekey 값을 확인한다.
        # 2. 그에 맞는 인덱스를 설정한다.
        # 3. 각 키의 인덱스를 확인하고, 일치할 경우 카운팅한다.
        # 4. 카운팅된 값을 리턴한다.
        result = 0
        id = 0
        if ruleKey == "type":
            id = 0
        elif ruleKey == "color":
            id = 1
        else:
            id = 2
        for i in items:
            if i[id] == ruleValue:
                result += 1
        return result        
                
            