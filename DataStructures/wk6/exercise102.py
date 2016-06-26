name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
	line = line.rstrip()
	if not line.startswith("From "): continue
	pos = line.find(":")
	hours = line[pos-2:pos]
	#print(hours)
	counts[hours] = counts.get(hours, 0) + 1
	
	
lst = list()
for key, val in counts.items():
	lst.append( (key, val) )
	
lst.sort()

for key, val in lst:
	print(val, key)
		