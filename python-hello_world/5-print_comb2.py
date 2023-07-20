for i in range(100):
    number = "{:02d}".format(i)
    if i == 99:
        print(number)
    else:
        print(number, end=", ")