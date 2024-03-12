l=[6,3,6,6,9,0,8,4,3,5]
sum=0
total=0
for num in l:
    if num%2==0:
        sum+=1
        total=total+num
        print(num,"is Even Number")
print("Count of Even numbers=",sum)
print("Sum of all even numbers= ",total)
# for num in l:
#     if num%2==0:
#         print(num,"is Even Number")
#     else:
#         pass
