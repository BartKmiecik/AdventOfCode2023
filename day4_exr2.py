import re

data = open('day4', 'r')
result = 0
pattern = f'([0-9]+)'
line = data.readline()
counter = 2
table_of_scratches = {1:1}
table_of_matches = {}
while line:
    split = line.split('|')
    winning_nums = re.findall(pattern, split[0])
    my_nums = re.findall(pattern, split[1])
    wins = [n for n in my_nums if n in winning_nums[1:]]
    sup_counter = 0
    if counter in table_of_scratches:
        table_of_scratches[counter] += 1
    else:
        table_of_scratches[counter] = 1
    table_of_matches[counter-1] = len(wins)
    for win in wins:
        key = counter + sup_counter
        if key in table_of_scratches:
            table_of_scratches[key] += table_of_scratches[counter-1]
        else:
            table_of_scratches[key] = table_of_scratches[counter-1]
        sup_counter += 1

    counter += 1
    line = data.readline()

for _, value in table_of_scratches.items():
    result += value

data.close()

print(result-1)
