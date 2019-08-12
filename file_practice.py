# open a file for writing and create it if it doesn't exits
#file_handle = open("textfile.txt", 'w+')

#Open the file for appending text to the end
#file_handle = open("textfile.txt", "r")

#Write some line of data to the file
#for i in range(10):
#    file_handle.write("This is line " + str(i) + "\n")

#Open the file back up and read the content
#if file_handle.mode == 'r':
#    contents = file_handle.read()
#    print(contents)

#Close the file when done
#file_handle.close()

file = open("weird.txt", 'r+')

file.write("Hello")
print(file.readlines(-1))