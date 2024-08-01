def main():
    import sys
    input = sys.stdin.read
    
    data = input().splitlines()
    total_score = 0.0  # 총 학점
    total_credit = 0.0  # 총 학점 수
    grade_dict = {
        "A+": 4.5, "A0": 4.0,
        "B+": 3.5, "B0": 3.0,
        "C+": 2.5, "C0": 2.0,
        "D+": 1.5, "D0": 1.0,
        "F": 0.0
    }
    
    for line in data:
        parts = line.split()
        course = parts[0]
        credit = float(parts[1])
        grade = parts[2]
        
        if grade in grade_dict:
            total_score += credit * grade_dict[grade]
            total_credit += credit

    if total_credit > 0:
        gpa = total_score / total_credit
    else:
        gpa = 0.0

    print(f"{gpa:.6f}")

if __name__ == "__main__":
    main()
