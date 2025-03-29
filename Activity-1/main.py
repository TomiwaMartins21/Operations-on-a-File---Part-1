# open file and read its contents
file = open('Activity-1\Codingal.txt','r')
print(file.read())
file.close()

# open file and read its beginning 8 characters
file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file 
file = open('Codingal.txt','a')
file.write("H1! I am Tomiwa and I am 14 yr old.")
file.close()