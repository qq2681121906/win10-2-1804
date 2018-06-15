print('*'*30)
print('欢迎使用【名片管理系统】V1.0')
print('1.新建名片')
print('2.显示全部')
print('3.查询名片')
print('4.删除名片')
print('5.退出系统')
print('*'*30)
list_Ming=[]
class MP(object):
    def fangfa(self):
        while True:
            shu=int(input('请输入你要操作的数字：'))
            if shu==1:
                self.new()
            elif shu==2:
                self.sall()
            elif shu==3:
                self.sOne()
            elif shu==4:
                self.delM()
            else:
                print('成功退出系统')
                break
    def new(self):
        print('*'*30)
        print('开始新建名片')
        name=input('请输入姓名：')
        com=input('请输入公司:')
        zhiwu=input('请输入职务：')
        phone=input('请输入电话号码：')
        email=input('请输入电子邮箱：')
        dic={'name':name,
             'com':com,
             'zhiwu':zhiwu,
             'phone':phone,
             'email':email}
        list_Ming.append(dic)
        print(list_Ming)
        print('成功添加%s的名片'%dic['name'])
    def sall(self):
        print('*'*30)
        print('功能：查询全部名片')
        if len(list_Ming) == 0:
            print("提示：没有任何名片记录")
        for dic in list_Ming:
            print(dic)
    def sOne(self):
        print('*'*30)
        print('查询一个名片')
        s=input('请输入要查询的名字？')
        for i in list_Ming:
            if s== i['name']:
                print('*'*33)
                print('姓名：%s'% i['name'])
                print('公司：%s'% i['com'])
                print('职务：%s'% i['zhiwu'])
                print('电话：%s'% i['phone'])
                print('电子邮箱：%s'% i['email'])
    def delM(self):
        print('*'*30)
        name = input("请输入你要删除的名字")
        flag = 0 #假设不在
        for temp in list_Ming:
            if name == temp["name"]:
                flag = 1#找到了
                i=input('确定要删除名片吗？确定请输y or n')
                if i=='y':
                    list_Ming.remove(temp)#删除
                    print("删除成功")
                break
        if flag == 0:
            print("没有此人")  

mm=MP()
mm.fangfa()