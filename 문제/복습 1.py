'''
white = list(map(int,input().split()))
answer = [1,1,2,2,2,8]
result = [answer[i] - white[i] for i in range(6)]
print(*result)
'''

'''별 찍기 
N = int(input())
for i in range(N+1):
    star = '*' *(2*i-1)
    space = ' ' * (N-i)
    print(space,star)
    
'''