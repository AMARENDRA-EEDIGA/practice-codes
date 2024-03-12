# By taking the condition it returns 
z=[x for x in range(0,101) if x%3==0]
# print(z)

## Normaly by using looping
my_list= []
for x in range(0,101):
     if x%3==0:
      my_list.append(x)
# print(my_list)



# Making the operation(x*3) with sequesce of numbers it returns
z=[x*3 for x in range(0,101)]
print(z)


## Normaly by using looping
my_list = []
for x in range(0,101):
   # if x%3==0:
     my_list.append(x*3)
print(my_list)
