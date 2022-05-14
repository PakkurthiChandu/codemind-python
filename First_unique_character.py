a=input()
for i in range(0,len(a)):
    if a.count(a[i])==1:
        print(a[i])
        break
else:
    print('-1')