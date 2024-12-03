def validator(row):
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
  return isSafe

def day2b(data): 
  # elimino un elemento e controllo che la 
  # lista risultante sia "safe", 
  # ripeto finchè non arrivo alla fine o trovo una sottostringa safe
  res =0
  for row in data:
    safe = validator(row)
    if not safe:
      for i in range(0, len(row)):
        tmp = row[i]
        del row[i]
        safe = validator(row)
        row = row[0:i] + [tmp] + row[i::]
        if safe:
          break
    if safe:
      res+=1

  print(res)

# split di default splitta ogni whitespace e \n o \ strano e cancella ogni elemento vuoto
data = [[*map(int, l.split())] for l in open('day2/input.txt')]
day2b(data)