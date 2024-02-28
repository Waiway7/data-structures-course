def decimalToBinary(num):
    if (num == 0):
        return 0
    print (num%2)
    return num % 2 + 10 * decimalToBinary(num // 2)

'''
0
0 * 10 + 1 = 1
1 * 10 + 0 = 10
1 + 10 * 10 = 101
0 + 10 * 101 = 1010
'''

print (decimalToBinary(13))