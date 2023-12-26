import re

pattern = f'([a-zA-Z]+)'
data = open('day8', 'r')

instructions = data.readline().strip()
next = data.readline()
next = data.readline()
nodes = {}
last_node = 'AAA'
while next:
    line = re.findall(pattern, next)
    nodes[line[0]] = (line[1], line[2])
    next = data.readline()

index = 1
has_result = False
while not has_result:
    result = ''
    # print(f'Starting with: {last_node}, instruction: {instructions[0]}')
    for x in instructions:
        # print(result)
        if x == 'L':
            result = nodes[last_node][0]
            if result == 'ZZZ':
                has_result = True
                break
            else:
                index += 1
                last_node = result
        else:
            result = nodes[last_node][1]
            if result == 'ZZZ':
                has_result = True
                break
            else:
                index += 1
                last_node = result
        # print(f'Instruction {x}, result: {result}')

print(index)
data.close()