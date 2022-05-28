n=int(input())
for i in range(0,n):
    k=int(input())
    a=input()
    for i in range(0,k):
        if a.count(a[i])==1:
            print(a[i])
            break
    else:
        print('-1')