# 테스트 케이스의 개수 T 입력 받기
T = int(input())

# T번 반복
for _ in range(T):
    # A와 B 입력 받기
    A, B = map(int, input().split())
    
    # A+B 출력
    print(A + B)
