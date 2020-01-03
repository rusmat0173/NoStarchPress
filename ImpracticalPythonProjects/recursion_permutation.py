""" Finally a useful reason for recursion.
    Normally the recursion examples give (often factorials or Fibonnacci) are a bit theoretical,
    with not much practical use.

    However, it's a great way to generate permutations.  This file practices this a bit.

    Note,though, that a very helpful itertools module can probably do everything in permutations for you.
    This is practiced as well

"""
# having a go at itertools
import itertools
z = list(itertools.permutations([0,1,2,3,4,5,]))
# print("No. combinations: {}.".format(len(z)))
# print(*z[:5], sep = "\n")

# standard recursion example
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res

n = 5
# print("\nn! is {}: ".format(factorial(n)))

# this is one method from internet.  Gets confusing if you try print statements/counters, etc.
# Works for strings and lists, etc.
# Use as site like http://www.pythontutor.com/visualize.html#mode=display
def rec_perm(seq):
    # this methodology needs a if not seq, for the case where the string(e.g.) is ""
    if not seq:
        return [seq] # <= this will return "" if no letters left
    else:
        temp = []
        for i in range(len(seq)):
            part = seq[:i] + seq[i+1:]
            for j in rec_perm(part):
                temp.append(seq[i:i+1] + j)
        return temp

try_1 = rec_perm("ABC")
try_1 = rec_perm([0,1,2])
print(try_1)

# another method from internet, adapted. I like this, very simple and elegant.
# The if, else is basically the same as above.
# ONLY WORKS for a string, the above works for lists, also.
def permute(word):
    return_list=[]
    if len(word) == 1:
        # There is only one possible permutation
        return_list.append(word)
    else:
        # Return a list of all permutations using all characters
        for i in range(len(word)):
            permute_list=permute(word[0:i]+word[i+1:len(word)])
            for item in permute_list:
                return_list.append(word[i]+item)
    return return_list

print(permute("Sand"))