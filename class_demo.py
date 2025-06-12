class StudentScore:
    def __init__(self,name,student_id,chinese_score,math_score,english_score):
        self.name=name
        self.student_id=student_id
        self.chinese_score=chinese_score
        self.math_score=math_score
        self.english_score=english_score
    def speak(self):
        print(f"语文成绩为：{self.chinese_score},数学成绩为{self.math_score},英语成绩为：{self.english_score}")

student_1 = StudentScore("wisdom",1234,100,100,100)

student_1.speak()