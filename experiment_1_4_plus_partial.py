import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import random
import perturbation_tool
from scipy.stats import wasserstein_distance

def main ():
    JS_multiTimes_Laplace = []
    JS_multiTimes_distPreserving = []
    dimension = 50
    round_number = 10
    for round_count in range(round_number):
        print("第几轮了:",round_count)
        EMD_Laplace = []
        EMD_distPreserving = []
        EMD_Laplace_plus = []
        EMD_distPreserving_plus = []
        JS_Laplace = []
        JS_distPreserving = []
        proportion_list = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
        for proportion in proportion_list:
            print('proportion:', proportion,'%')
            # temp_list = np.random.normal(mu, sigma, dimension*dimension)
            # user_number_list = list(map(int,np.rint(temp_list).tolist()))
            # # print(user_number_list)
            # for i in range(len(user_number_list)):
            #     if user_number_list[i] < 0:
            #         user_number_list[i] = 0
            # frequency_1 = np.array(user_number_list)
            np.random.seed(int(time.time()))
            frequency_1 = np.random.randint(0,50,dimension*dimension)
            perturbedFrequency_Laplace = [0 for i in range(dimension*dimension)]
            perturbedFrequency_distPreserving = [0 for i in range(dimension*dimension)]
            for i in range(len(frequency_1)):
                Epsilon_list = []
                for epsilon_count in range(frequency_1[i]):
                    Epsilon = random.uniform(0.1, 1)
                    Epsilon_list.append(Epsilon)
                oneDimensionLocation = i + 1
                if oneDimensionLocation % 200 == 0:
                    print('进度: ' + str(oneDimensionLocation) + '/' + str(dimension * dimension))
                reportedLocation_Laplace = perturbation_tool.perturbationOnOneLocation_userProportion(oneDimensionLocation,
                                                                                                     frequency_1[i],
                                                                                                     dimension,
                                                                                                     Epsilon_list,proportion)
                reportedLocation_distPreserving = perturbation_tool.perturbationOnOneLocation_patternPreserving_userProportion(
                    oneDimensionLocation,
                    frequency_1[i], dimension,
                    frequency_1, Epsilon_list,proportion)
                for i in reportedLocation_Laplace:
                    perturbedFrequency_Laplace[i - 1] += 1
                for i in reportedLocation_distPreserving:
                    perturbedFrequency_distPreserving[i - 1] += 1
            perturbedFrequency_Laplace_numpy = np.array(perturbedFrequency_Laplace)
            perturbedFrequency_distPreserving_numpy = np.array(perturbedFrequency_distPreserving)
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
            EMD_Laplace_plus.append(wasserstein_distance(frequency_orgin,frequency_perturbed_Laplace))
            EMD_distPreserving_plus.append(wasserstein_distance(frequency_orgin,frequency_perturbed_distPreserving))
            JS_Laplace.append(perturbation_tool.JS_divergence(formalized_orgin,formalized_perturbed_Laplace))
            JS_distPreserving.append(perturbation_tool.JS_divergence(formalized_orgin,formalized_perturbed_distPreserving))
        print("JS divergence")
        JS_multiTimes_Laplace.append(JS_Laplace)
        JS_multiTimes_distPreserving.append(JS_distPreserving)
    mean_list = []
    std_list = []
    for k in range(len(proportion_list)):
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
    for k in range(len(proportion_list)):
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