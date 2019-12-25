1.M与N的数学运算：用户输入两个数 M 和 N，其中 N 是整数，计算M 和 N 的5种数学运算结果，并依次输出，结果间用空格分隔。

5种数学运算分别是：M 与 N 的和、M 与 N 的乘积、M 的 N 次幂、M除 N 的余数、M 和 N 中较大的值。

2.将输入的字符串垂直输出

3.计算矩形面积：用户输入矩形的长和宽，计算其面积并输出，结果四舍五入，保留2位小数。

4.计算2的n次方，n由用户输入

5.成绩转换：编写一个学生成绩转换程序，用户输入百分制的学生成绩，成绩大于或等于60的输出“pass”，否则输出“fail”，成绩不四舍五入。

6.完美立方：找到大于1的4个整数满足完美立方等式：a3=b3+c3+d3（例如123=63+83+103）。编写一个程序，对于任意给定的正整数N（N ≤100），寻找所有的四元组（a,b,c,d），满足a3=b3+c3+d3，其中1<a，b，c，d≤N。

7.货币转换：写一个程序进行货币间币值转换，其中：人民币和美元间汇率固定为：1美元 = 6.78人民币。

程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用RMB表示，美元USD表示，符号和数值之间没有空格。

8.月份缩写：如果有 months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."，编写一个程序，用户输入一个月份的数字，输出月份的缩写。

9.温度转换：编写程序将用户输入华氏度转换为摄氏度，或将输入的摄氏度转换为华氏度。

转换算法如下：（C表示摄氏度、F表示华氏度）

     C = ( F - 32 ) / 1.8
     F = C * 1.8 + 32
要求如下：

(1) 输入输出的摄氏度采用大写字母C开头，温度可以是整数或小数，如：C12.34指摄氏度12.34度；

(2) 输入输出的华氏度采用大写字母F开头，温度可以是整数或小数，如：F87.65指摄氏度87.65度；

(3) 不考虑异常输入的问题，输出保留小数点后两位

10.汇率兑换：按照1美元=6人民币的汇率来编写一个美元与人民币的双向兑换程序

11.恺撒密码：凯撒密码是古罗马凯撒大帝用来对军事情报进行加解密的算法，它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，即，字母表的对应关系如下：

原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

对于原文字符P，其密文字符C满足如下条件：C=(P+3) mod 26

上述是凯撒密码的加密方法，解密方法反之，即：P=(C-3) mod 26

假设用户可能使用的输入仅包含小写字母a~z和空格，请编写一个程序，对输入字符串进行凯撒密码加密，直接输出结果，其中空格不用进行加密处理。

12.个人所得税计算：个人所得税采用“超额累进税率”计算方法，简化公式如下：

   缴税 = （个人薪金扣险所得 – 个税免征额）* 税率

其中，个税免征额为3500元，税率根据应纳税额数量而不同，如下图所示：

注意：“应纳税额”为：个人薪金扣险所得 – 个税免征额

请编写一个程序根据用户输入计算个人所得税，用户输入是个人薪金扣险所得。

约定用户输入为以人民币元为单位的整数。

13.3位水仙花数计算：“3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身。例如：ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC。

请按照从小到大的顺序输出所有的3位水仙花数，请用一个“逗号+空格”分隔输出结果。

14.统计下列英文诗歌：

All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.

编程实现对纽卡斯伯爵的不朽名篇What Is Liquid的统计工作。这首诗（1）有多少个字符？（计入空格和换行符）（2）判断是否以All开头？（3）判断是否以That's all, folks!结尾？（4）第一次和最后一次出现单词the的位置（偏移量）。（5）the出现的总次数？（6）判断诗中出现的所有字符是否都是字母和数字？



