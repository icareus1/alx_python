def common_elements(set_1, set_2):
    sim_ele = set(filter(lambda x: x in set_2, set_1))
    return sim_ele