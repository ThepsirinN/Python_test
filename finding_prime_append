def findprime(start,end):
  a = end
  i = 2
  j = start
  k = 0
  l = []
  while j<=a:
      while True:
          if (i < j and j%i == 0):
              //print(j,"is not prime")
              k += 1
              break
          if (i == j):
              break
          i += 1
      if(k == 0):
          l.append(j)
      k = 0
      i = 2
      j += 1
  return l
print(findprime(2,100))
