#Author : Saurabh
# Reader.py
#
# Follow a file like tail -f.
import time
def read(thefile):
	thefile.seek(0,2)
	while True:
		line = thefile.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line

#if __name__ == '__main__':
logfile = open("Omne.log","r")
loglines = read(logfile)
for line in loglines:
	print (line)
