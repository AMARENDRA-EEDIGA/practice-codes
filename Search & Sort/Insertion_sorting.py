n=int(input("Enter how many values need: "))
a=[]
print("Reading the elements:=")
for i in range(0,n):
    value=int(input(""))
    a.append(value)
for i in range(1,n):
    # assigns the value of the element at the current position i in the list a to it.
    temp=a[i]
    # This line initializes a variable j to i - 1, which points to the element just before the current element temp.
    j=i-1

    # j >= 0: This condition ensures that we don't go out of bounds in the array. We want to keep moving left through the sorted portion of the list.
    # temp < a[j]: This condition checks if the temp value is smaller than the element at position j. If it is, we need to shift the element at position j one position to the right to make space for temp.
    while temp<a[j] and j>=0:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=temp

print("Sorted List is:= ",end="")
for i in range(0,n):
    print(a[i], end=" ")
    
