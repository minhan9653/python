numbers = [int(input()) for _ in range(9)]  # 9개의 자연수 입력받기
max_value = max(numbers)  # 최댓값 찾기
max_index = numbers.index(max_value) + 1  # 최댓값의 위치(인덱스) 찾기

print(max_value)  # 최댓값 출력
print(max_index)  # 최댓값의 위치(인덱스) 출력
