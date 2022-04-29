a=int(input())
c=0
if a==1:
    print("not a prime")
else:
    for  i in range(2,a):
        if a%i==0:
            print("not a prime")
            c=1
            break;
    if c==0:
        print("prime")