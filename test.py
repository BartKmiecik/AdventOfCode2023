from collections import deque

tet = [1,2,3,4]
items = deque(tet)
print(f'First: {items}')
items.append(3)
print(f'Append: {items}')
items.rotate(0)
print(f'rotate: {items}')
# items.rotate(-1)
# print(f'Fourth: {items}')
item = items.popleft()
print(f'Popleft: {items}')
items.appendleft(4)
print(f'Append left: {items}')

while items:
    item = items.popleft()
    print(f'Popleft: {item}')

