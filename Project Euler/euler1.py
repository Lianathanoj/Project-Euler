multipleList = []

for i in range(1,1000):
	if i%3 == 0 and i%5 == 0:
		multipleList.append(i)
	elif i%3 == 0:
		multipleList.append(i)
	elif i%5 == 0:
		multipleList.append(i)

print(sum(multipleList))
		