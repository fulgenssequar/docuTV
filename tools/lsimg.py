import os
import sys
import re

allFiles = os.listdir(sys.argv[1])
allFiles.sort()

allFiles = [ "project/" + sys.argv[1] + "/" +  a for a in allFiles ]
allFiles = ["project/img_cover.png"] + allFiles
listStr = "var picArray = " + str(allFiles);

f = open("project/src/piclist.js", "w+")
f.write( listStr )
f.close()



