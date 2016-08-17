# this is too inefficient
# def prime_finder(num):
	# count = 0
	# for n in range(2, 99999999999):
		# for x in range(2, n):
			# if n % x == 0:
				# print(n, 'equals', x, '*', n//x)
				# break
		# else:
			# count += 1
			# if count == num:
				# return ("The ", count, " prime is ", n)
			# print(n, 'is a prime number')
# print(prime_finder(2000))

# Example of sieve of eratostehenes
def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []
    for i in range(2, limitn):
        if i in not_prime:
            continue
        for f in range(i*2, limitn, i):
            not_prime.add(f)
        primes.append(i)
    return primes[1000000]
print (primes_sieve(20000000))