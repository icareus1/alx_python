def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=lambda key: a_dictionary[key])
    # if not a_dictionary:
    #     return None
    # max_key = None
    # max_value = None
    # for key, value in a_dictionary.items():
    #     if max_value is None or value > max_value:
    #         max_key = key
    #         max_value = value
    # return max_key