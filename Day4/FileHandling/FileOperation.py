import os
#check the file exists


if os.path.exists('index.txt'):
    print('file exists')

#Get file size

size =os.path.getsize('index.txt')
print(size)


import time
mod_time=os.path.getmtime('index.txt')  #in which format
readable_time=time.ctime(mod_time) #output
print(readable_time)