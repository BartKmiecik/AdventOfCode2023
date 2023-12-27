import re
import numpy as np
from day5_supportingClass import SeedToPlant


patern = f'([0-9]+)'
groups_names = ['seeds', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
groups = {}
counter = 0
data = open('../text/day5', 'r')
next = data.readline()
groups[groups_names[counter]] = re.findall(patern, next)
seeds = []
seeds_ranges = int(len(groups['seeds'])/2)
for seed in range(int(groups['seeds'][0]), int(groups['seeds'][0]) + int(groups['seeds'][1])):
    print(seed)

        # seeds.append(SeedToPlant(int(seed)))
# for seed in groups['seeds']:
#     seeds.append(SeedToPlant(int(seed)))

# print(len(seeds))

# next = data.readline()
# while next:
#     numbs = re.findall(patern, next)
#     if not numbs and groups_names[counter] in groups:
#         counter += 1
#     elif groups_names[counter] in groups:
#         groups[groups_names[counter]] += numbs
#     else:
#         groups[groups_names[counter]] = numbs
#     next = data.readline()
#
# for i in range(1,len(groups_names)):
#     if i == 0:
#         continue
#     triplets = int((len(groups[groups_names[i]])+1)/3)
#     for j in range(triplets):
#         dest = int(groups[groups_names[i]][j*3])
#         start = int(groups[groups_names[i]][j * 3 + 1])
#         end = int(groups[groups_names[i]][j * 3 + 2])
#         for seed in seeds:
#             value = seed.return_parameter(groups_names[i])
#             if value in range(start, start + end):
#                 seed.change_parameter(groups_names[i], value - (start - dest), True)
#
#
# max = (1000000000, 1000000000)
# for seed in seeds:
#     # print(seed)
#     if seed.location < max[1]:
#         max = (seed.seeds, seed.location)
#
# print(max)
# data.close()