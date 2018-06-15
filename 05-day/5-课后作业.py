class XUANZE(object):
    def __init__(self):
        print("1-查询班级  2-查询学生 3-查询成绩")
        xxxx=int(input("输入"))
        if xxxx ==1:
            CLASS.addstudent(self)
        elif xxxx==2:
            STUDENT.ADDCHENGJI(self)
        elif xxxx==3:
            CHENGJI.SETCHENGJI(self)
class CLASS(object):
    def __init__(self):
        self.student = []
        self.banzhuren= "老王"
        self.classnum="12345"
    def addstudent(self):
        xx=input("输入学生")
        CLASS.student.append(xx)
    def __str__(self):
        return "学生%s老师%s 搬好%s"%(self.student,self.banzhuren,self.classnum)

class STUDENT(object):
    def __init__(self):
        self.name ="王哥"
        self.age=18
        self.chengji={}
    def ADDCHENGJI(self):
        xx=input("输入学生")
        if xx in self.student:
            STUDENT.SETCHENGJI()
class CHENGJI(object):
    def __init__(self):
        self.yuwen= 100
        self.shuxue = 100
        self.yingyu = 100
    def GETCHENGJI(self):
        print("语文%s数学%s英语%s"%(self.yuwen,self.shuxue,self.yingyu))
    def SETCHENGJI(self):
        xx=int(iput("选择1-语文 2-数学 3-英语 4-查看"))
        xxx=init(input("输入成绩"))
        if xx==1:
            self.yuwen=xxx
        elif xx==2:
            self.shuxue=xxx
        elif xx==3:
            self.yingyu=xxx
        elif xx==4:
            print(self.__str__())
        else:
            print("输入错误")

    def __str__(self):
        msg = "语文%s数学%s英语%s"%(self.yuwen,self.shuxue,self.yingyu)
        return msg
        

zz=XUANZE()