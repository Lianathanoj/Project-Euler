# def fib(n):
	# if n == 1:
		# return n
	# elif n == 0:
		# return 1
	# return fib(n-1) + fib(n-2)

# print (fib(6))



# found out that 32nd term is the maximum term that does not exceed 4000000

dictList = {0:0, 1:1, 2:2}

sumList = []

def fib(n):
	if n not in dictList:
		dictList[n] = fib(n-1) + fib(n-2)
	if dictList[n]>4000000:
		print(n) # find out the first value which is greater than 4 million, value-1 is 32
	return dictList[n]

print(fib(32))
	
for i in dictList.values():
	if i%2 == 0:
		sumList.append(i)
		
print(sum(sumList))
	