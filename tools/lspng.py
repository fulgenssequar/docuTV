import os
import sys
import re

allFiles = os.listdir(sys.argv[1])
allFiles.sort()
allFiles = [ sys.argv[1] + "/" +  a for a in allFiles ]
listStr = "picArray = " + str(allFiles);

f = open("piclist.js", "w+")
f.write( listStr )
f.close()



