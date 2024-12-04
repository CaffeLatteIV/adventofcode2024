
list1 = [[int(i) for i in row.split()] for row in open('day2/input.txt')]
safe =0
for row in list1:
  isSafe=True
  inc = False
  dec = False
  last = None
  # controllo incremento o decremento
  for n in row:
    if last and last < n:
      inc = True
    if last and last > n:
      dec = True
    # fine controllo
    if last and abs(n-last)>3 or n==last or (dec and inc):
      isSafe = False
      break
    last = n
  if isSafe:
    safe+=1
print (safe)
