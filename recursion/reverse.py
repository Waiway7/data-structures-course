def reverse(string):
    
    if len(string) == 0:
        return ""
    return string[-1] + reverse(string[0:len(string) - 1])


print (reverse("python"))