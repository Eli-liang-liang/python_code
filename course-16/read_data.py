lines = []

a = open("data.txt")
# b = a.read()
# print(b)

# cd python_code/course-16

for i in a:
    lines.append(i.strip())

print(lines)

xs = [] # ['1','2','3','4']
ys = [] # ['50','60', '70', '80']
# lines = ['1,50', '2,60', '3,70', '4,80']
for line in lines:
    print(line)
    nums = line.split(",")
    print(nums)
    xs.append(nums[0])
    ys.append(nums[1])

print(xs)
print(ys)

# s = "1,50"
# print(s.split(","))

write_object = open("formated_data3.txt", "w")
write_object.write("x : " + " ".join(xs) + "\n")
write_object.write("y : " + " ".join(ys))
write_object.close()






