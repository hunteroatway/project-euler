# calculate prime factors of n
def prime_fact(n):
  facts = []  
  facts.append(1)  
  p = 2
  while n >= p**2:
    if n % p == 0:
      facts.append(p)
      n = n / p
    else:
      p += 1
  facts.append(n)
  return facts

# determine whether n is prime
def is_prime(n):
  f = prime_fact(n)
  if f[0] != 1 or f[1] != n:
      return False
  return True

# loop until 10001 prime is found
c = 0
n = 2
while True:
  n += 1
  if is_prime(n):
    c += 1
  if c == 10000:
    break
print(n)
