""" Project Euler Q68.
    First repeating the Magic 3-gon ring in the example.
    Use as a template for a Magic 5-gon ring.

"""
from itertools import permutations

# get list of permutations (from internet)
perms = [''.join(p) for p in permutations('123456')]
print("No. combinations: {}.".format(len(perms)))
# print(perms[:10])

# find the 'arms' that are of equal magnitude and create valid_perms
valid_perms = []
for p in perms:
    tot_arm_1 = int(p[0]) + int(p[1]) + int(p[2])
    tot_arm_2 = int(p[3]) + int(p[2]) + int(p[4])
    tot_arm_3 = int(p[5]) + int(p[4]) + int(p[1])
    if tot_arm_1 == tot_arm_2 == tot_arm_3:
        temp = [p[0]+p[1]+p[2], p[3]+p[2]+p[4], p[5]+p[4]+p[1]]
        temp.sort()
        valid_perms.append(temp)

# need to remove duplicates (from internet)
permutations = []
[permutations.append(x) for x in valid_perms if x not in permutations]
# print(permutations)

# we can sort the permutations as each starting arm is unique.
# N.B. as question says we want the highest starting permutation, so we simply sort and take highest
permutations.sort()
highest = permutations[-1]
print(highest)

# In 'highest', we need to check if the elements are in correct sequence. (First one is fine.)
if highest[0][2] != highest[1][1]:
    temp = [highest[0], highest[2], highest[1]]
    highest = temp
print("Highest sequence is {}".format(highest))

# search function to find key in list of permutations (from internet)
def linear_search(_list, key):
    for item in range(len(_list)):
         if key in _list[item][1]:
             return _list[item]
    return -1

# in the Magic 3-gon ring there are 3 arms
no_arms = 3



# for p in permutations:
#     key = p[2]
#     output = p.pop(0)
#     for i in range(no_arms - 1):
#         new_entry = linear_search(permutations, key)
#         print(new_entry)
#         key = new_entry[2]
#         output += new_entry
#         permutations.remove(new_entry)
#
#     print(output)


# for i in range(no_arms - 1):
#     new_entry = linear_search(permutations, key)
#     print(new_entry)
#     key = new_entry[2]
#     output += new_entry
#     permutations.remove(new_entry)
#
# print(output)


