a = []
for i in range(100, 1000):
  for j in range(100, 1000):
    p = i * j
    t = str(p)[::-1]
    if (str(p) == t):
      a.append(p)
a.sort()
print(a[len(a)-1])
