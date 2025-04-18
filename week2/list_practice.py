fruits = ["apple", "banana", "orange", "grape", "mango"]
fruits.remove("banana")
# fruits[2] = "pear"
# fruits.append("watermelon")
print(len(fruits))
print("apple" in fruits)
# print(fruits[1])  # 输出：banana
# print(fruits[-1])  # 输出：mango

numbers = []
for i in range(5):
    num = int(input("请输入第{}个数字: ".format(i+1)))
    numbers.append(num)
print("最大值:", max(numbers))
print("最小值:", min(numbers))

