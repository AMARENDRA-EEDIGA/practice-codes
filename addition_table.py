def addition_table(given_number):

    iterated_number = 1
    my_sum = 1

    while iterated_number<=5:

        my_sum = given_number + iterated_number

        if my_sum > 20:

            break

        print(str(given_number), "+", str(iterated_number), "=",str(my_sum))


        iterated_number+=1

addition_table(5)
addition_table(17)
addition_table(30)




