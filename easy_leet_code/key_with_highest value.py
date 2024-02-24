def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)
    # TODO
    key, max_value = None, 0
    for k, v in my_dict.items():
        if v > max_value:
            key = k
            max_value = v 
    return key

my_dict = {'a': 5, 'b': 9, 'c': 2}
print (max_value_key(my_dict))