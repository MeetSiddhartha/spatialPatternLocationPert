import math
import numpy as np
import random


def Intersection_area(r1,r2,distance):
    if distance > r1 + r2:
        return 0
    elif r1 + distance <= r2 or r2 + distance <= r1:
        return min(r1,r2)**2 * math.pi
    else:
        ang1 = math.acos((r1 * r1 + distance * distance - r2 * r2) / (2 * r1 * distance));
        ang2 = math.acos((r2 * r2 + distance * distance - r1 * r1) / (2 * r2 * distance));
        return ang1 * r1 * r1 + ang2 * r2 * r2 - r1 * distance * math.sin(ang1);
def addNoise(numList):
    noised_list = []
    errorExpect = abs(numList[0]-numList[1])
    noise_list = np.random.normal(0, errorExpect/3.5, len(numList))
    noise_list = list(noise_list)
    for i in range(len(numList)):
        if numList[i] == 1:
            noised_list.append(1)
        else:
            if numList[i] + noise_list[i] <= 1:
                noised_list.append(numList[i] + noise_list[i])
            else:
                noised_list.append(1)
    return noised_list

def main ():
    R_AOI = 500
    distance_error = [41.604700552178521, 38.69440617833417, 38.672601986369749, 37.838984916181097, 36.145091079463285, 40.992663894684711, 37.277817366966502, 38.297674392241987, 37.448347907124131, 38.440902157311534]
    R_AOR_our = [548, 548, 548, 548, 548, 548, 548, 548, 548, 548]
    print('Epsilon变化情况')
    print('我们的方案:')
    Recall = []
    for i in range(len(distance_error)):
        recall = Intersection_area(R_AOI, R_AOR_our[i], distance_error[i]) / (R_AOI**2 * math.pi)
        Recall.append(recall)
    print(Recall)
    Precision = []
    for i in range(len(distance_error)):
        precision = Intersection_area(R_AOI, R_AOR_our[i], distance_error[i]) / (R_AOR_our[i] ** 2 * math.pi)
        Precision.append(precision)
    print(Precision)
    print(addNoise(Precision))

    R_AOI = 500
    distance_error = [39.48009212929151, 19.877477733493894, 13.24142317521886, 10.1812672969511, 8.171764948674014, 6.748007990509669, 5.8611598589895975, 5.074996552607749, 4.587352816681741, 3.968089646103063]
    R_AOR_our = [524.392164832802, 512.196082416401, 508.130721610934, 506.0980412082005, 504.8784329665604, 504.065360805467, 503.4845949761146, 503.04902060410024, 502.710240536978, 502.4392164832802]
    print('平面拉普拉斯方案:')
    Recall = []
    for i in range(len(distance_error)):
        recall = Intersection_area(R_AOI, R_AOR_our[i], distance_error[i]) / (R_AOI**2 * math.pi)
        Recall.append(recall)
    print(Recall)
    Precision = []
    for i in range(len(distance_error)):
        precision = Intersection_area(R_AOI, R_AOR_our[i], distance_error[i]) / (R_AOR_our[i] ** 2 * math.pi)
        Precision.append(precision)
    print(Precision)

    R_AOI = 500
    distance_error = [37.683724832025057, 35.594446629100659, 35.957381443277669, 38.973929247967973, 37.902584676534211, 37.246916442517097, 37.51259454297157, 38.412254925786009, 38.685703698619776]
    R_AOR_our = [518, 526, 531,536,540,544,548,551,556]
    print()
    print('C_accuracy变化情况')
    print('我们的方案:')
    Recall = []
    for i in range(len(distance_error)):
        recall = Intersection_area(R_AOI, R_AOR_our[i], distance_error[i]) / (R_AOI**2 * math.pi)
        Recall.append(recall)
    print(Recall)

    Precision = []
    for i in range(len(distance_error)):
        precision = Intersection_area(R_AOI, R_AOR_our[i], distance_error[i]) / (R_AOR_our[i] ** 2 * math.pi)
        Precision.append(precision)
    print(Precision)

    R_AOI = 500
    distance_error = [13.266259986472557, 13.474181377473844, 14.286043502874307, 12.396333906894679, 13.279288160726122, 15.127417434707281, 13.547665035698664, 14.939324104543225, 13.852485146159998]
    R_AOR_our = [501.77270536129873, 502.74796103010993, 503.657830702345, 504.58807114020965, 505.5944899667222, 506.7410441510822, 508.130721610934, 509.9810278233404, 512.9657338995581]
    print('平面拉普拉斯方案:')
    Recall = []
    for i in range(len(distance_error)):
        recall = Intersection_area(R_AOI, R_AOR_our[i], distance_error[i]) / (R_AOI**2 * math.pi)
        Recall.append(recall)
    print(Recall)

    Precision = []
    for i in range(len(distance_error)):
        precision = Intersection_area(R_AOI, R_AOR_our[i], distance_error[i]) / (R_AOR_our[i] ** 2 * math.pi)
        Precision.append(precision)
    print(Precision)

    R_AOI = [300,400,500,600,700,800,900,1000]
    distance_error = [37.683724832025057, 35.594446629100659, 35.957381443277669, 38.973929247967973, 37.902584676534211, 37.246916442517097, 37.51259454297157, 38.412254925786009]
    R_AOR_our = [348, 448, 548, 648, 748, 848, 948, 1048]
    print()
    print('R_AOI变化情况')
    print('我们的方案:')

    Recall = []
    for i in range(len(distance_error)):
        recall = Intersection_area(R_AOI[i], R_AOR_our[i], distance_error[i]) / (R_AOI[i]**2 * math.pi)
        Recall.append(recall)
    print(Recall)

    Precision = []
    for i in range(len(distance_error)):
        precision = Intersection_area(R_AOI[i], R_AOR_our[i], distance_error[i]) / (R_AOR_our[i] ** 2 * math.pi)
        Precision.append(precision)
    print(Precision)

    R_AOI = [300,400,500,600,700,800,900,1000]
    distance_error = [13.348594588783524, 13.79369955866288, 13.074056822368204, 12.804988938522364, 12.50784177918609, 13.157571750586843, 12.945625928050028,13.358682861387605]
    R_AOR_our = [308.130721610934, 408.130721610934, 508.130721610934, 608.130721610934, 708.130721610934, 808.130721610934, 908.130721610934, 1008.130721610934]
    print('平面拉普拉斯方案:')

    Recall = []
    for i in range(len(distance_error)):
        recall = Intersection_area(R_AOI[i], R_AOR_our[i], distance_error[i]) / (R_AOI[i]**2 * math.pi)
        Recall.append(recall)
    print(Recall)

    Precision = []
    for i in range(len(distance_error)):
        precision = Intersection_area(R_AOI[i], R_AOR_our[i], distance_error[i]) / (R_AOR_our[i] ** 2 * math.pi)
        Precision.append(precision)
    print(Precision)

if __name__ =='__main__':
    main ()