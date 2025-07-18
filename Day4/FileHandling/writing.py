
#write string to a file
with open('output.txt','w') as f:
    f.write('Hello,World')

#write multiple lines

lines=['Line 1\n','Line 2\n','Line 3\n']
with open('output.txt','w') as f:
    f.writelines(lines)


#Append to a file 

with open('output.txt','a') as f:
    f.write('\nAppended text')


    