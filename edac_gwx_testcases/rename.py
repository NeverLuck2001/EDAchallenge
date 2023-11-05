import os
import re

def rename1(path,origin):
#获取该目录下所有文件，存入列表中
    f = os.listdir(path)
    length0 = len(origin)
    for i in f:

        if i[-length0:] == origin:

            #设置旧文件名（就是路径+文件名）
            oldname = path + i

            #设置新文件名
            newname = path + i[:-length0] + 'txt'

            #用os模块中的rename方法对文件改名
            os.rename(oldname, newname)

            print(oldname, '======>', newname)

def rename2(path,origin):
#获取该目录下所有文件，存入列表中
    f = os.listdir(path)
    length0 = len(origin)
    for i in f:

        if i[-length0:] == origin:

            #设置旧文件名（就是路径+文件名）
            oldname = path + i

            #设置新文件名
            newname = path + i[:-length0] + 'ds'

            #用os模块中的rename方法对文件改名
            os.rename(oldname, newname)

            print(oldname, '======>', newname)

def rename3(path,origin):
#获取该目录下所有文件，存入列表中
    f = os.listdir(path)
    length0 = len(origin)
    for i in f:

        if i[-length0:] == origin:

            #设置旧文件名（就是路径+文件名）
            oldname = path + i

            #设置新文件名
            newname = path + i[:-length0] + 'summ'

            #用os模块中的rename方法对文件改名
            os.rename(oldname, newname)

            print(oldname, '======>', newname)


def rename4(path, origin):
    # 获取该目录下所有文件，存入列表中
    f = os.listdir(path)
    length0 = len(origin)
    for i in f:

        if i[-length0:] == origin:
            # 设置旧文件名（就是路径+文件名）
            oldname = path + i

            # 设置新文件名
            newname = path + i[:-length0] + 'lib'

            # 用os模块中的rename方法对文件改名
            os.rename(oldname, newname)

            print(oldname, '======>', newname)

def rename5(lvlib_path, key, key1):
    # 获取该目录下所有文件，存入列表中
    f = os.listdir(lvlib_path)

    for i in f:

            # 设置旧文件名（就是路径+文件名）
            oldname = lvlib_path + i

            # 设置新文件名
            newname = oldname.replace(key1,key)

            # 用os模块中的rename方法对文件改名
            os.rename(oldname, newname)


def rename6(lvlib_path, key, key1):
    # 获取该目录下所有文件，存入列表中
    f = os.listdir(lvlib_path)

    for i in f:
        # 设置旧文件名（就是路径+文件名）
        oldname = lvlib_path + i

        # 设置新文件名
        newname = oldname.replace(key, key1)

        # 用os模块中的rename方法对文件改名
        os.rename(oldname, newname)