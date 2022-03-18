# write a function to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# example: input is
# "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1


def frequency(input):
    freq = {}

    for word in input.split():
        freq[word] = freq.get(word, 0) + 1

    words = list(freq.keys())
    words.sort()

    for w in words:
        print(f'{w}:{freq[w]}')
frequency('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')

