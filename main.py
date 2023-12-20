import re

data = open('day3', 'r')
num_pattern = "([0-9]+)"
result = 0

last = data.readline().strip()
mid = data.readline().strip()
next = data.readline().strip()

last_nums = re.findall(num_pattern, last)
mid_nums = re.findall(num_pattern, mid)
next_nums = re.findall(num_pattern, next)

nr_line = 1

for num in last_nums:
    idx = last.index(num)
    if idx > 0:
        if last[idx-1] != '.':
            result += int(num)
            continue
    if idx + len(num) < len(last) -1:
        if last[idx+len(num)] != '.':
            result += int(num)
            continue
    below = mid[max(0, idx-1):min(len(mid), idx+len(num)+1)]
    if len(below.replace(".", "").split())>0:
        result += int(num)

while next:
    nr_line += 1
    idx = 0
    last_idx = 0
    for num in mid_nums:
        last_idx = idx
        idx = mid[idx:].index(num) + last_idx
        if idx > 0:
            if mid[idx - 1] != '.':
                result += int(num)
                continue
        if idx + len(num) < len(mid) - 1:
            if mid[idx + len(num)] != '.':
                result += int(num)
                continue
        below = next[max(0, idx - 1):min(len(next), idx + len(num) + 1)]
        if len(below.replace(".", "").split())>0:
            result += int(num)
            continue
        above = last[max(0, idx - 1):min(len(last), idx + len(num) + 1)]
        if len(above.replace(".", "").split())>0:
            result += int(num)

    last = mid
    mid = next
    next = data.readline().strip()

    last_nums = re.findall(num_pattern, last)
    mid_nums = re.findall(num_pattern, mid)
    next_nums = re.findall(num_pattern, next)



for num in mid_nums:
    idx = mid.index(num)
    if idx > 0:
        if mid[idx-1] != '.':
            result += int(num)
            continue
    if idx + len(num) < len(mid) -1:
        if mid[idx+len(num)] != '.':
            result += int(num)
            continue
    above = last[max(0, idx - 1):min(len(last), idx + len(num) + 1)]
    if len(above.replace(".", "").split())>0:
        result += int(num)
        continue

print(result)
data.close()