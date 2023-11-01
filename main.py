def digital_root(n):
  if n < 0:
    return -1

  sums = sum([int(num) for num in str(n)])
  if len(str(sums)) >= 2:
      sums = digital_root(sums)
  return sums
