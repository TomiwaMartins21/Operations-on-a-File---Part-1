# Program to remove lines starting with any prefix

file1 = open ('Codingal.txt', 'r')

file2 = open('CodinaglUpdated.txt', 'w')

# reading each line from orginal 
# text file
for line in file1.readlines():
        # reading all lines that do not 
        # begin file "Coding"
        if not (line.startswith('Coding')):

                # print those lines
                print(line)

                # storing only those lines that
                # do not begin with "Coding"
                file2.write(line)

# close and save the files
file2.close()
file1.close()