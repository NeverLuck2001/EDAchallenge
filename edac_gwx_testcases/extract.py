import numpy as np
import os
import re
from rename import rename1, rename2, rename3, rename4, rename5

path0 = './testcase0'
algo_dic = np.array([])[:, np.newaxis]
LP_dic = np.array([])[:, np.newaxis]

for q in range(2,9):  # 提取ds
    if os.path.exists(path0 + str(q) + '/'):
        path = path0 + str(q) + '/'
        np_path = path + 'ds_np/'
        ds_path = path + 'ds/'
        if not os.path.exists(np_path):
            os.makedirs(np_path)
        # np.load("D:/PythonProj/edac_gwx_testcases/testcase03/ds_np/spsram_256x12m2s_tt1v25c.txt.npy")
        list1 = os.listdir(ds_path)
        length1 = len(list1)

        if list1[0][-2:] == 'ds':
            rename1(ds_path, 'ds')
            list2 = os.listdir(ds_path)
            for i in range(length1):
                print(list2[i])
                f = open(ds_path + list2[i], 'r')  # f = open('spsram_64x63m4s_tt1v25c.txt','r')
                arr = np.array([])[:, np.newaxis]

                for line in f:
                    if "Width" in line and "Area" in line:
                        line = f.readline()
                        line = f.readline()
                        line = re.findall(r"\d+\.?\d*", line)
                        f3 = np.expand_dims(np.array(float(line[-1])), axis=0)[:, np.newaxis]
                        f2 = np.expand_dims(np.array(float(line[-2])), axis=0)[:, np.newaxis]
                        f1 = np.expand_dims(np.array(float(line[-3])), axis=0)[:, np.newaxis]
                        arr = np.concatenate((arr, f1, f2, f3), axis=0)
                        print('Area')
                        print(arr)
                    if "Leakage Current" in line and "uA" in line:
                        line = re.findall(r"\d+\.?\d*", line)
                        f3 = np.expand_dims(np.array(float(line[2])), axis=0)[:, np.newaxis]
                        f2 = np.expand_dims(np.array(float(line[1])), axis=0)[:, np.newaxis]
                        f1 = np.expand_dims(np.array(float(line[0])), axis=0)[:, np.newaxis]
                        arr = np.concatenate((arr, f1, f2, f3), axis=0)
                        print('Leakage Current')
                        print(arr)
                    if "Factor" in line and "Value" in line:
                        line = f.readline()
                        for p in range(7):
                            line = f.readline()
                            line = re.findall(r"\d+\.?\d*", line)
                            f1 = np.expand_dims(np.array(float(line[-1])), axis=0)[:, np.newaxis]
                            arr = np.concatenate((arr, f1), axis=0)
                        print('Factor')
                        print(arr)
                f.close()
                np.save(np_path + list1[i][:-3], arr)

            rename2(ds_path, 'txt')

        elif list1[0][-4:] == 'summ':
            rename1(ds_path, 'summ')
            list2 = os.listdir(ds_path)
            i = 0
            for i in range(length1):
                print(list2[i])
                f = open(ds_path + list2[i], 'r')  # np.load('ram1kx32_2p1r1w.summ.npy')
                arr = np.array([])[:, np.newaxis]
                for line in f:
                    if "CONFIGURATION" in line and "Power" in line:
                        line = f.readline()
                        line = re.findall(r"\d+\.?\d*", line)
                        f2 = np.expand_dims(np.array(float(line[-1])), axis=0)[:, np.newaxis]
                        f1 = np.expand_dims(np.array(float(line[-2])), axis=0)[:, np.newaxis]
                        arr = np.concatenate((arr, f1, f2), axis=0)
                        print('CONFIGURATION')
                        print(arr)
                    if "Voltage" in line and "Temperature" in line:
                        line = f.readline()
                        line = re.findall(r"\d+\.?\d*", line)
                        f4 = np.expand_dims(np.array(float(line[3])), axis=0)[:, np.newaxis]
                        f3 = np.expand_dims(np.array(float(line[2])), axis=0)[:, np.newaxis]
                        f2 = np.expand_dims(np.array(float(line[1])), axis=0)[:, np.newaxis]
                        f1 = np.expand_dims(np.array(float(line[0])), axis=0)[:, np.newaxis]
                        arr = np.concatenate((arr, f1, f2, f3, f4), axis=0)
                        print('Voltage')
                        print(arr)
                f.close()
                np.save(np_path + list1[i][:-5], arr)

            rename3(ds_path, 'txt')

    else:
        continue


for u in range(2,9):  # 提取lvlib
    if os.path.exists(path0 + str(u) + '/'):
        path = path0 + str(u) + '/'
        np_path = path + 'ds_np/'
        lvlib_path = path + 'lvlib/'

        if not os.path.exists(np_path):
            os.makedirs(np_path)
        # np.load("D:/PythonProj/edac_gwx_testcases/testcase03/ds_np/spsram_256x12m2s_tt1v25c.txt.npy")
        list1 = os.listdir(lvlib_path)
        length1 = len(list1)

        g = os.listdir(ds_path)
        g = g[0].split('_')
        key = re.findall(r"\w+\w*", g[-1])[0]
        h = list1[0].split('_')
        key1 = re.findall(r"\w+\w*", h[-1])[0]
        rename5(lvlib_path,key,key1)
        list3 = os.listdir(lvlib_path)

        print(length1)

        if list1[0][-3:] == 'lib' or list1[0][-3:] == 'txt':
            rename1(lvlib_path, 'lib')
            list2 = os.listdir(lvlib_path)
            for v in range(length1):

                print(list2[v])

                f = open(lvlib_path + list2[v], 'r')  # f = open('spsram_64x63m4s_tt1v25c.txt','r')
                arr = np.array([])[:, np.newaxis]
                for line in f:
                    if "CellName" in line:
                        line = f.readline()
                        line = re.findall(r"\w+\.?\w*", line)
                        algo_arr = np.expand_dims(np.array(line[-1]), axis=0)[:, np.newaxis]
                        #print(algo_arr)
                        FLAG = False
                        #print(algo_dic)
                        if algo_dic.size != 0:
                            for j in range(0, len(algo_dic)): # dic中是否存在这个算法
                                if line[-1] == algo_dic[j]:
                                    f1 = np.expand_dims(np.array(float(j)), axis=0)[:, np.newaxis]
                                    FLAG = True  # 已存在
                                    break
                            if not FLAG:  # 不存在时
                                algo_dic = np.concatenate((algo_dic, algo_arr), axis=0)
                                f1 = len(algo_dic) - 1
                                f1 = np.expand_dims(np.array(float(f1)), axis=0)[:, np.newaxis]
                                FLAG = False
                        else:
                            algo_dic = np.concatenate((algo_dic, algo_arr), axis=0)
                            f1 = len(algo_dic)-1
                            f1 = np.expand_dims(np.array(float(f1)), axis=0)[:, np.newaxis]

                        line = f.readline()
                        line = re.findall(r"\w+\.?\w*", line)
                        LP_arr = np.expand_dims(np.array(line[-1]), axis=0)[:, np.newaxis]
                        FLAG2 = False
                        if LP_dic.size != 0:
                            for j in range(0, len(LP_dic)):
                                if line[-1] == LP_dic[j]:
                                    f2 = np.expand_dims(np.array(float(j)), axis=0)[:, np.newaxis]
                                    FLAG = True  # 已存在
                                    break
                            if not FLAG:  # 不存在时
                                algo_dic = np.concatenate((algo_dic, algo_arr), axis=0)
                                f2 = len(algo_dic) - 1
                                f2 = np.expand_dims(np.array(float(f2)), axis=0)[:, np.newaxis]
                                FLAG = False
                        else:
                            LP_dic = np.concatenate((LP_dic, algo_arr), axis=0)
                            f2 = len(LP_dic)-1
                            f2 = np.expand_dims(np.array(float(f2)), axis=0)[:, np.newaxis]

                        line = f.readline()
                        line = re.findall(r"\d+\.?\d*", line)
                        f3 = np.expand_dims(np.array(line[-1]), axis=0)[:, np.newaxis]
                        arr = np.concatenate((arr, f1, f2, f3), axis=0)
                        print('#####################################################')
                        print('ALGO+LogiPort+WordDepth')
                        print(arr)
                f.close()
                print('#####################################################')
                arr0 = np.load(np_path + list3[v][:-4]+'.npy')
                arr1 = np.concatenate((arr0, arr), axis=0)
                np.save(np_path + list1[v][:-4], arr1)
                print(arr1)
            rename4(lvlib_path, 'txt')
        rename5(lvlib_path,key1,key)
    else:
        continue  #  #

