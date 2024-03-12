def pattern( num):
    # for i in range(1,num+1):
    #     for j in range(1,num+1):
    #         if  j==1 or j==num or i==1 or i==num or i+j==num+1 or i==j:
    #             print("*",end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()


    # for i in range(1,num+1):          
    #     for j in range(1,i+1):             
    #         print("*", end=" ")       
    #     print()  

    # for i in range(1,num+1):          
    #     for j in range(1,num+2-i):             
    #         print(num+1-i, end=" ")       
    #     print()  

    for r in range(1,num+1):
        for c in range(1,num+1):
            if c<r:
              print(" ",end=" ")
            else:
               print(c,end=" ")
        print()
                       
pattern(5)

#=======
def staircase(n):
    # Write your code here
    for row in range(1,n+1):
        for col in range(n):
            if row+col==n or row+col>n:
                print("#",end="")  
            else:
                print(" ",end="")
        print()
staircase(4)
Output:
   #
  ##
 ###
####       

