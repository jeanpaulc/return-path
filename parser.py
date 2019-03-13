import glob
import re

def file_set():
    # set all the files from the extracted archive into a list
    return glob.glob('./smallset/*.msg')

def date_search(string):
    # regex looks for RFC spec date/time matches; see RFC 5322, 3.3
    date_regex = re.compile(r'^Date:\s*(\D{3})?,?\s*(\d{1,2})\s*(\D{3})\s*(\d{4}).*')
    return date_regex.search(string)

def sender_search(string):
    sender_regex = re.compile(r'From:\s*')
    return sender_regex.match(string)

def email_search(string):
    email_regex = re.compile(r'<?([\w.-]+@[\w.-]+[^>\s])')
    return re.search(email_regex, string).group(1)

def subject_search(string):
    subject_regex = re.compile(r'^Subject:\s*', re.M)
    return subject_regex.match(string)

def main():
    # iterate through each file in the list
    for file_path in file_set():
        # open for reading; open new file for writing (append mode)
        with open(file_path, 'r') as file_reader, open('output.txt', 'a') as file_writer:
            # include file name
            file_writer.write('\n' + file_reader.name + '\n')

            #iterate through each line
            for line in file_reader:
                # read each line and use regex to match 'Sent:' header in message
                date_match = date_search(line)
                if date_match:
                    # remove Date key and write value to file
                    file_writer.write(line.split('Date:')[1].strip() + '\n')

                # read each line and use regex to match 'From:' header in message
                sender_match = sender_search(line)
                if sender_match:
                    # find email in the line and write to file
                    email_str = email_search(line)
                    file_writer.write(email_str + '\n')

                # read each line and use regex to match 'Subject: ' lines
                subject_match = subject_search(line)
                if subject_match:
                    # remove Subject key and write value to file
                    file_writer.write(line.split('Subject:')[1].strip() + '\n')

if __name__ == "__main__":
    main()
                
                
