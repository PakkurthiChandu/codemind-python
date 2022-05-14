a=list(map(str,input().split()))
for i in range(0,len(a)):
    print(a[i].count('a')+a[i].count('e')+a[i].count('i')+a[i].count('o')+a[i].count('u'),end=' ')