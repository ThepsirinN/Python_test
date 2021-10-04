def findprime(start,end):
  a = end
  i = 2
  j = start
  k = 0
  l = []
  while j<=a:
      while True:
          if (i < j and j%i == 0):
              #print(j,"is not prime")
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
# answer is [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
