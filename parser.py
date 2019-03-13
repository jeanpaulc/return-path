import glob
import re

# set all the files from the extracted archive into a list
file_set = glob.glob('./smallset/*.msg')
# print(file_set)

# iterate through each file in the list
for file_path in file_set:
    # print(file_path)
    # open for reading
    with open(file_path, 'r') as read_file:
        print('File: ', read_file.name)

        with open('output.txt', 'w') as write_file:
            for line in read_file:
                # read each line and use regex to match 'Sent: ' dates
                date_pattern = re.compile(r'^Date:\s*(\D{3})?,?\s*(\d{1,2})\s*(\D{3})\s*(\d{4}).*')
                # date_pattern = re.compile(r'^Date:\s*')
                date_match = date_pattern.search(line)
                if date_match:
                    print(line)

                # read each line and use regex to match 'From: ' emails
                # from_pattern = re.compile(r'From:\s*(?:.*)\s*<(.*@.*)>')
                from_pattern = re.compile(r'From:\s*')
                from_match = from_pattern.match(line)
                if from_match:
                    print(line)

                # read each line and use regex to match 'Subject: ' lines
                subject_pattern = re.compile(r'Subject:\s*')
                subject_match = subject_pattern.match(line)
                if subject_match:
                    print(line)
