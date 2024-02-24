def count_word_frequency(words):
    # TODO
    freq = {}
    for i in words:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print (count_word_frequency(words))