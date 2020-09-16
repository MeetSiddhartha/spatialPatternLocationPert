import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import random
import perturbation_tool
from scipy.stats import wasserstein_distance

def main ():
    dimension = 20
    EMD_Laplace = []
    EMD_distPreserving = []
    JS_Laplace = []
    JS_distPreserving = []

    perturbedFrequency_Laplace = [0 for i in range(dimension*dimension)]
    perturbedFrequency_distPreserving = [0 for i in range(dimension*dimension)]
    np.random.seed(int(time.time()))
    frequency_1 = np.random.randint(0,50,dimension*dimension)
    print('真实分布:',frequency_1)

    for i in range(len(frequency_1)):
        Epsilon_list = []
        for epsilon_count in range(frequency_1[i]):
            Epsilon = random.uniform(0.1, 1)
            Epsilon_list.append(Epsilon)
        oneDimensionLocation = i+1
        if oneDimensionLocation % 200 == 0:
            print(oneDimensionLocation)
        reportedLocation_Laplace = perturbation_tool.perturbationOnOneLocation_randomEpsilon(oneDimensionLocation,frequency_1[i],dimension,Epsilon_list)
        reportedLocation_distPreserving = perturbation_tool.perturbationOnOneLocation_patternPreserving_randomEpsilon(oneDimensionLocation,
                                                                                         frequency_1[i], dimension,
                                                                                         frequency_1,Epsilon_list)
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
    print(JS_Laplace)
    print(JS_distPreserving)

if __name__ =='__main__':
    main ()