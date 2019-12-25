'''
M与N的数学运算：用户输入两个数 M 和 N，其中 N 是整数，计算M 和 N 的5种数学运算结果，并依次输出，结果间用空格分隔。

5种数学运算分别是：M 与 N 的和、M 与 N 的乘积、M 的 N 次幂、M除 N 的余数、M 和 N 中较大的值。
'''

def operation():

    try:
        m = int(input('请输入整数m的值:'))
    except ValueError:
        print('m不是整数，请重新输入')
    else:
        try:
            n = int(input('请输入整数n的值:'))
        except ValueError:
            print('n不是整数，请重新输入')
        else:

            sum = m + n 

            product = m * n

            power = m ** n

            remainder =  m % n

            maxer = max(m, n)

            print('m与n的和为：{0}     m与n的积为：{1}     m的n次幂为：{2}     m除以n的余数为：{3}     m和n中较大的值为：{4}'.format(sum, product, power, remainder, maxer) )
           
     
operation()




    