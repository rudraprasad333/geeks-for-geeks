#Write a function that takes a string, integer, and float as input and returns them as a tuple in the format (string, integer squared, float round
# ed to 2 decimals)
'''
def check(x,y,z):
    tuple1=(x,y,z)
    return tuple1
x=input("enter the string value")
y=int(input("enter the integer value"))
z=float(input("enter the float value"))
print(check(x,y,z))

#Write a function that returns True if the sum of two given numbers is even, and False otherwise.
def check_sum(sum):
    if  sum%2==0:
        return True
    else:
        return False
x=int(input("enter the number"))
y=int(input("enter the number"))
sum=x+y
print(check_sum(sum))

def positive(x):
    if x>0:
        return("positive")
    elif x<0:
        return("negative")
    else:
        return("zero")
    
x=int(input("enter the number"))
print(positive(x))

#Write a function that prints all even numbers from 1 to 50 using a while loop.
def print_even():
    evennumber=[]
    z=1
    while z!=50:
        if z%2==0:
            evennumber.append(z)
        z=z+1
    return(evennumber)    
print(print_even())

#Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
import math
def isprime(n):
    for i in range(2,int(math.sqrt(n)+1)):
       if n%i==0:
           return False
           
           
    return True
           
n=int(input("enter the number"))
print(isprime(n))

#Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def oddlist(x):
    odd=[]
    for i in x:
        if i%2!=0:
            odd.append(i)
    return(odd)
n=int(input("enter the no of elements you want to enter"))
x=[]
for i in range(0,n):
    z=int(input("enter the numbers you want to enter"))
    x.append(z)
print(oddlist(x))

#Write a function that accepts a tuple of numbers and returns the maximum and minimum values.
def find(x):
    return(max(x),min(x))
    

    
    

list=[]
n=int(input("enter the number of elements "))
for i in range(n):

    x=int(input("enter the valuee for tuple"))
    list.append(x)
tuple(list)
print("maximum",find(list))
print("minium",find(list))

#Write a function that takes two lists and returns the common elements using set operations.
def common(x,y):
    clist=[]
    for i in x:
        for j in y:
            if i==j:
                clist.append(i)
    return(clist)
x=[]
y=[]
n=int(input("enter the no elements in x"))
for i in range(n):
    z=int(input("enter the values in x list "))
    x.append(z)
no=int(input("enter the no elements in y"))
for j in range(no):
    f=int(input("enter the elements in y"))
    y.append(f)
print("the common elements in a set is ",common(x,y))

#Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).

def ispalindrome(z):
    y=z[::-1]
    if z==y:
        return True
    else :
        return False
x=input("enter the string which you want to check")
if ispalindrome(x):
    print("the given is a palindrome ")
else :
    print("is not a palindrome")
'''
def isPalindrome(self, x):
         if self==x:
            return True
         else:
            return False
self=input("enter the no you want to enter") 
x=self[::-1]
print("The given number is a palindrome",isPalindrome(self,x))  
