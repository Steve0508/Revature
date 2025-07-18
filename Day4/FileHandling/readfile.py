

#reading entire file  Day4\FileHandling\readfile.py

with open('index.txt','r') as f:
    content =f.read()  #returns entire file as string

#reading line by line
with open('index.txt','r') as f:
    for line in f:
        print(line.strip()) #remove newline characters

#read all line into list
with open('index.txt','r') as f:
    lines =f.readlines() # return list of lines


#read one line

with open('index.txt','r') as f:
    first_line=f.readline()
