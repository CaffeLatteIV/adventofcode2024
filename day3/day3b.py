import re

# parte A
def mul(data):
  regex = r"(mul\([0-9]{1,3},[0-9]{1,3}\))"

  clean = [re.sub("mul\(|\)","",s).split(",") for s in re.findall(regex,data) ]
  res = 0
  for e in clean:
    mul =int(e[0])*int(e[1])
    res+=mul
  return res

# parte B (regex che prende tutti i caratteri tra don't() e do())
data = open("day3/input.txt").read()
reg = r"(don't\(\).+?do\(\))"
clean = re.sub(reg, "", data.replace("\n",""))
# regex se rimane un don't() alla fine senza un do() succesivo
clean = re.sub("don't\(\).+","",clean)
print(mul(clean))