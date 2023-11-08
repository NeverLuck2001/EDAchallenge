import numpy as np
import os

np_final_path = './np_final_path/'
list = os.listdir(np_final_path)
arr = np.expand_dims(np.expand_dims(np.array([]),axis=0),axis=2)

FLAG = False

for filename in list:
    if FLAG is False:
        data = np.load(np_final_path+filename)[np.newaxis,]
        arr = np.concatenate((arr,data),axis=1)
        FLAG = True
    else:
        data = np.load(np_final_path+filename)[np.newaxis,]
        arr = np.concatenate((arr, data), axis=0)
    #print(arr)
    np.save('total.npy',arr)
