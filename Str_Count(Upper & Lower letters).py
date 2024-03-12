
def String_test(str1):
    lower = 0
    upper = 0
    for char in str1:

        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1

        else:
            pass
    print("Upper Case letters are: ",upper)
    print("Lower case letters are: ", lower)
String_test("Hello Amarendra. What's up. Is It Ok")
