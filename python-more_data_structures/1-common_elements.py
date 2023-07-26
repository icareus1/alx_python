def common_elements(set_1, set_2):
    sim_ele = set(filter(lambda x: x in set_1, set_2))
    return sim_ele