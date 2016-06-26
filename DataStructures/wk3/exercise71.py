fname = ("mbox-short.txt")
fhand = open(fname)
for line in fhand:
	caps = line.upper()
	print(caps)
	#print(line)