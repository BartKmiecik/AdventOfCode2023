import sys

# sys.setrecursionlimit(3000)
def find_starting_index(list:[]):
    idx = ''
    for m in range(len(mapp)):
        try:
            idx = m, mapp[m].index('S')
        except:
            pass
        if idx:
            break
    return idx

def look_for_way(way:int, loc:[], last_counter:int):
    # 0 top 1 right 2 down 3 left
    if loc[0] < 0 or loc[0] > len(mapp) or loc[1] < 0 or loc[1] > len(mapp[0]):
        return -1
    last_counter = 1 + last_counter
    num = mapp[loc[0]][loc[1]]
    var1 = loc[0]
    var2 = loc[1]
    match way:
        case 0:
            var = mapp[loc[0]-1][loc[1]]
            # print(f'Num: {num}, var: {var}')
            if var == 'F':
                return 1, (loc[0]-1, loc[1]), last_counter
            if var == '|':
                return 0, (loc[0]-1, loc[1]), last_counter
            if var == '7':
                return 3, (loc[0]-1, loc[1]), last_counter
            else:
                return -1,(loc[0]-1, loc[1]), last_counter
        case 1:
            var = mapp[loc[0]][loc[1]+1]
            # print(f'Num: {num}, var: {var}')
            if var == '7':
                return 2, (loc[0], loc[1]+1), last_counter
            if var == '-':
                return 1, (loc[0], loc[1]+1), last_counter
            if var == 'J':
                return 0, (loc[0], loc[1]+1), last_counter
            else:
                return -1, (loc[0], loc[1]+1), last_counter
        case 2:
            var = mapp[loc[0] + 1][loc[1]]
            # print(f'Num: {num}, var: {var}')
            if var == 'L':
                return 1, (loc[0]+1, loc[1]), last_counter
            if var == '|':
                return 2, (loc[0]+1, loc[1]), last_counter
            if var == 'J':
                return 3, (loc[0]+1, loc[1]), last_counter
            else:
                return -1, (loc[0]+1, loc[1]), last_counter
        case 3:
            var = mapp[loc[0]][loc[1]-1]
            # print(f'Num: {num}, var: {var}')
            if var == 'L':
                return 0, (loc[0], loc[1] - 1), last_counter
            if var == '-':
                return 3, (loc[0], loc[1] - 1), last_counter
            if var == 'F':
                return 2, (loc[0], loc[1] - 1), last_counter
            else:
                return -1, (loc[0], loc[1] - 1), last_counter


data = open('../text/day10', 'r')

next = data.readline().strip()
mapp = []
while next:
    arr = []
    for n in next:
        arr.append(n)
    mapp.append(arr)
    next = data.readline().strip()

idx = find_starting_index(mapp)
# print(idx)

top = look_for_way(0, idx, 0)
right = look_for_way(1, idx, 0)
down = look_for_way(2, idx, 0)
left = look_for_way(3, idx, 0)

last_idx = 0
while top[0] != -1:
    top = look_for_way(top[0], top[1], top[2])
while right[0] != -1:
    right = look_for_way(right[0], right[1], right[2])
while down[0] != -1:
    down = look_for_way(down[0], down[1], down[2])
while left[0] != -1:
    left = look_for_way(left[0], left[1], left[2])


print(f'Top: {int(top[2]/2)}, right: {int(right[2]/2)}, down: {int(down[2]/2)}, left: {int(left[2]/2)}')


data.close()