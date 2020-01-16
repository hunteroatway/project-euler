def fib(n):
  if n==0 or n==1:
    return 0
  elif n==2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

sum = 0
for i in range(1, 35):
  res = fib(i)
  if res % 2 == 0:
    sum += res
print (sum)
