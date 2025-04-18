print("hello world!")

import keyword
keyword.kwlist

# !/usr/bin/python3

str = '123456789'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

input("\n\n按下 enter 键后退出。")

import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

print("邓梦诗：我要学自动化测试！")

name = "邓梦诗"  # 替换成你的名字
print(name + "说：我要学自动化测试！")

a=float(input("输入第一个数："))
b=float(input("输入第二个数："))
print("和是：",a+b)
print("积是：",a*b)

# !/usr/bin/python3

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")

score=int(input("输入成绩："))
if score >= 60:
    print("及格")
else:
    print("不及格")

num1 = float(input("输入第一个数："))
op = input("输入运算符（+ 或 * 或 -）：")
num2 = float(input("输入第二个数："))
if op == "+":
    print("结果：", num1 + num2)
elif op == "*":
    print("结果：", num1 * num2)
elif op == "-":
    print("结果：", num1 - num2)
else:
    print("无效运算符")

# Python 练习实例1
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i != j) and (j != k):
                print(i,j,k)
# Python 练习实例2
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print ("zhesha",(i-arr[idx])*rat[idx])
        i=arr[idx]
print ("总提成：",r)
# Python 练习实例3
def find_integer():
    for i in range(2,85):
        if 168 % i == 0:
            j = 168//i
            if i > j and (i + j)%2 ==0 and (i-j)%2 == 0:
                m = (i + j) // 2
                n = (i - j) // 2
                x = n * n - 100
                print(f"x: {x}, m: {m}, n: {n}")

# 调用求解函数
find_integer()

n = int(input("输入一个正整数："))
for i in range(1,n+1):
    print(i)

#1加到100
sum = 0
for i in range(1,101):
    sum += i
print("总和：",sum)
#统计1到100之间能被7整除的数的个数
count = 0
for i in range(1,101):
    if i % 7 == 0:
        count += 1
print("个数：",count)

count = 0
for i in range(1,101):
    if i % 3 == 0:
        print(i)
#第3题：输出1到100之间的所有奇数
for i in range(1,101):
    if i % 2 == 1:
        print(i)

for i in range(1,101):
    if i % 2 == 0:
        print(i,end=" ")

for i in range(1,101,2):
    print(i,end=" ")

for i in range(2,101,2):
    print(i)