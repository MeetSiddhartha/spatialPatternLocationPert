import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import random
import perturbation_tool
from scipy.stats import wasserstein_distance


def main ():
    dimension = 50
    EMD_Laplace = []
    EMD_distPreserving = []
    EMD_Laplace_plus = []
    EMD_distPreserving_plus = []
    JS_Laplace = []
    JS_distPreserving = []
    # mu = 10 #10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
    mu_list = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    sigma = 10
    for mu in mu_list:
        temp_list = np.random.normal(mu, sigma, dimension*dimension)
        user_number_list = list(map(int,np.rint(temp_list).tolist()))
        for i in range(len(user_number_list)):
            if user_number_list[i] < 0:
                user_number_list[i] = 0
        frequency_1 = np.array(user_number_list)
        print('真实分布:',frequency_1)
        perturbedFrequency_Laplace = [0 for i in range(dimension*dimension)]
        perturbedFrequency_distPreserving = [0 for i in range(dimension*dimension)]

        for i in range(len(frequency_1)):
            Epsilon_list = []
            for epsilon_count in range(frequency_1[i]):
                Epsilon = random.uniform(0.1, 1)
                Epsilon_list.append(Epsilon)
            oneDimensionLocation = i+1
            if oneDimensionLocation % 200 == 0:
                print(oneDimensionLocation)
            reportedLocation_Laplace = perturbation_tool.perturbationOnOneLocation_randomEpsilon(oneDimensionLocation,frequency_1[i],dimension,Epsilon_list) #Laplace 扰动
            reportedLocation_distPreserving = perturbation_tool.perturbationOnOneLocation_patternPreserving_randomEpsilon(oneDimensionLocation,
                                                                                             frequency_1[i], dimension,
                                                                                             frequency_1,Epsilon_list)  # distPreving 扰动
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

        JS_Laplace.append(perturbation_tool.JS_divergence(formalized_orgin,formalized_perturbed_Laplace))
        JS_distPreserving.append(perturbation_tool.JS_divergence(formalized_orgin,formalized_perturbed_distPreserving))
    print("JS divergence")
    print(JS_Laplace)
    print(JS_distPreserving)

if __name__ =='__main__':
    main ()