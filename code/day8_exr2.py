import copy
import re

pattern = f'([0-9a-zA-Z]+)'
data = open('../text/day8', 'r')

instructions = data.readline().strip()
next = data.readline()
next = data.readline()
nodes = {}
starting_nodes = {}
while next:
    line = re.findall(pattern, next.strip())
    main = line[0]
    nodes[main] = (line[1], line[2])
    # print(main)
    if main[-1] == 'A':
        starting_nodes[main] = (line[0], False)
    next = data.readline()

# print(starting_nodes)

index = 0
has_result = False

while not has_result:
    result = ''
    for x in instructions:
        cp = copy.copy(starting_nodes)
        index += 1
        for key, value in cp.items():
            # print(value)
            if x == 'L':
                result = nodes[value[0]]
                matched = True if result[0][-1] == 'Z' else False
                starting_nodes[key] = (result[0], matched)
            else:
                result = nodes[value[0]]
                matched = True if result[1][-1] == 'Z' else False
                starting_nodes[key] = (result[1], matched)

        has_result = True
        for key, value in starting_nodes.items():
            if not value[1]:
                has_result = False
            else:
                print(f'Key: {key}, value: {index}')


print(index)
data.close()