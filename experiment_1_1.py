import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import perturbation_tool
import math
from scipy.stats import wasserstein_distance

def main ():
    dimension = 50
    Epsilon = 0.5
    perturbedFrequency_Laplace = [0 for i in range(dimension*dimension)]
    perturbedFrequency_distPreserving = [0 for i in range(dimension*dimension)]
    np.random.seed(int(time.time()))
    frequency_1 = np.random.randint(0,50,dimension*dimension)
    print(frequency_1)

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
    print(perturbedFrequency_Laplace_numpy)
    print(perturbedFrequency_distPreserving_numpy)

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

    frequency_orgin = frequency_orgin.reshape((dimension,dimension))
    frequency_perturbed_Laplace = frequency_perturbed_Laplace.reshape((dimension,dimension))
    frequency_perturbed_distPreserving = frequency_perturbed_distPreserving.reshape((dimension,dimension))
    tempcmap = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True) # 与"YlGnBu"，"rainbow"是可以替换的
    sns.heatmap(frequency_orgin,annot=False,linewidths = 0,xticklabels=False,yticklabels=False,cmap="YlGnBu",cbar=False) #,vmax = 1,vmin = 0，"YlGnBu"，"rainbow"
    plt.savefig("Fig2(查询频率(扰动前)).png",bbox_inches = 'tight')
    sns.heatmap(frequency_perturbed_Laplace,annot=False,linewidths = 0,xticklabels=False,yticklabels=False,cbar=False,cmap="YlGnBu") #,vmax = 1,vmin = 0，"YlGnBu"，"rainbow"
    plt.savefig("Fig2(查询频率(Laplace扰动后)).png",bbox_inches = 'tight')
    sns.heatmap(frequency_perturbed_distPreserving,annot=False,linewidths = 0,xticklabels=False,yticklabels=False,cbar=True,cmap="YlGnBu") #,vmax = 1,vmin = 0，"YlGnBu"，"rainbow"
    plt.savefig("Fig2(查询频率(distPreserving扰动后)).png",bbox_inches = 'tight')

    plt.figure(figsize=(12,3.5))
    plt.subplot(131)
    sns.heatmap(frequency_orgin,annot=False,linewidths = 0,xticklabels=False,yticklabels=False,cmap="YlGnBu",cbar=False) #,vmax = 1,vmin = 0，"YlGnBu"，"rainbow"
    plt.subplot(132)
    sns.heatmap(frequency_perturbed_Laplace,annot=False,linewidths = 0,xticklabels=False,yticklabels=False,cbar=False,cmap="YlGnBu") #,vmax = 1,vmin = 0，"YlGnBu"，"rainbow"
    plt.subplot(133)
    sns.heatmap(frequency_perturbed_distPreserving,annot=False,linewidths = 0,xticklabels=False,yticklabels=False,cbar=True,cmap="YlGnBu") #,vmax = 1,vmin = 0，"YlGnBu"，"rainbow"
    plt.tight_layout()
    plt.savefig("Fig2(三合一).png",bbox_inches = 'tight')

    print("JS divergence")
    print(perturbation_tool.JS_divergence(formalized_orgin,formalized_perturbed_Laplace),perturbation_tool.JS_divergence(formalized_perturbed_Laplace,formalized_orgin))
    print(perturbation_tool.JS_divergence(formalized_orgin,formalized_perturbed_distPreserving),perturbation_tool.JS_divergence(formalized_perturbed_distPreserving,formalized_orgin))

if __name__ =='__main__':
    main ()