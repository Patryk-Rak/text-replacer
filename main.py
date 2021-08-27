import re

mylines = []  # Declare an empty list named mylines.
mylines2 = [] # Declare an empty list named mylines2.



with open ('Language2.txt', 'rt', encoding="utf16") as myfile:  # Open lorem.txt for reading
    for txtline in myfile:  # For each line, stored as myline,


        regex = re.compile('=')
        if (regex.search(txtline) == None):
            new_line = txtline
        else:
            old_line = txtline
            new_line = old_line.split('=')[1]
        mylines.append(new_line)  # add its contents to mylines.
    print(mylines)  # Print the list.      # and print the string.

with open('Language2.txt', 'rt', encoding="utf16") as myfile2:  # Open lorem.txt for reading
    for txtline2 in myfile2:  # For each line, stored as myline,

        regex = re.compile('=')
        if (regex.search(txtline2) == None):
            new_line2 = txtline2
        else:
            old_line2 = txtline2
            new_line2 = old_line2.split('=')[0]+'='+'\n'
        mylines2.append(new_line2)  # add its contents to mylines.
print(mylines2)  # Print the list.      # and print the string.

with open('Language3.txt', 'w', encoding="utf16") as f:
    for line in mylines:
        if line == "":
            f.write("\n")
        else:
            f.write(line)

with open('Language4.txt', 'w', encoding="utf16") as f:
    for line2 in mylines2:
        if line2 == "":
            f.write("\n")
        else:
            f.write(line2)