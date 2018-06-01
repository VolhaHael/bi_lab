import re

# Write a program to find all email addresses in string.
line_in_1 = 'hfhhde Volha_Hael@epam.com asdfv SDFSDF fdad _sdf olgagael@gmail.com'
for i in re.findall(r'[\w\.-]+@[\w\.-]+', line_in_1):
    print(i)
print()

# Write a prg to find all three, four, five characters long words in a string.
line_in_2 = 'I like cats of the Turkish Van breed.'
print(re.findall(r'\b\w{3,5}\b', line_in_2))
print()

# Write a program to separate and print the numbers of a given string.
line_in_3 = 'Avasd 10 adfahdf 34 adfaghafgh 123_as'
for i in re.findall(r'\d+', line_in_3):
    print(i)
print()

# Write a program to replace whitespaces with an underscore and vice versa.
line_in_4 = 'I like cats of the Turkish_Van breed.'
print(line_in_4)
line_in_4 = line_in_4.replace(" ", "_")
print(line_in_4)
line_in_4 = line_in_4.replace("_", " ")
print(line_in_4)
