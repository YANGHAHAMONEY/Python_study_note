slang_dict = {
    "觉醒年代": "新时代觉醒的广大青年学子",
    "双减": "为什么22届大学生没有呢？",
    "破防": "心理防线被突破，形容极度感动或震惊",
    "躺平": "消极应对内卷，选择低欲望生活方式",
    "社死": "社会性死亡，指公开场合出丑",
    "绝绝子": "形容事物好到极致（含夸张色彩）",
    "蚌埠住了": "谐音'绷不住了'，指情绪失控",
    "芭比Q": "谐音'BBQ'，引申为'完蛋了'",
    "栓Q": "谐音'thank you'，反讽式表达无语"
}

slang_dict["YYDS"] = "永远的神！"

print(slang_dict)

query = input("请输入您要查找的词条：")
if query in slang_dict:
    print("您查询的词条"+query+"含义如下")
    print(slang_dict[query])
else:
    print("您查询的词条暂未收录")
    print("当前已收录词条数："+str(len(slang_dict))+"条")
