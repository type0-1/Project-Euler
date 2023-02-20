 #!/usr/bin/env python3
 
with open("names.txt") as f:
  names = f.readlines()
 
names = names[0].split(",")
names = sorted(names)
nums = []

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
for i in range(len(names)):
  name = names[i].strip('"')
  count = 0
    for c in name:
 		  if c in alpha:
        count += (alpha.index(c) + 1)
 	nums.append(count * (i + 1))
print(sum(nums))
