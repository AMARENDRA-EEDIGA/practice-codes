
given_string = "1one 2two 3three 4four 5five"
new_string =""
new_list = given_string.split()

for element in new_list:
    new_string = new_string + element[1:] + "-" + element[0] + " "

print(new_string)    
