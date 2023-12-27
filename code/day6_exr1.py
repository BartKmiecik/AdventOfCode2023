import re

patern = f'([0-9]+)'
data = open('../text/day6', 'r')

times = re.findall(patern, data.readline())
records = re.findall(patern, data.readline())

result = 1
for time in range(len(times)):
    single_result = 0
    for i in range(int(times[time])):
        distance = i * (int(times[time])-i)
        if distance > int(records[time]):
            single_result += 1
    result *= single_result

print(result)
# print(times)
# print(records)

data.close()