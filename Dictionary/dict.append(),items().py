# This function receives a dictionary, which contains common employee 
# last names as keys, and a list of employee first names as values. 
# The function generates a new list that contains each employees’ full

def list_full_names(employee_dictionary):
    
    # Initialize the "full_names" variable as a list data type
    full_names = []

    # The outer for loop iterates through each "last_name" key and 
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in 
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:

            # Append the new "full_names" list with the last_name
            full_names.append(first_name+" "+last_name)
            
    # Return the new "full_names"
    return full_names

print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']


#The email_list function receives a dictionary, which contains domain names as
#keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

# def email_list(domains):
# 	emails = []
# 	for email,users in domains.items():
# 	  for user in users:
# 	    emails.append(user+"@"+email)
# 	return(emails)

# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
