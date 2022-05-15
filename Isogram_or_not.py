a=input()
for i in range(0,len(a)):
    if a.count(a[i])!=1:
        print('False')
        break
else:
    print('True')