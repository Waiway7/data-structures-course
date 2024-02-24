def sum_product(input_tuple):
    # TODO
    sum_tuple, product_tuple = 0, 1 
    
    for i in input_tuple:
        sum_tuple += i 
        product_tuple *= i 
    
    return sum_tuple, product_tuple