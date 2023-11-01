import numpy as np
import os
import re
from rename import rename1, rename2, rename3

path0 = './testcase0'
for q in range(10):
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
                    if "Pins" in line and "VDD" in line:
                        line = f.readline()
                        line = f.readline()
                        for p in range(13):
                            line = f.readline()
                            line = re.findall(r"\d+\.?\d*", line)
                            f1 = np.expand_dims(np.array(float(line[-1])), axis=0)[:, np.newaxis]
                            arr = np.concatenate((arr, f1), axis=0)
                        print('Pins')
                        print(arr)
                f.close()
                np.save(np_path + list1[i], arr)

            rename2(ds_path, 'txt')

        elif list1[0][-4:] == 'summ':
            rename1(ds_path, 'summ')
            list2 = os.listdir(ds_path)
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
                np.save(np_path + list1[i], arr)

            rename3(ds_path, 'txt')

    else:
        continue
