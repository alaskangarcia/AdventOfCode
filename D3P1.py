file = open("D1P1.txt","r")
list, value = [], []
gamma, epsilon = "", ""
gvalue, evalue = 0, 0
for f in file:
    list.append(f)
for i in range(0,len(list[0])-1,1):
    count1, count0 = 0, 0
    for l in list:
        if l[i] == "1":
            count1 = count1+1
        elif l[i] == "0":
            count0 = count0+1
    if count1 > count0:
        gvalue = gvalue + pow(2,len(list[0])-2-i)
    else:
        evalue = evalue + pow(2,len(list[0])-2-i)
    
for i in range (0,len(list),1):
    pass
print(f"Gamma{gvalue} Epsilon {epsilon} {evalue} Total {gvalue*evalue}")
