# open the file in read mode 
file_read = open('Activity-2\Codingal.txt','r')
print("File in Read mode -")
print(file_read.read())

# open the file in write mode 
file_write = open('Activity-2\Codingal.txt', 'w')
# write in the file
file_write.write("File in write mode ....")
file_write.write("Hi! I am Tomiwa. I am 15 yr . old")
file_write.close()

# open the file in append mode
file_append = open('Activity-2\Codingal.txt', 'a')
# append in the file
file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Tomiwa. I am 15 yr. old")
file_append.close()