def gcd(num, num2):
    min_num = min(num, num2)
    max_num = max(num, num2)
    if max_num % min_num == 0:
        return min_num
    else:
        return gcd(max_num % min_num, min_num)
    
print (gcd(48, 18))