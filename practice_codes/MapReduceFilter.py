from functools import reduce

lst = list(range(1, 5))
print('My lst :', lst)

odds = list(filter(lambda x: x % 2 != 0, lst))
print('odds : ', odds)

plus1 = list(map(lambda x: x + 1, odds))
#plus1 = list(map(lambda x, y: x + y, odds))
print(plus1)

addall = reduce(lambda x, y: x + y, plus1)
print(addall)
