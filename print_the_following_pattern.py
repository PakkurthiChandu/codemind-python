a=int(input())
for i in range(a,0,-1):
    for j in range(1,i+1):
        print("%c"%(64+i),end=' ')
    print()