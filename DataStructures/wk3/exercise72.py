# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
total_confidence = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(":")
    total_confidence = total_confidence + float(line[pos+1:])
    count = count + 1
    average = total_confidence/count
print("Average spam confidence:", average)
