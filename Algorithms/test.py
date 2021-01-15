import time

print("az")
query_lst = [-60000,-6000,-600,-60,-6,0,6,60,600,6000,60000]

lst = []
dic = {}


for i in range(10000):
    lst.append(i)
    dic[i] = 1 

start = time.time()
for v in query_lst:
    if v in lst:
        continue
end1 = time.time()

for v in query_lst:
    if v in dic:
        continue

end2 = time.time()

print ("list search time : " ,(end1-start))
print ("dict search time : " ,(end2-end1))

lst2 = []
dic2 = {}

for i in range(100000):
    lst2.append(i)
    dic2[i] = 1 

start2 = time.time()
for i in query_lst:
    if i in lst2:
        continue
end2_1 = time.time()

for yue in query_lst:
    if yue in dic2:
        continue

end2_2 = time.time()

print ("list2 search time : " ,(end2_1-start2))
print ("dict2 search time : " ,(end2_2-end2_1))

lst3 = []
dic3 = {}

for i in range(1000000):
    lst3.append(i)
    dic3[i] = 1 

start3 = time.time()
for i in query_lst:
    if i in lst3:
        continue
end3_1 = time.time()

for yue in query_lst:
    if yue in dic3:
        continue

end3_2 = time.time()

print ("list3 search time : " ,(end3_1-start3))
print ("dict3 search time : " ,(end3_2-end3_1))