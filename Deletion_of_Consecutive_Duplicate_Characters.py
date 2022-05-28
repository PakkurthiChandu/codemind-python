n=int(input())
for i in range(0,n):
    a=input()
    b=''
    for i in  range(0,len(a)-1):
        if(a[i]!=a[i+1]):
            b+=a[i]
    print(len(a)-len(b)-1)
        