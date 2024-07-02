class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # 매핑 딕셔너리를 생성합니다.
        mapping = {}
        current_char = 'a'
        
        for char in key:
            # 공백이 아니고 아직 매핑되지 않은 문자일 경우
            if char != ' ' and char not in mapping:
                mapping[char] = current_char
                current_char = chr(ord(current_char) + 1)
                if current_char > 'z':  # 'z'를 초과하면 멈춥니다.
                    break
        
        # 매핑을 사용하여 메시지를 해독합니다.
        decoded_message = []
        for char in message:
            if char == ' ':
                decoded_message.append(' ')
            else:
                decoded_message.append(mapping[char])
        
        return ''.join(decoded_message)