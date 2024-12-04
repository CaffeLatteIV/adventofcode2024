def orizz(data, xmas):
    count = 0
    for row in data:
      i=0
      for i in range(0, len(row)):
        isXmas = True
        j= i
        for x in xmas:
          if j >= len(row):
            isXmas = False
            break
          char = row[j]
          if char != x:
              isXmas =False
              break
          else:
            j+=1
        if isXmas:
          count+=1
    return count

def vertical(data,xmas):
  count =0
  for i in range(0, len(data)):
    for j in range(0, len(data[i])):
      height = i
      isXmas = True
      for x in xmas:
        if height>= len(data):
          isXmas = False
          break
        if data[height][j] !=x:
          isXmas = False
          break
        else:
          height+=1
      if isXmas: 
        count+=1
  return count

def diagonalSD(data, xmas):
  count =0
  for i in range(0, len(data)):
    for j in range(0, len(data[i])):
      height = i
      width = j
      c = data[height][width]
      isXmas = True
      for x in xmas:
        if height>= len(data) or width >= len(data[i]):
          isXmas = False
          break
        if data[height][width] !=x:
          isXmas = False
          break
        else:
          height+=1
          width +=1
      if isXmas: 
        count+=1
  return count

def diagonalDS(data, xmas):
  count =0
  for i in range(0, len(data)):
    for j in range(0, len(data[i])):
      height = i
      width = j
      isXmas = True
      for x in xmas:
        if height>= len(data) or width < 0:
          isXmas = False
          break
        if data[height][width] !=x:
          isXmas = False
          break
        else:
          height+=1
          width -=1
      if isXmas: 
        count+=1
  return count


xmas = ["X", "M", "A", "S"]
xmasInv = ["S", "A", "M", "X"]

data = [[*map(str, x.split()[0])] for x in open("day4/input.txt")]

res = orizz(data,xmas) + orizz(data,xmasInv) + vertical(data, xmas) + vertical(data, xmasInv) + diagonalSD(data, xmas) + diagonalSD(data, xmasInv) + diagonalDS(data,xmas)+ diagonalDS(data,xmasInv)
print(res)
