def fibonacci(n):
  assert n >= 0 and int(n) == n, "The number must be positive and integer"
  if n in [0,1]:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
  fibonacci(8)
