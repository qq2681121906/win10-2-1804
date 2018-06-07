class Zombie:
    def __init__(self,name,ph,color):
        self.name = name
        self.ph = ph
        self.color = color
    def __str__(self):
        s = self.name + '僵尸出现了,很闪闪着'+ self.color + '的光芒，充满' + self.ph + '血量，向你飞奔而来'
        return s
    def eat(self):
        print('%s僵尸正在努力啃咬目标------'%self.name)
    def run(self):
        print('%s僵尸奔跑过来了------'%self.name)

zb01 = Zombie('普通','100','灰色')
zb02 = Zombie('跳跳','80','红色')
print(zb01)
print(zb02)