class CuteCat:
    def __init__(self,cat_name,cat_age,cat_color):
        self.cat_name = cat_name
        self.cat_age = cat_age
        self.cat_color = cat_color

    def speak(self):
        print("喵"*self.cat_age)


cat_1 = CuteCat("hm",8,"blue")

cat_1.speak()

print(f"猫咪的名字为：{cat_1.cat_name},猫猫的年龄为： {cat_1.cat_age},猫猫的颜色为：{cat_1.cat_color}")