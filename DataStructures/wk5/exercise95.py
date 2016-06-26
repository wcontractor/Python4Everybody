#Open the file mbox-short.txt
#create a list of only those lines starting with from
#create a dictionary of the emails and count
#print the maximum email and count
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith("From ") : continue
    words = line.split()
    emails = words[1]
    count[emails] = count.get(emails, 0 ) + 1
        
print(emails, count[emails])