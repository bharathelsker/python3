def factorial(n):
    result = 1
    for i in range(1, n + 1, 1):
        result = result * i
    return result


if __name__ == '__main__':
    x = factorial(int(input('Enter the number : ')))
    print('Answer : ', x)

