'''
M与N的数学运算：用户输入两个数 M 和 N，其中 N 是整数，计算M 和 N 的5种数学运算结果，并依次输出，结果间用空格分隔。

5种数学运算分别是：M 与 N 的和、M 与 N 的乘积、M 的 N 次幂、M除 N 的余数、M 和 N 中较大的值。
'''


def operation():
    sum = m + n
    product = m * n
    power = m ** n
    remainder = m % n
    maxer = max(m, n)
    print('您输入的m为：{5}、 n为：{6}        '
          'm与n的和为：{0}     m与n的积为：{1}     '
          'm的n次幂为：{2}     m除以n的余数为：{3}     '
          'm和n中较大的值为：{4}'.format(sum, product, power, remainder, maxer, m, n))


if __name__ == "__main__":
    num1 = input("请输入整数m：")
    while True:
        try:
            m = int(num1)
            break
        except ValueError:
            num1 = input("m不是整数，请重新输入：")
    num2 = input("请输入整数n：")

    while True:
        try:
            n = int(num2)
            break
        except ValueError:
            num2 = input(("n不是整数，请重新输入："))

    operation()
