def largest_prime_factor(n):
    i = 2
    while i * i <= n: # this applies to composite (non-prime) numbers wherein there exists no prime factor of a number that is greater than its square root
        if n % i:
            i += 1
        else:
            n =  n//i
    return n
	
print(largest_prime_factor(600851475143))