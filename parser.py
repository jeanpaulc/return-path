import glob

# set all the files from the extracted gzip folder into a list
file_set = glob.glob('./smallset/*.msg')
print(file_set)

# iterate through each file in the list
for file_path in file_set:
    # print(i)
    # open for reading
    with open(file_path, 'r') as rf:
        print(rf.name, end='*')