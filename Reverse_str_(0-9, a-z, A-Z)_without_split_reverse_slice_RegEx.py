def reverse_1(st1):
  a = st1
  b = ""
  temp = ""
  for i in a:
      if i in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": 
          temp = i + temp
      else:
          b = b + temp + i
          print(b)
          temp = ""
  return b
print(reverse_1("Hi, Mark!"))
# Answer is iH, kraM!
