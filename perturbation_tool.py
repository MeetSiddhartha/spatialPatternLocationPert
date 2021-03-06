# For the sake of the commercialization requirements in the plan, we obfuscated this part of the code.
import Tools #line:1
import numpy as np #line:2
import math #line:3
import random #line:4
SNR =0.0000 #line:5
def perturbationOnOneLocation (O00OOO000O000OOOO ,O00O0O0O0OOOOOO0O ,O00O00OO00O0O000O ,OOOO00O00OO00OOO0 ):#line:6
    OO000000O0O000OOO =O00O0O0O0OOOOOO0O #line:7
    O0O0OOO00O000O0O0 =[[0 for OO000OOO000000OOO in range (O00O00OO00O0O000O )]for O0O000O0OOO0O00O0 in range (O00O00OO00O0O000O )]#line:8
    Tools .Sequencelize_Matrix (O0O0OOO00O000O0O0 )#line:9
    OOOO00O0000O0OO00 =[[0 for OOOO0OOOOO000OO00 in range (O00O00OO00O0O000O )]for O00OOO0O0O00O0OOO in range (O00O00OO00O0O000O )]#line:10
    O0OO0O0O0000OOO00 =[[0 for OOO00O0OO0OO0OOO0 in range (O00O00OO00O0O000O )]for OO0OOOOOO0OO00O0O in range (O00O00OO00O0O000O )]#line:11
    O0OO0O0O00000O000 =[[0 for O0OOO0OOO00O000O0 in range (O00O00OO00O0O000O )]for O0OO0OO0OOOO0OOOO in range (O00O00OO00O0O000O )]#line:12
    Tools .calculateDistanceMatrix (O0O0OOO00O000O0O0 ,OOOO00O0000O0OO00 ,O00OOO000O000OOOO ,O00O00OO00O0O000O )#line:13
    OO0OOO0O00OOOOO00 =Tools .irrationalLocationList (SNR ,O00OOO000O000OOOO ,O0O0OOO00O000O0O0 )#line:14
    O000OOO00OO0O0OO0 =Tools .calculateWeightMatrix (OOOO00O00OO00OOO0 ,O00O00OO00O0O000O ,OOOO00O0000O0OO00 ,O0OO0O0O0000OOO00 )#line:15
    Tools .calculateProbabiliityMatrix (O0OO0O0O00000O000 ,O0OO0O0O0000OOO00 ,O00OOO000O000OOOO ,OO0OOO0O00OOOOO00 ,O000OOO00OO0O0OO0 ,O00O00OO00O0O000O )#line:16
    OOO000O0O0O000000 =Tools .sampleFromProbabiliity (O0OO0O0O00000O000 ,O00O00OO00O0O000O ,OO000000O0O000OOO )#line:17
    return OOO000O0O0O000000 #line:18
def perturbationOnOneLocation_patternPreserving (OOO0OOOOO0O0O0000 ,O000OO00O0O0OO0OO ,O00OO00O0O0O00O00 ,O0OO000OOOO00O00O ,OO0OOOO0OO000OO00 ):#line:19
    OO00O0OO0OOOO0OOO =O000OO00O0O0OO0OO #line:20
    OOOO0OOO00O0OO00O =[[0 for OOOOO000000OO0OOO in range (O00OO00O0O0O00O00 )]for OOO0OO000000O000O in range (O00OO00O0O0O00O00 )]#line:21
    Tools .Sequencelize_Matrix (OOOO0OOO00O0OO00O )#line:22
    O00O0000OOO00OO00 =[[0 for OO0O00O000000OO00 in range (O00OO00O0O0O00O00 )]for O0O0O0OO00O0O0O00 in range (O00OO00O0O0O00O00 )]#line:23
    O000OO0OOOOO0OOO0 =[[0 for O0OO0O000000OOOO0 in range (O00OO00O0O0O00O00 )]for O0O0000O0OOOO00OO in range (O00OO00O0O0O00O00 )]#line:24
    OOOO000000O0OOOO0 =[[0 for OO0O00OO00O0OO0OO in range (O00OO00O0O0O00O00 )]for O00O0O000O0O0O00O in range (O00OO00O0O0O00O00 )]#line:25
    Tools .calculateDistanceMatrix_PatternPreserving (OOOO0OOO00O0OO00O ,O00O0000OOO00OO00 ,OOO0OOOOO0O0O0000 ,O00OO00O0O0O00O00 ,O0OO000OOOO00O00O )#line:26
    O0OO00OO000OO00O0 =Tools .irrationalLocationList (SNR ,OOO0OOOOO0O0O0000 ,OOOO0OOO00O0OO00O )#line:27
    OOOO0O0O00O0O0O00 =Tools .calculateWeightMatrix (OO0OOOO0OO000OO00 ,O00OO00O0O0O00O00 ,O00O0000OOO00OO00 ,O000OO0OOOOO0OOO0 )#line:28
    Tools .calculateProbabiliityMatrix (OOOO000000O0OOOO0 ,O000OO0OOOOO0OOO0 ,OOO0OOOOO0O0O0000 ,O0OO00OO000OO00O0 ,OOOO0O0O00O0O0O00 ,O00OO00O0O0O00O00 )#line:29
    OO00000O00OOOO00O =Tools .sampleFromProbabiliity (OOOO000000O0OOOO0 ,O00OO00O0O0O00O00 ,OO00O0OO0OOOO0OOO )#line:30
    return OO00000O00OOOO00O #line:31
def perturbationOnOneLocation_randomEpsilon (O00O0O0O0OO0OO000 ,O0O0OOO00O00OO00O ,OO0O0O0O000OOOO00 ,O0O0O000O0O0OO0OO ):#line:33
    if O0O0OOO00O00OO00O !=len (O0O0O000O0O0OO0OO ):#line:34
        print ('Error: Epsilon_list has a wrong length.')#line:35
    OO00OOOOO0OOOOOOO =1 #line:36
    O0000O0O00O00O0O0 =[[0 for O000OO0OOOO0OO00O in range (OO0O0O0O000OOOO00 )]for OO0O00O00O0O000O0 in range (OO0O0O0O000OOOO00 )]#line:37
    Tools .Sequencelize_Matrix (O0000O0O00O00O0O0 )#line:38
    OO0O0OOO0OOOOO000 =[[0 for O0000OO000OO000OO in range (OO0O0O0O000OOOO00 )]for OOO00O00OOO00000O in range (OO0O0O0O000OOOO00 )]#line:39
    OOOO0O0OO00O0O0O0 =[[0 for O0000O0OO00O0000O in range (OO0O0O0O000OOOO00 )]for O0O00O0OO000O0OOO in range (OO0O0O0O000OOOO00 )]#line:40
    O0000OOO0OOO00OOO =[[0 for OOO000000O000OO00 in range (OO0O0O0O000OOOO00 )]for O000OO0O0O0000O0O in range (OO0O0O0O000OOOO00 )]#line:41
    Tools .calculateDistanceMatrix (O0000O0O00O00O0O0 ,OO0O0OOO0OOOOO000 ,O00O0O0O0OO0OO000 ,OO0O0O0O000OOOO00 )#line:42
    OOOOOOOOO00O00OOO =Tools .irrationalLocationList (SNR ,O00O0O0O0OO0OO000 ,O0000O0O00O00O0O0 )#line:43
    OOOOO0OOO0O0O0O0O =[]#line:44
    for O00O000O0O0O000O0 in O0O0O000O0O0OO0OO :#line:45
        O000OO0O000O0O0OO =Tools .calculateWeightMatrix (O00O000O0O0O000O0 ,OO0O0O0O000OOOO00 ,OO0O0OOO0OOOOO000 ,OOOO0O0OO00O0O0O0 )#line:46
        Tools .calculateProbabiliityMatrix (O0000OOO0OOO00OOO ,OOOO0O0OO00O0O0O0 ,O00O0O0O0OO0OO000 ,OOOOOOOOO00O00OOO ,O000OO0O000O0O0OO ,OO0O0O0O000OOOO00 )#line:47
        OO00000000OO0O00O =Tools .sampleFromProbabiliity (O0000OOO0OOO00OOO ,OO0O0O0O000OOOO00 ,OO00OOOOO0OOOOOOO )#line:48
        OOOOO0OOO0O0O0O0O .append (OO00000000OO0O00O [0 ])#line:49
    return OOOOO0OOO0O0O0O0O #line:50
def perturbationOnOneLocation_patternPreserving_randomEpsilon (O0000O00OO0OOO0OO ,O00OO00OOOOOO00OO ,O0OOOO0O0OOOO00O0 ,OO00O0O0O0O0O0OOO ,OOOO0OOO0OOOO0O00 ):#line:52
    if O00OO00OOOOOO00OO !=len (OOOO0OOO0OOOO0O00 ):#line:53
        print ('Error: Epsilon_list has a wrong length.')#line:54
    O0O0OO00OO0O0O0O0 =1 #line:55
    OO0O0OO00OOOOOO0O =[[0 for OO0O0O0OO00OO0O0O in range (O0OOOO0O0OOOO00O0 )]for OO0O0OO000O00OOOO in range (O0OOOO0O0OOOO00O0 )]#line:56
    Tools .Sequencelize_Matrix (OO0O0OO00OOOOOO0O )#line:57
    O00O0OOO00O0O0O0O =[[0 for OO0O0OOO0O0OOOOO0 in range (O0OOOO0O0OOOO00O0 )]for O00OOO0O00OOOO00O in range (O0OOOO0O0OOOO00O0 )]#line:58
    OO0OO0OOOOO000OO0 =[[0 for OOOOO0OOO000OO0O0 in range (O0OOOO0O0OOOO00O0 )]for OOOO000000O0OO0OO in range (O0OOOO0O0OOOO00O0 )]#line:59
    O00OOOO00O00000OO =[[0 for OOOO0O0OO000O000O in range (O0OOOO0O0OOOO00O0 )]for O00O0O00OOOO00000 in range (O0OOOO0O0OOOO00O0 )]#line:60
    Tools .calculateDistanceMatrix_PatternPreserving (OO0O0OO00OOOOOO0O ,O00O0OOO00O0O0O0O ,O0000O00OO0OOO0OO ,O0OOOO0O0OOOO00O0 ,OO00O0O0O0O0O0OOO )#line:62
    OOOOO0OOO00O00O00 =Tools .irrationalLocationList (SNR ,O0000O00OO0OOO0OO ,OO0O0OO00OOOOOO0O )#line:63
    O000OO0O0OO0OO00O =[]#line:64
    for OOO00OO00OOOOO00O in OOOO0OOO0OOOO0O00 :#line:65
        O0O0000OOOOOOO00O =Tools .calculateWeightMatrix (OOO00OO00OOOOO00O ,O0OOOO0O0OOOO00O0 ,O00O0OOO00O0O0O0O ,OO0OO0OOOOO000OO0 )#line:66
        Tools .calculateProbabiliityMatrix (O00OOOO00O00000OO ,OO0OO0OOOOO000OO0 ,O0000O00OO0OOO0OO ,OOOOO0OOO00O00O00 ,O0O0000OOOOOOO00O ,O0OOOO0O0OOOO00O0 )#line:68
        O0OOO0OO0OO0O00OO =Tools .sampleFromProbabiliity (O00OOOO00O00000OO ,O0OOOO0O0OOOO00O0 ,O0O0OO00OO0O0O0O0 )#line:69
        O000OO0O0OO0OO00O .append (O0OOO0OO0OO0O00OO [0 ])#line:70
    return O000OO0O0OO0OO00O #line:71
def perturbationOnOneLocation_userProportion (OOOO0OOO0O0000O0O ,OO0000OO000OOO0OO ,O0OOOOOO00OOO0OO0 ,O0OO0OOOOO0O000O0 ,O0O00OOO000OOOO0O ):#line:73
    OO0O0O0O000O00O0O =[[0 for OO00OO00O000O0OOO in range (O0OOOOOO00OOO0OO0 )]for O0O00OOO000O0O000 in range (O0OOOOOO00OOO0OO0 )]#line:74
    Tools .Sequencelize_Matrix (OO0O0O0O000O00O0O )#line:75
    OO00OO00OO0OO0000 =[[0 for OO0O0O000OOO0O000 in range (O0OOOOOO00OOO0OO0 )]for OO000O0OOO000OOO0 in range (O0OOOOOO00OOO0OO0 )]#line:76
    OO0OO00OOOO00000O =[[0 for O0O000OO0O0O0OOOO in range (O0OOOOOO00OOO0OO0 )]for O0O0OOO0O00000OOO in range (O0OOOOOO00OOO0OO0 )]#line:77
    O0OOO0OOOO000O0OO =[[0 for OOOOOO0OO00O00O0O in range (O0OOOOOO00OOO0OO0 )]for OO0OO000O0OO00O00 in range (O0OOOOOO00OOO0OO0 )]#line:78
    Tools .calculateDistanceMatrix (OO0O0O0O000O00O0O ,OO00OO00OO0OO0000 ,OOOO0OOO0O0000O0O ,O0OOOOOO00OOO0OO0 )#line:79
    O0O0O0OO00O00000O =Tools .irrationalLocationList (SNR ,OOOO0OOO0O0000O0O ,OO0O0O0O000O00O0O )#line:80
    OO0O0000OO00O0O00 =[]#line:81
    if type (O0OO0OOOOO0O000O0 )==list :#line:82
        OOO0OOOOO00O00OO0 =1 #line:83
        OO0OOOOO00OO0O00O =0 #line:84
        for O00O00O00O0OOO0O0 in O0OO0OOOOO0O000O0 :#line:85
            if OO0OOOOO00OO0O00O <OO0000OO000OOO0OO *O0O00OOO000OOOO0O /100 :#line:86
                OOO0O0000000O0000 =Tools .calculateWeightMatrix (O00O00O00O0OOO0O0 ,O0OOOOOO00OOO0OO0 ,OO00OO00OO0OO0000 ,OO0OO00OOOO00000O )#line:87
                Tools .calculateProbabiliityMatrix (O0OOO0OOOO000O0OO ,OO0OO00OOOO00000O ,OOOO0OOO0O0000O0O ,O0O0O0OO00O00000O ,OOO0O0000000O0000 ,O0OOOOOO00OOO0OO0 )#line:88
                OO000OOO0O0OO0000 =Tools .sampleFromProbabiliity (O0OOO0OOOO000O0OO ,O0OOOOOO00OOO0OO0 ,OOO0OOOOO00O00OO0 )#line:89
                OO0O0000OO00O0O00 .append (OO000OOO0O0OO0000 [0 ])#line:90
            else :#line:91
                OO0O0000OO00O0O00 .append (OOOO0OOO0O0000O0O )#line:92
            OO0OOOOO00OO0O00O =OO0OOOOO00OO0O00O +1 #line:93
    else :#line:94
        O00O00O00O0OOO0O0 =O0OO0OOOOO0O000O0 #line:95
        OOO0O0000000O0000 =Tools .calculateWeightMatrix (O00O00O00O0OOO0O0 ,O0OOOOOO00OOO0OO0 ,OO00OO00OO0OO0000 ,OO0OO00OOOO00000O )#line:96
        Tools .calculateProbabiliityMatrix (O0OOO0OOOO000O0OO ,OO0OO00OOOO00000O ,OOOO0OOO0O0000O0O ,O0O0O0OO00O00000O ,OOO0O0000000O0000 ,O0OOOOOO00OOO0OO0 )#line:98
        OO000OOO0O0OO0000 =Tools .sampleFromProbabiliity (O0OOO0OOOO000O0OO ,O0OOOOOO00OOO0OO0 ,int (OO0000OO000OOO0OO *O0O00OOO000OOOO0O /100 ))#line:99
        OO0O0000OO00O0O00 .extend (OO000OOO0O0OO0000 )#line:100
        OOOO0OO00OOOO0OO0 =[OOOO0OOO0O0000O0O ]*(OO0000OO000OOO0OO -int (OO0000OO000OOO0OO *O0O00OOO000OOOO0O /100 ))#line:101
        OO0O0000OO00O0O00 .extend (OOOO0OO00OOOO0OO0 )#line:102
    return OO0O0000OO00O0O00 #line:103
def perturbationOnOneLocation_patternPreserving_userProportion (OO00O00O0OO000OOO ,O000O0O00O0000OO0 ,O00O0OOO0OOOO000O ,OO0000000O000OOOO ,O0O000OO00OOO0O00 ,O00O00O0OOOO000O0 ):#line:106
    OO000O0OO0O00O00O =[[0 for OO0OO0O0000000OO0 in range (O00O0OOO0OOOO000O )]for O0O0O0OO00O00OOO0 in range (O00O0OOO0OOOO000O )]#line:107
    Tools .Sequencelize_Matrix (OO000O0OO0O00O00O )#line:108
    OOOO00OO000OOOO00 =[[0 for OOO000OOO0000OOOO in range (O00O0OOO0OOOO000O )]for OO0OO00OOO0O0000O in range (O00O0OOO0OOOO000O )]#line:109
    OOOOOOO0000OO0OO0 =[[0 for O00000O0O0O00O00O in range (O00O0OOO0OOOO000O )]for OOO00O0O000O0OO00 in range (O00O0OOO0OOOO000O )]#line:110
    O0O0OO00O00OO0000 =[[0 for O00OO0OOOOOOOOOOO in range (O00O0OOO0OOOO000O )]for OO00OOO0OO0O0OO00 in range (O00O0OOO0OOOO000O )]#line:111
    Tools .calculateDistanceMatrix_PatternPreserving (OO000O0OO0O00O00O ,OOOO00OO000OOOO00 ,OO00O00O0OO000OOO ,O00O0OOO0OOOO000O ,OO0000000O000OOOO )#line:113
    OOOOO0O0000000O00 =Tools .irrationalLocationList (SNR ,OO00O00O0OO000OOO ,OO000O0OO0O00O00O )#line:114
    OOOOO00OOOOOOO0O0 =[]#line:115
    if type (O0O000OO00OOO0O00 )==list :#line:116
        O00O0O00OO00OO0OO =1 #line:117
        O00O000OOO0OO0000 =0 #line:118
        for O0O0O00OOO00OO000 in O0O000OO00OOO0O00 :#line:119
            if O00O000OOO0OO0000 <O000O0O00O0000OO0 *O00O00O0OOOO000O0 /100 :#line:120
                O0OO00O0OO0OOOO0O =Tools .calculateWeightMatrix (O0O0O00OOO00OO000 ,O00O0OOO0OOOO000O ,OOOO00OO000OOOO00 ,OOOOOOO0000OO0OO0 )#line:121
                Tools .calculateProbabiliityMatrix (O0O0OO00O00OO0000 ,OOOOOOO0000OO0OO0 ,OO00O00O0OO000OOO ,OOOOO0O0000000O00 ,O0OO00O0OO0OOOO0O ,O00O0OOO0OOOO000O )#line:123
                O0OOO00O000O0O0O0 =Tools .sampleFromProbabiliity (O0O0OO00O00OO0000 ,O00O0OOO0OOOO000O ,O00O0O00OO00OO0OO )#line:124
                OOOOO00OOOOOOO0O0 .append (O0OOO00O000O0O0O0 [0 ])#line:125
            else :#line:126
                OOOOO00OOOOOOO0O0 .append (OO00O00O0OO000OOO )#line:127
            O00O000OOO0OO0000 =O00O000OOO0OO0000 +1 #line:128
    else :#line:129
        O0O0O00OOO00OO000 =O0O000OO00OOO0O00 #line:130
        O0OO00O0OO0OOOO0O =Tools .calculateWeightMatrix (O0O0O00OOO00OO000 ,O00O0OOO0OOOO000O ,OOOO00OO000OOOO00 ,OOOOOOO0000OO0OO0 )#line:131
        Tools .calculateProbabiliityMatrix (O0O0OO00O00OO0000 ,OOOOOOO0000OO0OO0 ,OO00O00O0OO000OOO ,OOOOO0O0000000O00 ,O0OO00O0OO0OOOO0O ,O00O0OOO0OOOO000O )#line:134
        O0OOO00O000O0O0O0 =Tools .sampleFromProbabiliity (O0O0OO00O00OO0000 ,O00O0OOO0OOOO000O ,int (O000O0O00O0000OO0 *O00O00O0OOOO000O0 /100 ))#line:135
        OOOOO00OOOOOOO0O0 .extend (O0OOO00O000O0O0O0 )#line:136
        O00OOOOO0O0OOO0O0 =[OO00O00O0OO000OOO ]*(O000O0O00O0000OO0 -int (O000O0O00O0000OO0 *O00O00O0OOOO000O0 /100 ))#line:137
        OOOOO00OOOOOOO0O0 .extend (O00OOOOO0O0OOO0O0 )#line:138
    return OOOOO00OOOOOOO0O0 #line:139
def KL_divergence (OOO000OO000000OOO ,O0OO0O0O0000000OO ):#line:141
    O000O00O000000O0O =0 #line:142
    for OO0O00O0O00O0O000 in range (len (OOO000OO000000OOO )):#line:143
        if OOO000OO000000OOO [OO0O00O0O00O0O000 ]==0 :#line:144
            OOO000OO000000OOO [OO0O00O0O00O0O000 ]=np .mean (OOO000OO000000OOO )/100 #line:145
        if O0OO0O0O0000000OO [OO0O00O0O00O0O000 ]==0 :#line:146
            O0OO0O0O0000000OO [OO0O00O0O00O0O000 ]=np .mean (O0OO0O0O0000000OO )/100 #line:147
        O000O00O000000O0O +=OOO000OO000000OOO [OO0O00O0O00O0O000 ]*math .log (OOO000OO000000OOO [OO0O00O0O00O0O000 ]/O0OO0O0O0000000OO [OO0O00O0O00O0O000 ])#line:148
    return O000O00O000000O0O #line:149
def JS_divergence (O00OO0OOOOOOO00OO ,OO00O00O0O0O00OOO ):#line:151
    O000OO0OOO0OO0000 =[0 for O00000OOOOOO00O0O in range (len (O00OO0OOOOOOO00OO ))]#line:152
    for O0O000OO00OOOOOO0 in range (len (O00OO0OOOOOOO00OO )):#line:153
        O000OO0OOO0OO0000 [O0O000OO00OOOOOO0 ]=(O00OO0OOOOOOO00OO [O0O000OO00OOOOOO0 ]+OO00O00O0O0O00OOO [O0O000OO00OOOOOO0 ])/2 #line:154
    O00OOOOO0000OOO00 =0.5 *KL_divergence (O00OO0OOOOOOO00OO ,O000OO0OOO0OO0000 )+0.5 *KL_divergence (OO00O00O0O0O00OOO ,O000OO0OOO0OO0000 )#line:155
    return O00OOOOO0000OOO00