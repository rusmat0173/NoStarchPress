""" This is the Poor Man's Bar Chart exercise, in  Cpt1.
    Is done without pprint and collections/defaultdict
    that the author uses.

    FOR BLOG: split string over several lines. (See analyse_string)
    
"""

analyse_string = "The USA Network television channel once ran a detective dramedy called Psych, \n" \
                 "in which hyper-observant amateur sleuth Sean Spencer solved cases while pretending \n" \
                 "to use psychic abilities."

not_wanted = " ',.!?()[]@#~><0123456789"
short_string01 = analyse_string.lower()
short_string02 = ''
for char in short_string01:
    if char not in not_wanted and char != "\n":
        short_string02 += char
set_of_letters = set(short_string02)
letter_dictionary = {}
for letter in set_of_letters:
    letter_dictionary[letter] = []
for letter in short_string02:
    letter_dictionary[letter].append(letter)

alphabet= "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    if letter in letter_dictionary.keys():
        print(letter + ": " + str(letter_dictionary[letter]))