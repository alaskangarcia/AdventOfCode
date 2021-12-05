file = open("D1P1.txt","r")
list1, lista, listb, list2 = [], [], [], []
for f in file:
    list1.append(f)
list2 = list1
bigdumb = len(list1[0])-1
tmp = 0
for i in range(0, bigdumb, 1):
    count1, count0 = 0, 0
    for l in list1:
        if l[i] == "1":
            count1 = count1 + 1
        elif l[i] == "0":
            count0 = count0 + 1
    if count1 >= count0:
        for l in list1:
            if l[i] == "1":
                tmp = tmp +1
                lista.append(l)
    elif count1 < count0:
        for l in list1:
            if l[i] == "0":
                lista.append(l)
    list1 = lista
    lista = []
    if len(list1) == 1:
        break
for i in range(0, bigdumb, 1):
    count1, count0 = 0, 0
    for l in list2:
        if l[i] == "1":
            count1 = count1 + 1
        elif l[i] == "0":
            count0 = count0 + 1
    if count1 < count0:
        for l in list2:
            if l[i] == "1":
                listb.append(l)
    elif count1 >= count0:
        for l in list2:
            if l[i] == "0":
                listb.append(l)
    list2 = listb
    listb = []
    if len(list2) == 1:
        break
    
def binaryconv(number):
    tmp = 0
    print(number)
    for i in range(0, len(number),1):
        if number[i] == "1":
            tmp = tmp + pow(2, len(number)-2-i)
    return tmp
print(f"Oxygen generator {list1} CO2 Scrubber {list2} Total {binaryconv(list1[0]) *binaryconv(list2[0])}")
