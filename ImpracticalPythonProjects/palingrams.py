""" Playing with palingrams in Cpt 2. of the book

"""
import load_dictionary

word_list = load_dictionary.load("2of12.txt")

# for word in word_list:
#     print( word)
pali_list = []


# a_word = "tesco"
# print(a_word[::-1])
# print('gh')

# for word in word_list:
#     if len(word) > 1 and word == word[::-1]:
#         pali_list.append(word)
#
# print(*pali_list, sep = ",")  # <= here, the * ('splat') makes list print nicely like this

# word = "nurses"
# print(word[:2])
# rev = word[::-1]
# print(rev)
""" load word
    check its length
    
"""
# this prints backwards, but less so each time
# for i in range(len(word)):
#     print(word[:i:-1])
#
# # I want to print forwards one more so each time, from first two letters
# for i in range(len(word)):
#     print(word[:i+1]) # <= works nicely

# palingrams = []
# no_chars = len(word)
# if no_chars > 1:
#     a_str = word[0]
#     for i in range(1,no_chars-1):
#         a_str += word[i]
#         if a_str[::-1] in word_list:
#             palingrams.append(word + " " + a_str[::-1])

# word_list = ['bib', 'cheddar', 'bother', 'nurses', 'grits', 'stir', 'skins', 'pear', 'tea', 'on', 'no', 'dear',
#              'rabbit', 'run', 'eat', 'flog', 'golf', 'stack', 'cats', 'run']
word_list = load_dictionary.load("2of12.txt")
# print(word_list)
whatever= set()
for word in word_list:
    no_chars = len(word)
    if no_chars > 1:
        #'nurses run'-type
        core = ""
        for i in range(no_chars):
            core += word[i]
            reverse = core[::-1]
            remainder = word[i+1:]
            if remainder == remainder[::-1] and reverse in word_list and len(reverse) > 3: # first part checks the remainder is a palindrome/symmetrical
                whatever.add(word + " " + reverse)

        #'stir grits'-style
        core = ""
        for j in range(no_chars):
            core += word[len(word)-j-1]
            remainder = word[:len(word)-j-1]
            if remainder == remainder[::-1] and core in word_list and len(core) > 3: # first part checks the remainder is a palindrome/symmetrical
                whatever.add(core + " " + word)


whatever2 = list(whatever)
whatever3 = sorted(whatever2)

with open('foo.txt', 'w') as f:
    for item in whatever3:
        f.write("{}\n".format(item))

