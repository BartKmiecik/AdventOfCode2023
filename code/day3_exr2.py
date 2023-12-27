import copy
import re

data = open('../text/day3', 'r')
num_pattern = "([0-9]+)"
result = 0
nr_line = 0

last = data.readline().strip()
mid = data.readline().strip()
next = data.readline().strip()

last_nums = re.findall(num_pattern, last)
mid_nums = re.findall(num_pattern, mid)
next_nums = re.findall(num_pattern, next)


idx = 0
last_idx = 0
for i in range(len(last_nums)):
    last_idx = idx
    idx = last[idx:].index(last_nums[i]) + last_idx
    if idx + len(last_nums[i]) < len(last) - 2:
        if last[idx + len(last_nums[i])] == '*' and last[idx + len(last_nums[i]) + 1].isdigit():
            result += int(last_nums[i]) + int(last_nums[i+1])


while next:
    idx = 0
    last_idx = 0
    num_to_add = ''
    nr_line += 1
    for i in range(len(last_nums)):
        num_to_add = ''
        j = last_nums[i]
        last_idx = idx
        idx = last[idx:].index(last_nums[i]) + last_idx
        if idx + len(last_nums[i]) < len(last) -2:
            if last[idx+len(last_nums[i])] == '*' and last[idx+len(last_nums[i])+1].isdigit():
                result += int(last_nums[i]) + int(last_nums[i+1])

        below = mid[max(0, idx-1):min(len(mid), idx+len(last_nums[i])+1)]
        if below.find('*') != -1:
            star_idx = below.find('*') + idx
            # print(f'Star test {below.index("*")} and {below[below.index("*")]}')
            # print(f'Idx {idx} Star_idx {star_idx} and {mid[star_idx]}')
            left = copy.copy(star_idx)
            right = copy.copy(star_idx)
            while left >= 0:
                if mid[left].isdigit():
                    num_to_add = mid[left] + num_to_add
                    left -= 1
                else:
                    break
            if not mid[right].isdigit() and num_to_add != '':
                num_to_add = ''
                break
            # if num_to_add != '' and mid[right+1].isdigit():
            #     num_to_add = ''
            #     break
            else:
                while right < len(mid):
                    right += 1
                    if mid[right].isdigit():
                        num_to_add += mid[right]
                    else:
                        break
            left = copy.copy(star_idx) -1
            right = copy.copy(star_idx) -1
            # if int(last_nums[i]) == 965:
            #     print(num_to_add)
            if star_idx >= idx + len(last_nums[i]):
                if num_to_add != '' and last[right].isdigit():
                    num_to_add = ''
                    break
                else:
                    while right < len(last) + star_idx:
                        right += 1
                        if last[right].isdigit():
                            num_to_add += last[right]
                        else:
                            break
            right = copy.copy(star_idx) - 1
            if num_to_add != '' and next[left].isdigit():
                num_to_add = ''
                break
            else:
                if next[left].isdigit():
                    num_to_add = next[left] + num_to_add
                while left >= 0:
                    left -= 1
                    # print(f'{mid[:star_idx]}')
                    # print(f'{next[:left]}')
                    # print(f'{next[left]} a digit {next[left].isdigit()}')
                    if next[left].isdigit():
                        num_to_add = next[left] + num_to_add
                    else:
                        break
            while right < len(next):
                right += 1
                if next[right].isdigit():
                    num_to_add += next[right]
                else:
                    break

            if num_to_add:
                mult = int(num_to_add) * int(last_nums[i])
                result += mult
                print(f'Line{nr_line} Num1: {int(last_nums[i])} Num2: {int(num_to_add)} equal: {mult}')

    last = mid
    mid = next
    next = data.readline().strip()

    last_nums = re.findall(num_pattern, last)
    mid_nums = re.findall(num_pattern, mid)
    next_nums = re.findall(num_pattern, next)



# while next:
#     nr_line += 1
#     idx = 0
#     last_idx = 0
#     for num in mid_nums:
#         last_idx = idx
#         idx = mid[idx:].index(num) + last_idx
#         if idx > 0:
#             if mid[idx - 1] != '.':
#                 result += int(num)
#                 continue
#         if idx + len(num) < len(mid) - 1:
#             if mid[idx + len(num)] != '.':
#                 result += int(num)
#                 continue
#         below = next[max(0, idx - 1):min(len(next), idx + len(num) + 1)]
#         if len(below.replace(".", "").split())>0:
#             result += int(num)
#             continue
#         above = last[max(0, idx - 1):min(len(last), idx + len(num) + 1)]
#         if len(above.replace(".", "").split())>0:
#             result += int(num)
#
#     last = mid
#     mid = next
#     next = data.readline().strip()
#
#     last_nums = re.findall(num_pattern, last)
#     mid_nums = re.findall(num_pattern, mid)
#     next_nums = re.findall(num_pattern, next)
#
#
#
# for num in mid_nums:
#     idx = mid.index(num)
#     if idx > 0:
#         if mid[idx-1] != '.':
#             result += int(num)
#             continue
#     if idx + len(num) < len(mid) -1:
#         if mid[idx+len(num)] != '.':
#             result += int(num)
#             continue
#     above = last[max(0, idx - 1):min(len(last), idx + len(num) + 1)]
#     if len(above.replace(".", "").split())>0:
#         result += int(num)
#         continue

print(result)
data.close()