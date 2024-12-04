
def diagonalSD(data, xmas,i,j, maxWidht, maxHeight):
  height = i
  width = j
  c = data[height][width]
  isXmas = True
  for x in xmas:
    if height>= maxHeight or width >= maxWidht:
      isXmas = False
      break
    if data[height][width] !=x:
      isXmas = False
      break
    else:
      height+=1
      width +=1
  return isXmas

def diagonalDS(data, xmas,i,j,maxHeight):
    height = i
    width = j
    isXmas = True
    for x in xmas:
      if height>= maxHeight or width < 0:
        isXmas = False
        break
      if data[height][width] !=x:
        isXmas = False
        break
      else:
        height+=1
        width -=1
    return isXmas

data = [[*map(str, x.split()[0])] for x in open("day4/input.txt")]
# Testing
# a = [
#   list("MMMSXXMASM"),
#   list("MSAMXMSMSA"),
#   list("AMXSXMAAMM"),
#   list("MSAMASMSMX"),
#   list("XMASAMXAMM"),
#   list("XXAMMXXAMA"),
#   list("SMSMSASXSS"),
#   list("SAXAMASAAA"),
#   list("MAMMMXMMMM"),
#   list("MXMXAXMASX")
#   ]
# data = a
mas = ["M", "A", "S"]
masInv = ["S", "A", "M",]
count=0
for i in range(0,len(data)):
  for j in range(0,len(data)):
    if data[i][j] in ["M","S"]:
      # controllo diagonale1 sia "mas" che "sam"
      isXmas = diagonalSD(data, mas, i, j, len(data), len(data[i])) or diagonalSD(data, masInv, i, j, len(data), len(data[i])) 
      # solo se ho trovato un possibile candidato (esiste già un mas in diagonale)
      if isXmas:
        # controllo diagonale2 sia "mas" che "sam"
        isXmas = diagonalDS(data, mas, i, j+2, len(data)) or diagonalDS(data, masInv, i, j+2, len(data))
      if isXmas:
        count+=1
      
print(count)