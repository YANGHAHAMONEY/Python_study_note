print("平均值计算器，输入 q 结束运算")
total = 0  # 输入数字的总和
count = 0  # 输入数字的总个数

while True:
    user_input = input("请输入数字：")
    if user_input == "q":
        break  # 输入 q 时退出循环
    try:
        num = float(user_input)  # 尝试转换为数字
        total += num
        count += 1
    except ValueError:
        print("输入无效，请重新输入数字或输入 q 退出")

if count == 0:
    print("平均值为：0")
else:
    print(f"平均值为：{total / count}")