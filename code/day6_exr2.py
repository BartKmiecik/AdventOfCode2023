import re

patern = f'([0-9]+)'
data = open('../text/day6', 'r')

times = re.findall(patern, data.readline())
records = re.findall(patern, data.readline())
total_time = ''
for t in times:
    total_time += t
total_record = ''
for r in records:
    total_record += r


single_result = 0
for i in range(int(total_time)):
    distance = i * (int(total_time) - i)
    if distance > int(total_record):
        single_result += 1


print(single_result)
# print(total_time)
# print(total_record)

data.close()