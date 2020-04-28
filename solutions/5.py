# calculates the prime factors of n 
def prime_fact(n):
  facts = []  
  p = 2
  while n >= p**2:
    if n % p == 0:
      facts.append(p)
      n = n / p
    else:
      p += 1
  facts.append(n)
  return facts

# all the prime factors from 1-20
p = []
for i in range(2, 21):
  p.append(prime_fact(i))

# all prime factors in dict 
count = []
for i in range(len(p)):
  count.append(dict((j, p[i].count(j)) for j in p[i]))

# loop in reverse order for highest powers
hp = []
for i in range(len(count)-1,-1,-1):
  if len(count[i].keys()) < 2:
    hp.append(count[i].keys())

# calculate final sum
sum = 1
for i in range(len(hp)):
  sum = sum * hp[i][0]
print(sum)
