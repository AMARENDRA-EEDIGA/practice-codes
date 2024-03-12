# n = 5
# for i in range(0,n):

#     for j in range(0,i+1):
#        print("* ",end=" ")

#     print("\n")   

string = "mom omom"
white = string.replace(" ","")
print(white)
rev = white[::-1]
if white==rev:
    print("Palindrom")
else:
    print("NOt a palindrom")
# print(white)