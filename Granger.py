# from matplotlib import pyplot as plt ### Not used
from statsmodels.tsa.stattools import grangercausalitytests as gct
import plotly.graph_objects as go
import plotly.express as px
from Methods import *

import numpy as np
import plotly
import mne # Multitaper spectrums
import cv2


def coherence_granger(x, y, lag=2, test='lrtest'): # Incomplete

    d = np.array((x, y)).transpose()
    gc = gct(d, lag, verbose=False)
    c = 0
    
    p_values = [round(gc[i+1][0][test][1], 12) for i in range(lag)]
    # print(f'P Values = {p_values}')

    c = np.max(p_values)       
    # if c > 0.2:
    #     return -0.2
    return c


def granger_plotter(data=None, key='pfc', save=False,
                t1=500, t2=2501, fmin=0, fmax=100,
                normalize_w=False, k=5,
                title="Spectral coherence multitaper ",
                bw=15, trials=None, lag=2):
    
    if trials==None:
        trials = [i for i in range(data['lfp'].shape[2])]
    
    lam1 = data['lfp'][:, 0:16, trials]
    lam2 = data['lfp'][:, 16:32, trials]
    lam3 = data['lfp'][:, 32:48, trials]
    
    if key=='pfc':
        Y = lam1[t1:t2, :, :]
    elif key=='p7a':
        Y = lam2[t1:t2, :, :]
    elif key=='v4':
        Y = lam3[t1:t2, :, :]
    else:
        print('Not in set')
        return
    
    # ps_pfc = pspectlamavg(Y, axis=0, fs=1000, fc=150, fmin=fmin, fmax=fmax)
    Ym = np.mean(Y, 2)
    ps_pfc = Ym
    # print(ps_pfc.shape, Ym.shape)
    
    if normalize_w==True:
        for i in range(ps_pfc.shape[0]-k):
            if k > 0:
                ps_pfc[i, :] /= np.max(np.max(ps_pfc[i:i+k, :]))
            else:
                ps_pfc[i, :] /= np.max(np.max(ps_pfc[i, :]))
        if k > 0:
            for i in range(ps_pfc.shape[0]-k, ps_pfc.shape[0]):
                ps_pfc[i, :] /= np.max(np.max(ps_pfc[i, :]))
        
        title = title + ",Normalized relative to other channels"
        
    t = np.linspace(fmin, fmax, 1000)
    y = np.linspace(1, 16, 300)
    print("Granger test started ...")
    c = np.zeros((ps_pfc.shape[1], ps_pfc.shape[1]))
    
    for i in range(ps_pfc.shape[1]):
        c[i, i] = -0.1
        for j in range(ps_pfc.shape[1]):
            if i==j:
                continue
            u = coherence_granger(ps_pfc[:, i], ps_pfc[:, j], lag=lag)
            c[i, j] = u
            # c[j, i] = u
            
    print("Granger p_values calculation done.")
    t = np.linspace(1, 17, 16)
    y = np.linspace(1, 17, 16)
    
    customplot(c, save=save, show=True, filename="specCoherence" + str(trials[0]) + ".html"
                   , w=16, h=16, t=t, y=y, relative=False
                   ,xlabel="Ch ID", ylabel="Ch ID",
                   title=title, reverse=True)
    return


def s_granger_plotter(data=None, key='pfc', save=False,
                t1=500, t2=2501, fmin=0, fmax=100,
                normalize_w=False, k=5,
                title="Spectral coherence multitaper ",
                bw=15, trials=None, lag=2):
    
    if trials==None:
        trials = [i for i in range(data['lfp'].shape[2])]
    
    lam1 = data['lfp'][:, 0:16, trials]
    lam2 = data['lfp'][:, 16:32, trials]
    lam3 = data['lfp'][:, 32:48, trials]
    
    if key=='pfc':
        Y = lam1[t1:t2, :, :]
    elif key=='p7a':
        Y = lam2[t1:t2, :, :]
    elif key=='v4':
        Y = lam3[t1:t2, :, :]
    else:
        print('Not in set')
        return
    
    # ps_pfc = pspectlamavg(Y, axis=0, fs=1000, fc=150, fmin=fmin, fmax=fmax)
    c = np.zeros((16, 16))
    print("Granger test started ...")

    for t in trials:
        print('Trials no.', t)
        Ym = Y[:, :, t]
        ps_pfc = Ym
        # print(ps_pfc.shape, Ym.shape)
        
        if normalize_w==True:
            for i in range(ps_pfc.shape[0]-k):
                if k > 0:
                    ps_pfc[i, :] /= np.max(np.max(ps_pfc[i:i+k, :]))
                else:
                    ps_pfc[i, :] /= np.max(np.max(ps_pfc[i, :]))
            if k > 0:
                for i in range(ps_pfc.shape[0]-k, ps_pfc.shape[0]):
                    ps_pfc[i, :] /= np.max(np.max(ps_pfc[i, :]))
            
            title = title + ",Normalized relative to other channels"
            
        t = np.linspace(fmin, fmax, 1000)
        y = np.linspace(1, 16, 300)
        for i in range(ps_pfc.shape[1]):
            c[i, i] += -0.1
            for j in range(ps_pfc.shape[1]):
                if i==j:
                    continue
                u = coherence_granger(ps_pfc[:, i], ps_pfc[:, j], lag=lag)
                c[i, j] += u
                # c[j, i] += u
            
    print("Granger p_values calculation done.")
    t = np.linspace(1, 17, 16)
    y = np.linspace(1, 17, 16)
    c /= len(t)
    
    customplot(c, save=save, show=True, filename="specCoherence" + str(trials[0]) + ".html"
                   , w=16, h=16, t=t, y=y, relative=False
                   ,xlabel="Ch ID", ylabel="Ch ID",
                   title=title, reverse=True)
    return

