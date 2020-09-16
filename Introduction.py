import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import random

def main ():
    np.random.seed(int(time.time()))
    frequency_1 = np.random.randint(0,100,100)
    print(frequency_1)
    sum = 0
    for i in range(len(frequency_1)):
        sum += frequency_1[i]
    list_np = []
    for i in range(len(frequency_1)):
        list_np.append(frequency_1[i]/sum)
    frequency = np.array(list_np)
    print(frequency)
    frequency = frequency.reshape((10,10))
    tempcmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
    sns.heatmap(frequency,annot=False,linewidths = 0,xticklabels=False,yticklabels=False,cbar=True,cmap="YlGnBu")
    plt.savefig("Fig1(查询频率模拟图).jpg")

if __name__ =='__main__':
    main ()