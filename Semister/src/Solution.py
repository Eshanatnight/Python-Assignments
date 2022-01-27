"""

Name: Eshan Chatterjee
Roll No.: 11500119069

"""


"""
Question 18: Write a python program to keep first two occurrences of an element from
a list of integers without changing the order of occurrences.

Input1:  1 4 6 8 2 2 4 6 8 9 8 1 2 2      Output: 1 4 6 8 2 2 4 6 8 9 1

Input 2:  2 2 2 2 2 2 1 1            Output2: 2 2 1 1

Input3:  1 3 3 3 3 3 3           Output3: 1 3 3
"""

#test_list = [1, 4, 6, 8, 2, 2, 4, 6, 8, 9, 8, 1, 2, 2]
#test_list = [2, 2, 2, 2, 2, 2, 1,1]
test_list = [1, 3, 3, 3, 3, 3, 3]

'''
test_list = []
chk = True
count = 0

while chk:
    count += 1
    print("Enter Integer Element")
    test_list.append(int(input()))

    if(count > 4):
        print("Finshed adding? (y\\n)")
        inp = input()
        if(inp == "y" or inp == "Y"):
            chk = False
'''
print( "Original List is: " + str(test_list))
final_list = []

for elem in test_list:
    count = test_list.count(elem)
    if (count > 2):
        final_list.append(elem)
        if (final_list.count(elem) > 2):
            final_list.pop()

    else:
        final_list.append(elem)

print("Final List is: " + str(final_list))