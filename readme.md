# Email Header Parser

## Description

The outcome of this exercise is a single file output, containing various email headers from the supplied data.

## Part 1: Prework
Using Go, Python, or PHP, we'd like for you to prepare a code sample that will parse an archive of email files and create a single output file that contains the following:

* Date sent
* From address
* Subject line

During the on-site interview, we will change the project requirements and work through the changes required to your parser.

### Notes:
* Read from the already extracted directory
* Just output the date/from/subject values (e.g. ```'From: foo@bar.com'``` -> ```'foo@bar.com'```)
* Don’t worry about parsing or manipulating the date field, just dump what’s there
* Plain text output is fine

## How run it
Create a new python virtual environment (Requires Python 3, version 3.7.2 or higher)

```$ python3 -m venv return-path && cd return-path```

Delete the output.txt file (if it already exists)

```$ rm output.txt```

Run the parser script

```$ python3 headerparser.py```

**NOTE:** ```headerparser.py``` is the newer script that properly parses the email headers, using the Email std lib