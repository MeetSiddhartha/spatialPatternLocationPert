# 采用真实数据集，划分为网格区域，产生用户位置的分布（五环以内）
import pandas as pd
import matplotlib.pyplot as plt
import random as rd



def main ():
    print(rd.random())
    dimension = 100
    matrix_userDistribution = [[0 for i in range(dimension)] for i in range(dimension)]
    x_length = 475144.9697096213 - 423404.88791599206
    y_length = 4445627.808702538 - 4393774.2244457025

    print(int(5.12534))

    for k in range(18670):
        if rd.random() < 0.2:
            file_count=k
            original_fileName = "F:/Data_New/DaDiZuoBiao/user" + str(file_count) + ".txt"
            print(original_fileName)
            df = pd.read_table(original_fileName,'r',delimiter = ',',names = ["x","y"])
            print(df.index.max())
            for i in range(df.index.max()+1):
                if any([df.loc[i, 'x'] < 423404.88791599206 or df.loc[i, 'x'] > 475144.9697096213,
                    df.loc[i, 'y'] < 4393774.2244457025 or df.loc[i, 'y'] > 4445627.808702538]):
                    continue
                else:
                    ratio_x = (df.loc[i, 'x'] - 423404.88791599206) / x_length
                    ratio_y = (df.loc[i, 'y'] - 4393774.2244457025) / y_length
                    matrix_userDistribution[int(ratio_x * dimension) - 1][int(ratio_y * dimension) - 1] += 1
    print(matrix_userDistribution)
    print(len(matrix_userDistribution))
    frequency_1 = [i for j in matrix_userDistribution for i in j]
    print()
    print(frequency_1)
    print(len(frequency_1))

if __name__ =='__main__':
    main ()



