
# The function should reverse the keys and values to show which 
# categories (values) each resource (key) belongs to. 

def invert_resource_dict(resource_dictionary):
    
  # Initialize a "new_dictionary" variable 
    new_dictionary = {}
    
    # The outer for loop iterates through each "resource_group" and 
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        
        # The inner for loop iterates over each "resource" value in 
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            
            # The if-statement checks if the current "resource" value has 
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
                
            # If False (else), then add the "resource" as a new key with the 
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed  
    # all iterations.
    return(new_dictionary)


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}


#Question: The groups_per_user function receives a dictionary, which contains group names with the list of users.
#Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of
#their groups as values.


# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	# Go through group_dictionary
# 	for group_list, users in group_dictionary.items():
# 		# Now go through the users in the group
# 		for user in users:
# 			if user in user_groups:
# 				user_groups[user].append(group_list)
# 			else:
# 				user_groups[user] = [group_list]
# 			# Now add the group to the the list of
#                         # groups for this user, creating the entry
#                         # in the dictionary if necessary

# 	return(user_groups)

# print(groups_per_user({"local": ["admin", "userA"],
#                        "public":  ["admin", "userB"],
# 		        "administrator": ["admin"] }))





