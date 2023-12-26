A='*'
B=int(input())
for i in range(B+1):
    stars=A*i
    space=' ' * (B-i)
    print(space,stars)