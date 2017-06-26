import os
import sys
import re
i = 1;
files = os.listdir(".")
files.sort(key=lambda x: os.path.getctime(x))
for filename in files:
	newname = str(i).zfill(2) + "-" + re.sub(sys.argv[1], "", filename, 1)
	os.rename(filename, newname)
	i = i + 1
	
	
		