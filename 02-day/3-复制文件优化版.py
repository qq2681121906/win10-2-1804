#打开原来的文件
#把原来的文件内容读出来
#新建一个文件
#把内容写进去
#关闭

#1.获取用户要复制的文件名
file_name = input("请输入文件的名字要带后缀名")
#2.打开要复制的文件
old_file = open(file_name,'r')
#源文件---> 新文件[复件].py
#rfind返回的是下标
position = file_name.rfind(".")
new_file_name = file_name[0:position]+"副本"+file_name[position:]
#new_file name = '[复件]'+olf_file_name
#3.新建一个文件
#new_file = open('gebi_laowang.txt','w')
new_file = open(new_file_name,'w')
#4.从旧文件中读取数据,并且写入新的文件中
while True:
    content = old_file.read(1024)
    if len(content) == 0:
        break
    new_file.write(content)
#5.关闭2个文件
old_file.close()
new_file.close()