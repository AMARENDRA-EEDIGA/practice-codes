
# Armstrong Numver: "a number that is equal to the sum of cubes of its digits".
n = int(input("Enter a number to check an Armstrong number: ")) # Ex: 153

b=n # storing given number in a variable "b"

length = len(str(n)) # length=3
# Here need to find the no. of digits in it.
# here if we not convert it into string we will get an error[TypeError: object of type 'int' has no len()]

Sum = 0
while n!=0:

# by dividing with %(modulo) we will get last element
    rem = n%10 # 153%10 = 3
    
    Sum = Sum +(rem**length) # 0+(3**3)=27, 27+(5**3)=27+125, 152+(1**3)=153
    
    n=n//10 # 153//10=15, 15//10=1, 1//10=1

if b == Sum:  # 153=153
    print("Armstrong Number...")# True
else:
    print("Not an Armstrong")
    
