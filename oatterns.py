x=5
y=6
z=9
n=5
next=[(i,j,k) for i in range(5)  for j in range (y) for k in range (z) if (i+j+k)!=n]
print(next)