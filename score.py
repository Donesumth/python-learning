total = 0
pass_count = 0
for i in range(5):
    score = float(input("输入第"+str(i+1)+"次成绩；"))
    total += score
    if score >=60:
        pass_count += 1
print("平均分：",total/5)
print("及格次数：",pass_count)