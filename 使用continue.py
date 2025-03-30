s=0
i=1
while i<=100:
    a=i%2
    if a==1:
        i=i+1
        continue
    else:
        s=s+i
    i=i+1 
print(s)

q=0
f=1
for r in range(1, 101):
    v=r%2
    if v==1:
        continue
    q+=r   
print(q)    