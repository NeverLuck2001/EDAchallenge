import os

print('文件父目录？')
path = input() + '\\'
print('原来后缀是？')
change0 = input()
print('后缀改为？')
change2 = input()
length0 = len(change0)
#length2 = len(change2)

#获取该目录下所有文件，存入列表中
f = os.listdir(path)

for i in f:

    if i[-length0:] == change0:

        #设置旧文件名（就是路径+文件名）
        oldname = path + i
    
        #设置新文件名
        newname = path + i[:-length0] + change2

        #用os模块中的rename方法对文件改名
        os.rename(oldname, newname)

        print(oldname, '======>', newname)
