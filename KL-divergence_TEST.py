import math
from scipy.stats import wasserstein_distance
import numpy as np

P = [0,0.48,0.16]
Q = [0.33,0.3,0.33]

# # compute KL-divergence (also called Relative Entropy)
# def KL_divergence(list_P,list_Q):
#     KL_PQ = 0
#     for i in range(len(list_P)):
#         if list_P[i] == 0:
#             list_P[i] = np.mean(list_P)/100
#             # print(np.mean(list_P)/100,list_P[i])
#         if list_Q[i] == 0:
#             list_Q[i] = np.mean(list_Q)/100
#         # print( list_P[i],np.mean(list_P)/100)
#         KL_PQ += list_P[i] * math.log(list_P[i] / list_Q[i])
#     # print(KL_PQ)
#     return KL_PQ
#
# # compute JS-divergence (also called smoothed version of Relative Entropy)
# def JS_divergence(list_P,list_Q):
#     temp_list = [0 for i in range(len(list_P))]
#     for i in range(len(list_P)):
#         temp_list[i] = (list_P[i] + list_Q[i]) / 2
#     JS_PQ = 0.5 * KL_divergence(list_P, temp_list) + 0.5 * KL_divergence(list_Q, temp_list)
#     return JS_PQ
#
# print(KL_divergence(P,Q),KL_divergence(Q,P)) #KL divergence
# print(JS_divergence(P,Q),JS_divergence(Q,P)) #JS divergence

frequency_1 = np.array([0, 10, 3])
frequency_2 = np.array([0, 10, 2])
print(wasserstein_distance(frequency_1, frequency_2))
print(wasserstein_distance([0, 10, 3], [0, 10, 2]))

# print(JS_divergence(frequency_1,frequency_2),JS_divergence(frequency_2,frequency_1)) #JS divergence
