def x_figure(salary):

    tally = 0

    if salary==0:

        tally += 1

    while salary >=1:

        salary = salary/10

        tally += 1

    return tally

print(x_figure(230000032))
