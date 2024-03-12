## 1.Method
n=int(input("Enter how many values: "))

#a=[]
a=[0]*n
# using for loop iterates up to given count of 'n' numbers
for i in range(n):
    # Reading the inputs by the user and store it into a variable called value
    value=int(input(""))
    # Using append method we can add each element into the 
    #a.append(value)
    a[i]=value
search=int(input("Read the search element is= "))

for i in range(n):
    if search==a[i]:
        print("Search ele found at= ",i)
        break;

    if i==n-1:
        print("Element is not found in the list...")

## 2.Method
n = int(input("Enter how many values: "))
a = []
# Initialize i outside the loop
i = 0
for i in range(n):
    value = int(input(""))
    a.append(value)
search = int(input("Read the search element: "))
for i in range(n):
    if search == a[i]:
        print("Search element found at index:", i)
        break
    if i == n - 1:
       print("Element is not found in the list...")
