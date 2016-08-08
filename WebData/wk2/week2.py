import re
sum = 0
fhandler = open('regex_sum_283034.txt', 'r')
for line in fhandler:
	#line = line.rstrip()
	lst_of_numbers = re.search('[0-9]+', line)
	print(lst_of_numbers)
#for item in lst_of_numbers:
#	number = float(item)
#	print(number)
	#sum = numbers + sum
	#print(sum)