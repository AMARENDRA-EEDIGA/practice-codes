n=int(input("Enter how many values need: "))

a=[]

for i in range(0,n):
    value=int(input(""))
    a.append(value)

search=int(input("Read the search element= "))

first=0
last=n-1
while first<=last:
    mid=(first+last)//2

    if a[mid]>search:
        last = mid-1
        
    elif a[mid]==search:
        print("Search element found at ", mid+1)
        break
    
    else:
        first=mid+1
        
if first>last:
    print("Search element is not found in the list...")

## Note:= For a binary search to work correctly, the list must be sorted befor searching.        
