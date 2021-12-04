file = open("D1P1.txt")
list = []
last = 1000
incr = 0
for f in file:
    list.append(int(f))

for i in range(0,len(list)-2,1):
    if list[i]+list[i+1]+list[i+2] > last:
        incr = incr + 1
    last = list[i]+list[i+1]+list[i+2]
    
print(incr)
