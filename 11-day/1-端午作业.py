class GongChang(object):
    def __init__(self,carname):
        self.carname=carname
class Shop(object):
    def __init__(self,sname,shou):
        self.sname=sname
        self.shou=shou

class Car(GongChang,Shop):
    def __init__(self,a,b,c):
        GongChang.__init__(self,a)
        Shop.__init__(self,b,c)

    def run(self):
        return "汽车跑的快"
    def storp(self):
        return "汽车停下了"
aa=input("你要制造的汽车是：")
bb=input("你要在哪家店购买汽车")
cc=input("汽车的售价是")
aa=Car(aa,bb,cc)
print("你制造的汽车是 %s 在 %s 店销售 售价 %s" %(aa.carname,aa.sname,aa.shou))
print(" %s %s"%(aa.carname,aa.run()))
print(" %s %s"%(aa.carname,aa.storp()))