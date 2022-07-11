n=int(input())
a=list(map(int,input().split()))
if a.count(1)+a.count(0)==n:
    print('True')
else:
    print('False')