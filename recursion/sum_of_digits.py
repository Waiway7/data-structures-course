
def sum_of_digits(num: int) -> int:
    
    if (num / 10) < 1:
        return num
    
    return num % 10 + sum_of_digits(num // 10)

    
print (sum_of_digits(598))