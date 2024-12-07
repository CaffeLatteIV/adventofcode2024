import math
def validateRule(rule, row):
    (pre, post) = rule
    for i in range(0, len(row)):
        page = row[i]
        if page == post:
            found = findPage(pre, row[i::])
            return not found
    return True


def findPage(n, pages):
    for page in pages:
        if n == page:
            return True
    return False

def fixErrors(rules,data):
  res =0
  for row in data:
    valid = False
    i=0
    while i< len(rules):
      (pre,post) = rules[i]
      valid = validateRule([pre,post], row)
      if not valid:
        postInd = row.index(post)
        preInd = row.index(pre)
        row[postInd] = pre 
        row[preInd] = post 
        i=0
      else:
        i+=1
    res +=int(row[math.floor((len(row) -1) /2)])
  return res


file = open("day5/input.txt").read().split("\n\n")
rules = [x.split("|") for x in file[0].split("\n")]
dataFull = [x.split(",") for x in file[1].split()]
data = []
for row in dataFull:
  for rule in rules:
    if not validateRule(rule,row):
      data += [row]
      break

print(fixErrors(rules,data))