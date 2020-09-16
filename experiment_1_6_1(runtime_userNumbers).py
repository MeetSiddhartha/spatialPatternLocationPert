import numpy as np
import time
import Tools
import matplotlib.pyplot as plt
import seaborn as sns
import perturbation_tool
from scipy.stats import wasserstein_distance

def main ():
    Epsilon = 0.5
    dimension = 50
    SNR = 0.0000
    realLocation = np.random.randint(0,dimension*dimension-1,1)
    howManyPeople = 1000
    n = howManyPeople
    numberofusers_list = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
    sigma = 10
    np.random.seed(int(time.time()))
    userDistribution = 'normal'
    meanTimeList = []
    for numberofusers in numberofusers_list:
        frequency_1 = np.random.randint(0,numberofusers,dimension*dimension)
        spatialPattern = frequency_1
        matrix_Sequence = [[0 for i in range(dimension)] for i in range(dimension)]
        Tools.Sequencelize_Matrix(matrix_Sequence)
        matrix_Distance = [[0 for i in range(dimension)] for i in range(dimension)]
        matrix_Weight = [[0 for i in range(dimension)] for i in range(dimension)]
        matrix_Probabiliity = [[0 for i in range(dimension)] for i in range(dimension)]
        time_start = time.time()
        Tools.calculateDistanceMatrix_PatternPreserving(matrix_Sequence, matrix_Distance, realLocation, dimension, spatialPattern)
        irrationalLocationList = []
        cum = Tools.calculateWeightMatrix(Epsilon,dimension,matrix_Distance,matrix_Weight)
        Tools.calculateProbabiliityMatrix(matrix_Probabiliity,matrix_Weight,realLocation,irrationalLocationList,cum,dimension)
        reportedLocation = Tools.sampleFromProbabiliity(matrix_Probabiliity,dimension,n)
        time_end = time.time()
        timeCost = (time_end - time_start) / n
        print(timeCost)
        meanTimeList.append(timeCost)
    print('totally cost')
    print(meanTimeList)

if __name__ =='__main__':
    main ()