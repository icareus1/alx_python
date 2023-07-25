def no_c(my_string):
    strList = list(my_string)
    for i in range(len(strList)):
        if strList[i] == 'C' or strList[i] == 'c':
            strList[i] = ''
    return "".join(strList)