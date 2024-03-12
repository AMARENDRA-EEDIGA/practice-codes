def count_factors(given_number):

    factor=1
    count=1

    # if  given_number==1:
    #     print(given_number," is not a prime number")
    # if  given_number==0:
    #     print(given_number," is not a prime number")
    #     return 0

    while factor < given_number:

        if given_number % factor==0:

            count = count+1

        factor = factor+1

    
    if count==2:
       print(given_number," is a prime number")


    return count


print(count_factors(0))
print(count_factors(1))
print(count_factors(2))
print(count_factors(29))
print(count_factors(24))
print(count_factors(13))
