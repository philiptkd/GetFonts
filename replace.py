#replaces text in a file. 

import sys
import re

fileName = str(sys.argv[1])     #fully qualified
toReplace = str(sys.argv[2])    #regex pattern
replaceWith = str(sys.argv[3])

#read in the file
with open(fileName, 'r') as file:
    filedata = file.read()

#replace the target string
filedata = re.sub(toReplace, replaceWith, filedata)

#write the file out again
with open(fileName, 'w') as file:
    file.write(filedata)
