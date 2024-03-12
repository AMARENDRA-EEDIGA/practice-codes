n=int(input("Enter some numbers:")) # Example: 14641
rev=0
temp=n
while temp>0:
     rem=temp%10 # 14641%10 = 1
     rev=(rev*10)+rem # (0*10)+1 = 1
     temp=temp//10 # 1464
if rev==n: # 
    print(n,"is a Pallindrome Number")
else:
    print("This is not a Pallindrome number. Please try again")

    
