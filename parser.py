import glob
import re

# set all the files from the extracted archive into a list
file_set = glob.glob('./smallset/*.msg')

# iterate through each file in the list
for file_path in file_set:
    # print(file_path)
    # open for reading
    with open(file_path, 'r') as rf:
        with open('output.txt', 'a') as af:
            af.write('\n' + rf.name + '\n')

            for line in rf:
                # read each line and use regex to match 'Sent: ' dates
                date_pattern = re.compile(r'^Date:\s*(\D{3})?,?\s*(\d{1,2})\s*(\D{3})\s*(\d{4}).*')
                date_match = date_pattern.search(line)
                if date_match:
                    # remove Date key and write value to file
                    af.write(line.split('Date:')[1].strip() + '\n')

                # read each line and use regex to match 'From: ' emails
                from_pattern = re.compile(r'From:\s*')
                from_match = from_pattern.match(line)
                if from_match:
                    # find email in the line
                    email_pattern = re.compile(r'<?([\w.-]+@[\w.-]+[^>\s])')
                    email = re.search(email_pattern, line).group(1)
                    # write email to file
                    af.write(email + '\n')

                # read each line and use regex to match 'Subject: ' lines
                subject_pattern = re.compile(r'^Subject:\s*', re.M)
                subject_match = subject_pattern.match(line)
                if subject_match:
                    # remove Subject key and write value to file
                    af.write(line.split('Subject:')[1].strip() + '\n')
                
                
