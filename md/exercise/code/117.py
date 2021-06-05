from functools import reduce

# 自幂数
start = 0
end = 0
n = int(input('请选择自幂数的位数【1，2，3，4，5，6】:'))

while 0 < n < 7:
    start = pow(10, n - 1)
    end = pow(10, n) - 1
    print(n, '位数的自幂数有:')
    for k in range(start, end + 1):
        if reduce(lambda x, y: x+y, map(lambda z: int(z) ** n, str(k))) == k:
            print(k)
    n = int(input('\n 请选择自幂数的位数【1，2，3，4，5，6】:'))
else:
    print('输入位数不在范围内,程序结束。')
