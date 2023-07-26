def common_elements(set_1, set_2):
    # common_ele_set = set(filter(lambda x: x in set_2, set_1))
    # return common_ele_set
    common_ele_set = set_1 & set_2
    return common_ele_set