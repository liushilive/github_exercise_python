def reduceNum(n):
    print(f'{n} = ', end='')
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字 !')
        exit(0)
    elif n == 1:
        print(f'{n}')
    else:
        while n not in [1]:  # 循环保证递归
            for index in range(2, n + 1):
                if n % index == 0:
                    n //= index  # n 等于 n/index
                    if n == 1:
                        print(index)
                    else:  # index 一定是素数
                        print(f'{index} *', end=' ')
                    break


reduceNum(90)
reduceNum(100)
