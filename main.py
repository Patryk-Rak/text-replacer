import re

mylines = []                             # Declare an empty list named mylines.


with open ('Language2.txt', 'rt', encoding="utf16") as myfile:  # Open lorem.txt for reading
    for txtline in myfile:  # For each line, stored as myline,


        regex = re.compile('=')
        if (regex.search(txtline) == None):
            new_line = txtline
        else:
            old_line = txtline
            new_line = old_line.split('=')[1].lstrip()


        # old_line = txtline
        # new_line = old_line.split('=')[0].lstrip()
        mylines.append(new_line)  # add its contents to mylines.
print(mylines)  # Print the list.      # and print the string.

with open('Language3.txt', 'w', encoding="utf16") as f:
    for line in mylines:
        if line == "":
            f.write("\n")
        else:
            f.write(line)