f = open("input.txt", "r")
lines = f.readlines()
list1 = [row.split(" ")[0] for row in lines]
list2 = [row.split(" ")[-1] for row in lines]
list1.sort()
list2.sort()
res = 0
for i in range(0, len(list1)):
    a = int(list1[i])
    b = int(list2[i])
    res += abs(a-b)

print(res)
# part two
f = open("day2/input.txt", "r")
lines = f.readlines()
list1 = [int(row.split(" ")[0]) for row in lines]
list2 = [int(row.split(" ")[-1]) for row in lines]
list1.sort()
list2.sort()
res = 0
count =0
n = 0
i = 0
# while (n< len(list1)):
#   if list1[n] == list2[i]:
#     count +=1
#   i= i+1 if i < len(list2)-1 else len(list2)-1
#   if list1[n] < list2[i] or i == len(list2)-1:
#     res = res + (count * int(list1[n]))
#     n+=1
#     i=n
for a in list1:
  for b in list2:
    if (a == b):
      count+=1
    if (a < b):
      break
  res+= a*count
  count=0

print(res)
