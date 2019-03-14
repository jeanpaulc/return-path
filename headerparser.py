import glob
import re
import email
'''
The email package provides a standard parser that understands most 
email document structures, including MIME documents. You can pass 
the parser a bytes, string or file object, and the parser will return 
to you the root EmailMessage instance of the object structure.
'''

def file_set():
    # set all the files from the extracted archive into a list
    return glob.glob('./smallset/*.msg')

def email_search(string):
    email_regex = re.compile(r'<?([\w.-]+@[\w.-]+[^>\s])')
    return re.search(email_regex, string).group(1)

def main():
    # iterate through each file in the list
    for file_path in file_set():
        # open file for reading; create new file for output
        with open(file_path, 'r') as file_obj, open('output.txt', 'a') as output_file:
            # parse the email text and return a message object structure tree from the open file object
            email_msg = email.message_from_file(file_obj)

            # pull the values of the 'Date:', 'From:', and 'Subject:' headers
            date_header_value = email_msg['date']
            from_header_value = email_msg['from']
            subject_header_value = email_msg['subject']

            # use regex to parse for only the email string
            email_str = email_search(from_header_value)

            # write the results and include the file name
            output_file.write(file_obj.name + '\n')
            output_file.write(date_header_value + '\n')
            output_file.write(email_str + '\n')
            output_file.write(subject_header_value + '\n----\n')

if __name__ == "__main__":
    main()
