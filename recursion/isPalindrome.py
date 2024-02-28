def isPalindrome(strng):
    if len(strng) == 0:
        return True
    else:
        if (strng[0] != strng[-1]):
            return False
        return isPalindrome(strng[1:len(strng) - 1])