import numpy as np
import math

# reset the starting point t after discarding burn-in period to zero
def burn_in_array(t, I):
    t_burn = t[int(len(t)/2):-1]-t[int(len(t)/2)]
    I_burn = I[int(len(t)/2):-1]
    return t_burn, I_burn

def thinning(t, I, thin_step):
    t_thin = []
    I_thin = []
    for i in range(len(t)):
        if i % thin_step == 0:
            t_thin.append(t[i])
            I_thin.append(I[i])
    return t_thin, I_thin

# def thinning_int(t, I):
#     if t[-1] % 1 == 0:
#         t_thin_int = np.arange( t[-1]+1 )
#     else:
#         t_thin_int = np.arange( math.ceil(t[-1]) )
#
#     if len(t) > len(t_thin_int):
#         t_temp = t
#         I = I
#     elif len(t) < len(t_thin_int):
#         t_temp = np.append(t, np.ones(len(t_thin_int)-len(t) )*t[-1])
#         I = np.append(I, np.ones(len(t_thin_int)-len(t) )*I[-1] )
#
#     I_thin_arr = np.zeros(len(t_temp))
#     I_thin_arr[0] = I[0]
#
#     for i in np.arange(1, len(t_temp) ):
#         while True:
#             k = 0
#             if i > t_temp[i]:
#                 while i > t_temp[i+k] and i+k < len(t_temp)-1:
#                     k += 1
#                 else:
#                     I_thin_arr[i] = I[i+k-1]
#                     break
#             elif i < t_temp[i]:
#                 while i < t_temp[i-k]:
#                     k += 1
#                 else:
#                     I_thin_arr[i] = I[i-k]
#                     break
#     return t_thin_int, I_thin_arr[0:len(t_thin_int)]

def thinning_int(t, I):
    if t[-1] % 1 == 0:
        t_thin_int = np.arange( t[-1]+1 )
    else:
        t_thin_int = np.arange( math.ceil(t[-1]) )

    I_thin_arr = np.zeros(len(t_thin_int))
    I_thin_arr[0] = I[0]

    if len(I_thin_arr) > len(t):
        t_modify = np.append(t, np.ones( len(I_thin_arr)-len(t) )*t[-1] )
    else:
        t_modify = t_thin_int

    for i in np.arange(1, len(t_modify)):
        k = 0
        while k < len(t_modify):
            if t_thin_int[i] >= t_modify[i-k]:
                I_thin_arr[i] = I[i-k]
                break
            k += 1
    return t_thin_int, I_thin_arr

def time_interval_avg(t):
    return t[-1]/(len(t)-1)

def t_I_complement(t, I, Tmax):
    if abs(Tmax - t[-1]) > 1:
        while Tmax - ( t[-1] + time_interval_avg(t) ) > 0.1:
            t = np.append(t, t[-1] + time_interval_avg(t) )
            I = np.append(I, I[-1])
    return t, I