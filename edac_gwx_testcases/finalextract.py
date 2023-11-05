import numpy as np
import re
import os

path = "./testcase03"
np_final_path = path + '/np_final_path'
if not os.path.exists(np_final_path):
    os.makedirs(np_final_path)
txt_path = path + "/MemeryInfomation.txt"

count = len(open(path+"/MemeryInfomation.txt",'r').readlines())

f = open(path + "/MemeryInfomation.txt", 'r')
line = f.readline()

name_dic = np.array([])[:, np.newaxis]
clk_dic = np.array([])[:, np.newaxis]
algo_dic = np.array([])[:, np.newaxis]
port_dic = np.array([])[:, np.newaxis]
op_dic = np.array([])[:, np.newaxis]

for i in range(count-1):
    line = f.readline()
    data = re.findall(r"\S+\.?\S*", line)
    print(data)
    name = np.expand_dims(np.array(data[0]), axis=0)[:, np.newaxis]
    x_pos = np.expand_dims(np.array(float(data[2])), axis=0)[:, np.newaxis]
    y_pos = np.expand_dims(np.array(float(data[3])), axis=0)[:, np.newaxis]
    clk = np.expand_dims(np.array(data[4]), axis=0)[:, np.newaxis]
    power = np.expand_dims(np.array(float(data[5])), axis=0)[:, np.newaxis]
    algo = np.expand_dims(np.array(data[6]), axis=0)[:, np.newaxis]
    port = np.expand_dims(np.array(data[7]), axis=0)[:, np.newaxis]
    op = np.expand_dims(np.array(data[8]), axis=0)[:, np.newaxis]
    wd = np.expand_dims(np.array(float(data[9])), axis=0)[:, np.newaxis]

    FLAG = False

    if name_dic.size != 0:
        for j in range(0, len(name_dic)):  # dic中是否存在这个算法
            if name == name_dic[j]:
                f1 = np.expand_dims(np.array(float(j)), axis=0)[:, np.newaxis]
                FLAG = True  # 已存在
                break
        if not FLAG:  # 不存在时
            name_dic = np.concatenate((name_dic, name), axis=0)
            f1 = len(name_dic) - 1
            f1 = np.expand_dims(np.array(float(f1)), axis=0)[:, np.newaxis]
            FLAG = False
        else:
            FLAG = False
    else:
        name_dic = np.concatenate((name_dic, name), axis=0)
        f1 = len(name_dic) - 1
        f1 = np.expand_dims(np.array(float(f1)), axis=0)[:, np.newaxis]

    if clk_dic.size != 0:
        for j in range(0, len(clk_dic)):  # dic中是否存在这个算法
            if clk == clk_dic[j]:
                f2 = np.expand_dims(np.array(float(j)), axis=0)[:, np.newaxis]
                FLAG = True  # 已存在
                break
        if not FLAG:  # 不存在时
            clk_dic = np.concatenate((clk_dic, clk), axis=0)
            f2 = len(clk_dic) - 1
            f2 = np.expand_dims(np.array(float(f2)), axis=0)[:, np.newaxis]
            FLAG = False
        else:
            FLAG = False
    else:
        clk_dic = np.concatenate((clk_dic, clk), axis=0)
        f2 = len(clk_dic) - 1
        f2 = np.expand_dims(np.array(float(f2)), axis=0)[:, np.newaxis]

    if algo_dic.size != 0:
        for j in range(0, len(algo_dic)):  # dic中是否存在这个算法
            if algo == algo_dic[j]:
                f3 = np.expand_dims(np.array(float(j)), axis=0)[:, np.newaxis]
                FLAG = True  # 已存在
                break
        if not FLAG:  # 不存在时
            algo_dic = np.concatenate((algo_dic, algo), axis=0)
            f3 = len(algo_dic) - 1
            f3 = np.expand_dims(np.array(float(f3)), axis=0)[:, np.newaxis]
            FLAG = False
        else:
            FLAG = False
    else:
        algo_dic = np.concatenate((algo_dic, algo), axis=0)
        f3 = len(algo_dic) - 1
        f3 = np.expand_dims(np.array(float(f3)), axis=0)[:, np.newaxis]

    if port_dic.size != 0:
        for j in range(0, len(port_dic)):  # dic中是否存在这个算法
            if port == port_dic[j]:
                f4 = np.expand_dims(np.array(float(j)), axis=0)[:, np.newaxis]
                FLAG = True  # 已存在
                break
        if not FLAG:  # 不存在时
            port_dic = np.concatenate((port_dic, port), axis=0)
            f4 = len(port_dic) - 1
            f4 = np.expand_dims(np.array(float(f4)), axis=0)[:, np.newaxis]
            FLAG = False
        else:
            FLAG = False
    else:
        port_dic = np.concatenate((port_dic, port), axis=0)
        f4 = len(port_dic) - 1
        f4 = np.expand_dims(np.array(float(f4)), axis=0)[:, np.newaxis]

    if op_dic.size != 0:
        for j in range(0, len(op_dic)):  # dic中是否存在这个算法
            if op == op_dic[j]:
                f5 = np.expand_dims(np.array(float(j)), axis=0)[:, np.newaxis]
                FLAG = True  # 已存在
                break
        if not FLAG:  # 不存在时
            op_dic = np.concatenate((op_dic, op), axis=0)
            f5 = len(op_dic) - 1
            f5 = np.expand_dims(np.array(float(f5)), axis=0)[:, np.newaxis]
            FLAG = False
        else:
            FLAG = False
    else:
        op_dic = np.concatenate((op_dic, op), axis=0)
        f5 = len(op_dic) - 1
        f5 = np.expand_dims(np.array(float(f5)), axis=0)[:, np.newaxis]

    arr = np.array([])[:, np.newaxis]
    arr = np.concatenate((arr,f1,x_pos,y_pos,f2,power,f3,f4,f5,wd), axis=0)
    np.save(np_final_path + '/'+ str(i), arr)