# using the function
def odd_numbers(n):
    return [x for x in range(n+1) if x%5==0 ]
print(odd_numbers(100))
print(odd_numbers(-1))
print(odd_numbers(0))

# using a variable

result=[x for x in range(0,101) if x%5==0 ]
print(result)


# Long form for loop with nested if-statement

my_list = []
for x in range(0,101):
  if x % 5 == 0:
    my_list.append(x)
print(my_list)

