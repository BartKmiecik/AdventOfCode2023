def calculate_diff(list_of_numbs:list):
    new_list = []
    should_repeat = False
    for n in range(len(list_of_numbs) - 1):
        var = int(list_of_numbs[n+1]) - int(list_of_numbs[n])
        new_list.append(var)
        if not should_repeat and var != 0:
            should_repeat = True
    return new_list, should_repeat

data = open('../text/day9', 'r')

next = data.readline().split()
result = 0

while next:
    # print(next)
    next.reverse()
    result += int(next[-1])
    diff, repeat = calculate_diff(next)
    while repeat:
        result += int(diff[-1])
        diff, repeat = calculate_diff(diff)
    next = data.readline().split()

print(result)
data.close()