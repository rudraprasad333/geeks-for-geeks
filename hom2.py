 n=int(input("enter the no"))
y=int(input("enter the no"))
string1=str(n)
string2=str(y)
z=string1[:-1]+string2[-1]
f=string2[:-1]+string1[-1]
int1=int(z)
int2=int(f)
product=int1*int2
print(product)
print(z)
print(f)