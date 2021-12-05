file = open("D1P1.txt")
list, boards, balls, cball = [], [], [], 0
fboard, lball = [], 0
for f in file:
    list.append(f[:-1])
balls = list[0].split(",")
list = list[2:]
fill, tmp= [], []
def testBoard(board):
    bingos, tcount = 0, 0
    #Check Row
    for i in range(0, len(board), 1):
        for c in range(0, len(board[i]), 1):
            if board[i][c] == "#":
                tcount = tcount + 1
        if tcount == 5:
            bingos = bingos + 1
        tcount = 0
    #Check Column
    tcount = 0
    for i in range(0, len(board), 1):
        for c in range(0, len(board[i])):
            if board[c][i] == "#":
                tcount = tcount + 1
        if tcount == 5:
            bingos = bingos + 1
        tcount = 0
    #Check Diags
    #Check Forward
    tcount = 0
    for i in range(0, len(board), 1):
        if board[i][i] == "#":
            tcount = tcount + 1
    if tcount == 5:
        bingos = bingos + 1
    tcount = 0
    #Check Back
    tcount = 0
    for i in range(0, len(board), 1):
        if board[i][len(board)-1-i] == "#":
            tcount = tcount + 1
    if tcount == 5:
        bingos = bingos + 1
        tcount = 0
    tcount = 0
    return bingos


for i in range(0, len(list)-1, 1):
    if list[i] == '':
        for tm in tmp:
            tt = []
            for c in range(0, len(tm)-1, 1):
                if tm[c] == "":
                    tt.append(c)
            for u in range(len(tt)-1,-1,-1):
                tm.pop(tt[u])
            fill.append(tm)
        boards.append(fill)
        tmp = []
        fill = []
    else:
        tmp.append(list[i].split(" "))
            
count = 0
fount = False
for ball in range(0, len(balls), 1):
    for board in range(0, len(boards), 1):
        for line in range(0, len(boards[board]), 1):
            for item in range(0, len(boards[board][line]), 1):
                if boards[board][line][item] == balls[ball]:
                    count = count + 1
                    boards[board][line][item] = '#'
        if testBoard(boards[board]) == 1:
            fboard = boards[board]
            lball = balls[ball]
            fount = True
            break
    if fount:
        break
total = 0
for fb in fboard:
    for f in fb:
        if f != "#":
            total = total + int(f)
            
print(f"Sum {total} Ball {lball} Total {total * int(lball)}")
