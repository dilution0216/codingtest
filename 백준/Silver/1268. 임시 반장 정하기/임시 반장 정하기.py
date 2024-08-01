def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  # 학생 수
    classes = []
    index = 1
    for i in range(n):
        student_classes = list(map(int, data[index:index + 5]))
        classes.append(student_classes)
        index += 5

    # 학생별로 몇 명과 같은 반이었는지 세기 위한 리스트
    same_class_count = [0] * n
    
    # 각 학생이 다른 학생들과 몇 번 같은 반이었는지 계산
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(5):
                    if classes[i][k] == classes[j][k]:
                        same_class_count[i] += 1
                        break
    
    # 가장 많은 학생들과 같은 반이었던 학생을 찾기
    max_count = max(same_class_count)
    for i in range(n):
        if same_class_count[i] == max_count:
            print(i + 1)
            break

if __name__ == "__main__":
    main()
