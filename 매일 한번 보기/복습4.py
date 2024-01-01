T,M=map(int,input().split())
if M >=45 :
    Minute=M-45
    print(T,Minute)
else :
    T=T-1 
    Minute = M+15
    print(T,Minute)