def sumofdigits(n):
  assert n >= 0 and int(n) == n, "The number must be positive and an integer"
  if n in [0,1]:
    return 0
  else:
    return int(n%10) + sumofdigits(int(n//10))
  
  sumofdigits(1234)
