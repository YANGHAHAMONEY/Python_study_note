def calculate_BMI(weight, height):
    BMI = weight / (height * height)
    if BMI < 18.5:
        print("偏瘦")
    elif BMI >= 18.5 and BMI < 25:
        print("正常")
    elif BMI >= 25 and BMI < 30:
        print("偏胖")
    elif BMI >= 30 and BMI < 35:
        print("肥胖")
    print(f"您的BMI评估结果为：{BMI:.2f}")
    return BMI


result = calculate_BMI(83, 1.8)
print(f"您的BMI评估结果为：{result:.2f}")
