import platform
import os

TEMP1 = "JDPVgBGvG5LRBmBGZHW6jZ9J.txt"
TEMP2 = "QXZ42nrJGapxKbeL7qZndzUR.txt"
OUT_EXT = ".tour"
MAX_TIMED_CITIES = 750
TIMEOUT = 295

##Cleanup
def cleanup():
	if((not os.path.isfile(TEMP1)) and (not os.path.isfile(TEMP2))):
		print "\nNo files to clean up.\n"
		exit(0)
		
	if(os.path.isfile(TEMP1)):
		os.remove(TEMP1)
	if(os.path.isfile(TEMP2)):
		os.remove(TEMP2)	