import sys
from DivAndConq import slowChange

if(len(sys.argv) < 2):
	print "Did not specify filename.\nExiting"
	exit(0)

filename = sys.argv[1]
filenameExt = filename[-4:]
print "***" + filenameExt + "***"

if(filenameExt not in ".txt"):
	print "Invalid filetype.\nExiting."
	exit(0)

money = open(filename, 'r')

#Redirect to a stupid name catted from in on command line
filename = filename[:-4]
sys.stdout = open("change" + filename + ".txt", "w+")

amount = [0]

while True:
	values = money.readline()
	if not values:
		break
	if values == [''] or values[0] == '#' or values[0] == '\n':
		continue
	amount = int(money.readline())
	
	values = values.rstrip('\n')
	values = values.rstrip('\r')
	values = values.rstrip(']')
	values = values.lstrip('[')
	values = values.split(',') 
	values = map(int, values)
	
	coinCount = [0] * len(values)
	coinCount = slowChange(amount, values)
	print coinCount
	print sum(coinCount)

money.close()