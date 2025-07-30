n=int(input("enter the no"))
z=str(n)
if len(z)<2:
    print("the no should have two digits")

x=z[:-2]+z[-1]+z[-2]
print(x)