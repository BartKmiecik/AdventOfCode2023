import re
# i = 1
# print(i)
# print(i<<1)
data = open('day4', 'r')
result = 0
pattern = f'([0-9]+)'
line = data.readline()
while line:
    split = line.split('|')
    winning_nums = re.findall(pattern, split[0])
    # print(winning_nums[1:])
    my_nums = re.findall(pattern, split[1])
    var = [n for n in my_nums if n in winning_nums[1:]]
    if var:
        result += 1<<(len(var)-1)
    line = data.readline()

data.close()

print(result)