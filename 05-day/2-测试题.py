class Student():
    def __init__(self,name,sex,age,cj):
        self.name = name
        self.sex = sex
        self.age = age
        self.cj = {}

    def addcj(self,k,v):
        self.cj.setkey[k] ={v}

    def hanshu(a):
        for i in range(1,6):
            k = input('科目')
            v = input('成绩')
            a.hanshu(k,v)
    def __str__(self):
        return'姓名:'+self.name +'性别:'+self,sex +'年龄:'+str(self.age) +'成绩:'+str(self.cj)
    f = open('1.txt','w')
    f.write('a')
    f.close()

xiaoming = Student('小明','男',20,{60,60,60,60,60})
xiaoming.hanshu()