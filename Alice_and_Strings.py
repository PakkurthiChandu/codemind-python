n=int(input())
for i in range(n):
    a=input()
    b=input()
    if len(a)==len(b):
        for j in range(len(a)):
            if(a[j]>b[j]):
                print('NO')
                break
        else:
            print('YES')
    else:
        print('NO')