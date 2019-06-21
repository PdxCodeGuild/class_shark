# FileIO_example.py
# writes file
# creates file if the filename doesn't exist, or overwrites existing file
with open('filename.txt', 'w') as f: 
    print('Hello', 'World!', 123, file=f) 
    # # equivalent to above
    # f.write('Hello ' + 'World! ' + str(123) + '\n')

# reads file
with open('filename.txt') as f:
# with open('filename.txt', 'r') as f: # equivalent to above
    contents = f.read()

print(contents)

# writes file
# appends to file if the filename exists, or creates new file
with open('filename.txt', 'a') as f:
    f.write(str(123)) # no newline
    # print('another one', file=f)


print(contents.split('\n'))