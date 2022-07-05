a=int(input())
b=a*a
n=len(str(a))
b=str(b)
c=b[(len(b)-n):len(b)]
c=int(c)
if a==c:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
