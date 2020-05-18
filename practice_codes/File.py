f_read = open('a.txt', 'r')

f_copy = open('c.txt', 'w')

for i in f_read:
    f_copy.write(i)
