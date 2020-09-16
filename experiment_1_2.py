import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import perturbation_tool
from scipy.stats import wasserstein_distance


def main ():
    dimension = 50
    JS_multiTimes_Laplace = []
    JS_multiTimes_distPreserving = []
    round_number = 10
    for round_count in range(round_number):
        print("第几轮了:", round_count)
        EMD_Laplace = []
        EMD_distPreserving = []
        JS_Laplace = []
        JS_distPreserving = []
        Epsilon_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        for Epsilon in Epsilon_list:
            print('Epsilon:',Epsilon)
            perturbedFrequency_Laplace = [0 for i in range(dimension*dimension)]
            perturbedFrequency_distPreserving = [0 for i in range(dimension*dimension)]
            np.random.seed(int(time.time()))
            frequency_1 = np.random.randint(0,50,dimension*dimension)
            print('真实分布:',frequency_1)

            for i in range(len(frequency_1)):
                oneDimensionLocation = i+1
                if oneDimensionLocation % 200 == 0:
                    print(oneDimensionLocation)
                reportedLocation_Laplace = perturbation_tool.perturbationOnOneLocation(oneDimensionLocation,frequency_1[i],dimension,Epsilon)
                reportedLocation_distPreserving = perturbation_tool.perturbationOnOneLocation_patternPreserving(oneDimensionLocation,
                                                                                                 frequency_1[i], dimension,
                                                                                                 frequency_1,Epsilon)
                for i in reportedLocation_Laplace:
                    perturbedFrequency_Laplace[i-1] += 1
                for i in reportedLocation_distPreserving:
                    perturbedFrequency_distPreserving[i-1] += 1
            perturbedFrequency_Laplace_numpy = np.array(perturbedFrequency_Laplace)
            perturbedFrequency_distPreserving_numpy = np.array(perturbedFrequency_distPreserving)
            print('Laplace扰动分布',perturbedFrequency_Laplace_numpy)
            print('distPreserving扰动分布',perturbedFrequency_distPreserving_numpy,'\n')

            sum_orgin = 0
            sum_perturbed_Laplace = 0
            sum_perturbed_distPreserving = 0
            for i in range(len(frequency_1)):
                sum_orgin += frequency_1[i]
                sum_perturbed_Laplace += perturbedFrequency_Laplace[i]
                sum_perturbed_distPreserving += perturbedFrequency_distPreserving[i]
            if sum_orgin != sum_perturbed_Laplace:
                print('Error 1')
            elif sum_orgin != sum_perturbed_distPreserving:
                print('Error 2')
            formalized_orgin = []
            formalized_perturbed_Laplace = []
            formalized_perturbed_distPreserving = []
            for i in range(len(frequency_1)):
                formalized_orgin.append(frequency_1[i]/sum_orgin)
                formalized_perturbed_Laplace.append(perturbedFrequency_Laplace[i]/sum_perturbed_Laplace)
                formalized_perturbed_distPreserving.append(perturbedFrequency_distPreserving[i] / sum_perturbed_distPreserving)
            frequency_orgin = np.array(formalized_orgin)
            frequency_perturbed_Laplace = np.array(formalized_perturbed_Laplace)
            frequency_perturbed_distPreserving = np.array(formalized_perturbed_distPreserving)

            EMD_Laplace.append(wasserstein_distance(frequency_1, perturbedFrequency_Laplace_numpy))
            EMD_distPreserving.append(wasserstein_distance(frequency_1, perturbedFrequency_distPreserving_numpy))

            JS_Laplace.append(perturbation_tool.JS_divergence(formalized_orgin,formalized_perturbed_Laplace))
            JS_distPreserving.append(perturbation_tool.JS_divergence(formalized_orgin,formalized_perturbed_distPreserving))
        print("JS divergence")
        JS_multiTimes_Laplace.append(JS_Laplace)
        JS_multiTimes_distPreserving.append(JS_distPreserving)

    mean_list = []
    std_list = []
    for k in range(len(Epsilon_list)):
        column_list = []
        for i in range(len(JS_multiTimes_Laplace)):
            column_list.append(JS_multiTimes_Laplace[i][k])
        column_numpyList = np.array(column_list)
        column_mean = np.mean(column_numpyList)
        column_std = np.std(column_numpyList,ddof=1)
        mean_list.append(column_mean)
        std_list.append(column_std)
    print('Laplace下JS距离的均值，标准差:')
    print(mean_list)
    print(std_list)

    mean_list = []
    std_list = []
    for k in range(len(Epsilon_list)):
        column_list = []
        for i in range(len(JS_multiTimes_distPreserving)):
            column_list.append(JS_multiTimes_distPreserving[i][k])
        column_numpyList = np.array(column_list)
        column_mean = np.mean(column_numpyList)
        column_std = np.std(column_numpyList,ddof=1)
        mean_list.append(column_mean)
        std_list.append(column_std)
    print('distPreserving下JS距离的均值，标准差:')
    print(mean_list)
    print(std_list)

if __name__ =='__main__':
    main ()