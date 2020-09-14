j = "aA"
s = "aAAbbbb"
count = 0
for a in s:
    if a in j:
        print(a, "是一个宝石")
        count += 1
    else:
        continue

print("宝石一共有：", count, "个")