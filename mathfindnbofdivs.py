x=int(input('Give a number'))
la=[]
i=1
while i<=x:
    d=x/i
    y=x//i
    if d==y:
        la.append(i)
    else:
        la=la
    i+=1
print(la)
n=len(la)
print(n)



