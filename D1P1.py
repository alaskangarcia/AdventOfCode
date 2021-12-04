file = open("D1P1.txt", "r")
last = 10000
most = 0
tmp = 0
for f in file:
    if int(f) > last:
        print("UP")
        tmp = tmp + 1
    last = int(f)
print(f"\n{tmp}")
