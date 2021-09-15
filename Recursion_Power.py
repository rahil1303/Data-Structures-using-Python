def power(base,exp):
  if x == 0:
    return 1
  if x == 1:
    return base
  else:
    return base * power(base,exp-1)
 
print(power(2,4))
