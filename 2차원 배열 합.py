# 행렬의 크기 N, M 입력
N, M = map(int, input().split())

# 행렬 A 입력
matrix_A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 B 입력
matrix_B = [list(map(int, input().split())) for _ in range(N)]

# 행렬 덧셈 수행
result_matrix = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        result_matrix[i][j] = matrix_A[i][j] + matrix_B[i][j]

# 결과 출력
for row in result_matrix:
    print(' '.join(map(str, row)))
