# This method will perform on checking only the factors of 1 and itself. Otherwise it will break then it returns Not a prime.
n = 23
c = 2
# Here i am checking form 2 to n with while loop, Because prime numbera starts from 2 to.....
while(c<n):
    # If the number have the factors except 1 and itself. It breaks tihs loop. Because a Prime number does't have more than 2 factors
    if(n%c==0):
        break
    # I am increasing the c value upto number n.
    c+=1
# Here i am checking if the numbre have only 2 factors, then it is a prime number. else......
if n==c:
    print("prime")
else:
    print("Not a prime")

# This method will perform on number of Factors...
n = 88
No_of_Factors = 0
start =1

# Here i am checking form 1 to n with while loop
while(start<=n):

    # Here i am checking if the number have how many factors, 
    if n%start==0:

        # here i am storing the no. of factors into 'sum
        No_of_Factors+=1

    # I am increasing the start value upto number n.
    start+=1

# Here i am checking if the No_of_Factors == 2 then it is Prime Otherwise NOt
if No_of_Factors==2:
    print("Prime")

else:
    print("Not a prime")


