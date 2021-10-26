# from matplotlib import pyplot as plt ### Not used
from statsmodels.tsa.stattools import grangercausalitytests as gct
import plotly.graph_objects as go
import plotly.express as px
import Methods

import numpy as np
import plotly
import mne # Multitaper spectrums
import cv2


def coherence_pearson(x, y):

    c = np.corrcoef(x, y)
    return c[0, 1]


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


def coherence_plotter(data=None, key='pfc', save=False,
                t1=500, t2=2501, fmin=0, fmax=100,
                normalize_w=False, k=5,
                title="Spectral coherence multitaper ",
                bw=15, trials=None):
    
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
    
    ps_pfc = Methods.pspectlamavg(Y, axis=0, fs=1000, fc=150, fmin=fmin, fmax=fmax)
    
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
    
    c = spectral_coherence(psd=ps_pfc.transpose())
    t = np.linspace(1, 17, 16)
    y = np.linspace(1, 17, 16)
    Methods.customplot(c, save=True, show=True, filename="specCoherence.html"
                   , w=16, h=16, t=t, y=y, relative=True
                   ,xlabel="Ch ID", ylabel="Ch ID",
                   title=title, reverse=False)
    return


def spectral_coherence(psd=None):
    
    # print(psd.shape)
    c = np.zeros((psd.shape[0], psd.shape[0]))
    for i in range(psd.shape[0]):
        c[i, i] = 1
        for j in range(i+1, psd.shape[0]):
            u = coherence_pearson(psd[i, :], psd[j, :])
            c[i, j] = u
            c[j, i] = u
            
    return c


def granger_coherence(sig=None, lag=4):
    
    # print(psd.shape)
    c = np.zeros((sig.shape[0], sig.shape[0]))
    for i in range(sig.shape[0]):
        for j in range(sig.shape[0]):
            u = coherence_granger(sig[i, :], sig[j, :], lag=lag)
            c[i, j] = u
            
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
        
    print("Granger test started ...")
    c = granger_cohernece(psd=ps_pfc.transpose())
            
    print("Granger p_values calculation done.")
    t = np.linspace(1, 17, 16)
    y = np.linspace(1, 17, 16)
    
    Methods.customplot(c, save=save, show=True, filename="specCoherence" + str(trials[0]) + ".html"
                   , w=16, h=16, t=t, y=y, relative=False
                   ,xlabel="Ch ID", ylabel="Ch ID",
                   title=title, reverse=False)
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

    for t in range(len(trials)):
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
           
        try:
            c += granger_coherence(psd=ps_pfc.transpose())
        except:
            c = granger_coherence(psd=ps_pfc.transpose())
            
    print("Granger p_values calculation done.")
    t = np.linspace(1, 17, 16)
    y = np.linspace(1, 17, 16)
    c /= len(t)
    
    Methods.customplot(c, save=save, show=True, filename="specCoherence" + str(trials[0]) + ".html"
                   , w=16, h=16, t=t, y=y, relative=False
                   ,xlabel="Ch ID", ylabel="Ch ID",
                   title=title, reverse=True)
    return


def time_power_spectrum_density(data=None, key='key', save=True
                                , time_window_size=500, time_overlap=100
                                , trials=None, bw=40, tl=0, tr=4500, time_base=0):
    
    '''
        => To calculate the psd in each time window, in order to check time dependent variations
    '''
    
    tq = time_window_size-time_overlap
    ts = [i for i in range(tl, tr-tq, tq)]
    tpsd = []
    
    for t in ts:
        
        
        psd, freqs = Methods.power_spectrum_density(data=data, key='pfc', save=True
                                            , t1=t, t2=t+time_window_size
                                            , fmin=0, fmax=100, normalize_w=False
                                            , bw=bw, k=0, trials=trials)
        
        tpsd.append(psd)
    
    ts.append(ts[len(ts)-1] + time_window_size)
    for t in range(len(ts)):
        ts[t] += time_base
        
    return np.array(tpsd), freqs, ts


def time_spectral_coherence(data=None, key='key', save=True, trials=None, ts=None):
    
    tsc = np.zeros([data.shape[0], data.shape[1], data.shape[1], data.shape[3]])
    
    for t in range(len(trials)):
        
        for i in range(len(ts)-1):
            
            
            tsc[i, :, :, t] = spectral_coherence(psd=data[i, :, :, t])
            
    
    return tsc


def time_granger_causality(data=None, key='key', time_window_size=500, time_overlap=100
                                , trials=None, bw=40, tl=0, tr=4500, time_base=0):
    
    if key=='pfc':
        lam = data['lfp'][:, 0:16, trials]
    elif key=='p7a':
        lam = data['lfp'][:, 16:32, trials]
    elif key=='v4':
        lam = data['lfp'][:, 32:48, trials]
    else:
        print('Not in set')
        return
    
    tq = time_window_size-time_overlap
    ts = [i for i in range(tl, tr-tq, tq)]
    tgc = np.zeros([len(ts), lam.shape[1], lam.shape[1], len(trials)])
    print("Dynamic granger started, it will take a while. log of progress will be printed.")
    for i in range(len(trials)):
        
        print("Trial no. ", trials[i])
        sig = lam[:, :, i].transpose()
        for t in range(len(ts)):
            
            print("Cal. for t = ", ts[t])
            tgc[t, :, :, i] = granger_coherence(sig=sig[:, ts[t]:ts[t]+time_window_size]
                                                , lag=7)
                
    
    return tsc
