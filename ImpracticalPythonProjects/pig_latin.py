""" This is the Pig Latin exercise, in  Cpt1.

"""
base_word = input("Enter a word that begins with a consonant> ")
pig_latin = base_word[1:] + base_word[0] + "ay"
print(pig_latin)

