import re
data = open("day3/input.txt").read()

regex = r"(mul\([0-9]{1,3},[0-9]{1,3}\))"

clean = [re.sub("mul\(|\)","",s).split(",") for s in re.findall(regex,data) ]
res = 0
for e in clean:
  mul =int(e[0])*int(e[1])
  res+=mul

print(res)