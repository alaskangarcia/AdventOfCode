file = open("D1P1.txt")
f = []
hoz = 0
aim = 0
dep = 0
for f1 in file:
    f1 = f1.split(" ")
    f1[1] = int(f1[1])
    f.append(f1)

for l in f:
    if l[0] == "forward":
        hoz = hoz + l[1]
        dep = dep + aim*l[1]
    elif l[0] == "up":
        aim = aim - l[1]
    elif l[0] == "down":
        aim = aim + l[1]
    print(dep)

print(f"Hoz {hoz} Aim {aim} Dep {dep} Total {hoz*dep}")
