user_weight = float(input("请输入你的体重（单位：KG）"))
user_height = float(input("请输入你的身高（单位：M）"))
user_BMI = user_weight / (user_height **2)

print("您的BMI为:"+str(user_BMI))

if user_BMI <=18.5:
    print("此BMI值属于偏瘦范围")
elif 18.5 < user_BMI <= 25:
    print("此BMI值属于正常范围")
elif 25 <user_BMI <=30:
    print("此BMI值属于偏胖范围")
else:
    print("此BMI值属于肥胖范围")