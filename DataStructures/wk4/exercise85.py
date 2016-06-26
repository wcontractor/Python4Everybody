fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

count = 0
emails = list()
fh = open(fname)

for line in fh:
	line = line.rstrip()
	if not line.startswith("From "):continue
	words = line.split()
	emails = words[1]
	count = count + 1
	print(emails)

print("There were", count, "lines in the file with From as the first word")