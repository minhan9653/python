submitted_numbers = set()

# 출석번호를 28명만큼 입력받아 세트에 추가
for _ in range(8):
    student_number = int(input())
    submitted_numbers.add(student_number)

# 누락된 출석번호 찾기
missing_numbers = list(set(range(1, 11)) - submitted_numbers)

# 누락된 출석번호 오름차순 정렬 후 출력
missing_numbers.sort()
print(missing_numbers[0])  # 가장 작은 출석번호
print(missing_numbers[1])  # 그 다음 출석번호

