import math
def validateRule(rule, pages):
  (pre, post) = rule
  for i in range(0,len(pages)):
    page = pages[i]
    if page == post:
      found = findPage(pre,pages[i::])
      return not found
  return True
def findPage(n,pages):
  for page in pages:
    if n == page:
      return True
  return False  
file = open("day5/input.txt").read().split("\n\n")
rules = [x.split("|") for x in file[0].split("\n")]
pages = [x.split(",") for x in file[1].split()]
valid =0
i =0
notValid =[]
for row in pages:
  isValid = False
  for rule in rules:
    isValid = validateRule(rule,row)
    if isValid == False:
      break
  if isValid:
    valid+=int(row[math.floor((len(row) -1) /2)])
  if not valid:
    notValid += [row]
  i+=1

# print(valid)
print(notValid)