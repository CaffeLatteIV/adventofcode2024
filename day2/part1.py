f = open("day2/input.txt", "r")
lines = f.readlines() 
list1 = [(row.split(" ")) for row in lines]
safe =0
for row in list1:
  isSafe=True
  inc = False
  dec = False
  last = int(row[0])
  # controllo incremento o decremento
  for i in range(1,len(row)):
    n = int(row[i])
    if last < n:
      inc = True
    if last > n:
      dec = True
    if dec and inc:
      isSafe = False
      break
    # fine controllo
    if abs(n-last)>3 or abs(n-last)==0:
      isSafe = False
      break
    last = n
  if isSafe:
    safe+=1
print (safe)
