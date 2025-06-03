user_weight = float(input("请输入你的体重（单位：KG）"))
user_height = float(input("请输入你的身高（单位：M）"))
user_BMI = user_weight / (user_height **2)

print("您的BMI为:"+str(user_BMI))