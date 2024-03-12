
# This function returns the total time, with minutes represented as 
# decimals (example: 1 hour 30 minutes = 1.5)
def sum_server_use_time(Server):

    #Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes
    total_use_time = 0
    # Iterate through the "Server" dictionary’s key and value items 
    # using a for loop.
    for key,value in Server.items():

        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[value]
        
    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)  

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer)) # Should print 20.1
        

