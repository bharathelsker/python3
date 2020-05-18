#Fibonacci series with a limit
limit = int(input('Enter the limit : '))

fib=[0,1]

while True:
    new = fib[-2] + fib[-1]

    if new >= limit:
        break
    else:
        fib.append(new)

print('fib :', fib)

print('END')