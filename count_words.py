a=input()
c=a.lower()
b=c.split()
d=0
for i in range(0,len(b)):
    if(b[i][0]=='a' or b[i][0]=='e' or b[i][0]=='i' or b[i][0]=='o' or b[i][0]=='u') and (b[i][len(b[i])-1]!='a' or b[i][len(b[i])-1]!='e' or b[i][len(b[i])-1]!='i' or b[i][len(b[i])-1]!='o' or b[i][len(b[i]-1)]!='u'):
        d+=1
print(d)
        
