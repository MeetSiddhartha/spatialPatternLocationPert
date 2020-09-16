import Tools
import numpy as np
import time
import random
import math

def main ():
    Epsilon = 0.5
    dimension = 50
    SNR = 0.0000
    threshold = 5
    numberofusers_list = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
    mu_list = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
    sigma = 10
    np.random.seed(int(time.time()))
    userDistribution = 'uniform'
    n = 1
    laplaceRuntime_meanList = []
    laplaceRuntime_stdList = []
    for numberofusers in numberofusers_list:
        print('用户数期望:', numberofusers)
        count_list = []
        for number in range(1000):
            realLocation = np.random.randint(0, dimension * dimension - 1, 1)
            if userDistribution == 'uniform':
                frequency_1 = np.random.randint(0, numberofusers, dimension * dimension)
            elif userDistribution == 'normal':
                temp_list = np.random.normal(numberofusers, sigma, dimension*dimension)
                user_number_list = list(map(int,np.rint(temp_list).tolist()))
                for i in range(len(user_number_list)):
                    if user_number_list[i] < 0:
                        user_number_list[i] = 0
                frequency_1 = np.array(user_number_list)

            matrix_Sequence = [[0 for i in range(dimension)] for i in range(dimension)]
            Tools.Sequencelize_Matrix(matrix_Sequence)
            matrix_Distance = [[0 for i in range(dimension)] for i in range(dimension)]
            matrix_Weight = [[0 for i in range(dimension)] for i in range(dimension)]
            matrix_Probabiliity = [[0 for i in range(dimension)] for i in range(dimension)]
            Tools.calculateDistanceMatrix(matrix_Sequence,matrix_Distance,realLocation,dimension)
            irrationalLocationList = []
            cum = Tools.calculateWeightMatrix(Epsilon,dimension,matrix_Distance,matrix_Weight)
            Tools.calculateProbabiliityMatrix(matrix_Probabiliity,matrix_Weight,realLocation,irrationalLocationList,cum,dimension)
            count = 1
            reportedLocation = Tools.sampleFromProbabiliity(matrix_Probabiliity,dimension,n)
            while abs(frequency_1[reportedLocation-1] - frequency_1[realLocation]) > threshold:
                count = count + 1
                reportedLocation = Tools.sampleFromProbabiliity(matrix_Probabiliity,dimension,n)
            count_list.append(count)
        print(count_list)
        print('Laplace重复次数的均值，标准差:')
        Repetition_number_mean = np.mean(count_list)
        Repetition_number_std = np.std(count_list, ddof=1)
        print(Repetition_number_mean)
        print(Repetition_number_std)
        single_laplacian_time = [7.400012016296387e-05, 7.399988174438476e-05, 7.500004768371582e-05, 7.800006866455078e-05, 7.599997520446777e-05, 7.599997520446777e-05, 7.800006866455078e-05, 7.699990272521973e-05, 7.399988174438476e-05, 7.800006866455078e-05]
        laplace_runtime_mean = Repetition_number_mean * random.choice(single_laplacian_time)
        laplace_runtime_std = Repetition_number_std * random.choice(single_laplacian_time)
        laplaceRuntime_meanList.append(laplace_runtime_mean)
        laplaceRuntime_stdList.append(laplace_runtime_std)
        print('Laplace运行时间的均值，标准差:')
        print(laplace_runtime_mean)
        print(laplace_runtime_std)
    print(laplaceRuntime_meanList)
    print(laplaceRuntime_stdList)

if __name__ =='__main__':
    main ()