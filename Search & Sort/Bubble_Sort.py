# n=eval(input("Enter no of elementu to read: "))
# a=[]
# for i in range(0,n):
#     value=input("read the values: ")
#     a.append(value)
# # Itarating the loop from 0 to n-1. Because since after each pass,
# # the largest unsorted element "bubbles up" to its correct position,
# # so we don't need to check the last element
# for i in range(0,n):
    
# # The inner loop iterates through the unsorted part of the array.
# #Initially, you need to compare and swap the 1st ele with the 2nd,
# #the 2nd with the 3rd, and so on. After each pass of the outer loop,
# #the largest element gets "bubbled up" to its correct position
# #at the end of the array, so you don't need to recheck it.
# # so finally we need to decrement the no. of iterations in the inner loop by 'i' to avoid unnecessary comparisons and swaps.

#      for j in range(0,n-1-i):
        
#         if a[j]>a[j+1]:
#             a[j], a[j+1]=a[j+1],a[j]
# print("Sorted array elements :",end="")
# for j in range(0,n):
#     print(a[j],end=" ")


a = [23,5,35,-2,64,8,34,99,-99]

for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1],a[j]

for i in range(len(a)):
   print(a[i],end=" ")
