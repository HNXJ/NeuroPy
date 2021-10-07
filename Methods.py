# from matplotlib import pyplot as plt ### Not used

import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import plotly
import mne # Multitaper spectrums
import cv2


def print_all_content(data=None):
    
    for v in data.keys():
        try:
            print("Value: ", v, " || Size: ", data[v].shape)
        except:
            print("Value: ", v)

    return


def ERP_plot(save=False, data=None, key="pfc"):
    
    if key=='pfc':
        lam = np.mean(data['lfp'][:, 0:16, :], 2)
    elif key=='p7a':
        lam = np.mean(data['lfp'][:, 16:32, :], 2)
    elif key=='v4':
        lam = np.mean(data['lfp'][:, 32:48, :], 2)
    else:
        print('Not in set')
        return
    
    lam = lam.transpose()
    lam = cv2.resize(lam, (900, 300))
    t = np.linspace(-1500, 3000, 900)
    y = np.linspace(1, 16, 300)
    
    fig = go.Figure(
        data=go.Heatmap(z=lam, y=y, x=t), 
        layout=go.Layout(
            title="ERP heatmap (" + key + ")",
            xaxis=dict(title='Time(ms)'),
            yaxis=dict(title='Channel ID')
        ),
    )
    
    if save==True:
        plotly.offline.plot(fig, filename="ERP_" + key + ".html")

    fig.show()
    return


def CSD_plot(save=False, data=None, key='pfc'):
    
    lam1 = data['lfp'][:, 0:16, :]
    lam2 = data['lfp'][:, 16:32, :]
    lam3 = data['lfp'][:, 32:48, :]
    
    sig = 2*(10**-4)
    es = 0.4
    
    csd1 = sig*(lam1[:, 0:14, :] - 2*lam1[:, 1:15, :] +lam1[:, 2:16, :])/(2*(es**2))
    csd2 = sig*(lam2[:, 0:14, :] - 2*lam2[:, 1:15, :] +lam2[:, 2:16, :])/(2*(es**2))
    csd3 = sig*(lam3[:, 0:14, :] - 2*lam3[:, 1:15, :] +lam3[:, 2:16, :])/(2*(es**2))
    
    acsd1 = np.mean(csd1, 2)
    acsd2 = np.mean(csd2, 2)
    acsd3 = np.mean(csd3, 2)

    if key=='pfc':
        acsd1 = acsd1.transpose()
    elif key=='p7a':
        acsd1 = acsd2.transpose()
    elif key=='v4':
        acsd1 = acsd3.transpose()
    else:
        print('Not in set')
        return
    
    acsd1 = cv2.resize(acsd1, (900, 300))
    t = np.linspace(-1500, 3000, 900)
    y = np.linspace(3, 13, 300)
    
    fig = go.Figure(
        data=go.Heatmap(z=acsd1, y=y, x=t), 
        layout=go.Layout(
            title="Average CSD heatmap (" + key + ")",
            xaxis=dict(title='Time(ms)'),
            yaxis=dict(title='Channel ID')
        ),
    )
    
    if save==True:
        plotly.offline.plot(fig, filename="ACSD_" + key + ".html")
        
    fig.show()


def pspectlam(x, axis=0, fs=1000, fc=500, mode="MT", fmin=0, fmax=100, bw=15):
    if mode=="MT":
        
        ch_names = [str(i) for i in range(1, 17)]
        info = mne.create_info(ch_names=ch_names, sfreq=1000)
        d = x
        
        if len(d.shape) < 3:
            raw = mne.io.RawArray(d, info, first_samp=0, copy='auto', verbose=None)
        else:
            raw = mne.EpochsArray(d, info, verbose=None)
            
        
        # bw = 7
        f = mne.time_frequency.psd_multitaper(raw, fmin=fmin, fmax=fmax, tmin=None, tmax=None,
                                          bandwidth=bw, adaptive=False, low_bias=True,
                                          normalization='length', picks=ch_names, proj=False,
                                          n_jobs=1, verbose=None)
        return f[0]
    
    x = x - np.mean(np.mean(x))
    _fft = np.fft.fft(x, axis=axis)
    k = fs/fc
    n = np.int(np.ceil(_fft.shape[axis]/k))
    return _fft[:n, :, :]


def pspectlamavg(x, axis=0, fs=1000, fc=1000, fmin=0, fmax=100, bw=15):
    x = np.mean(x, 2)
    xf = pspectlam(x.transpose(), axis=axis, fs=fs, fc=fc, fmin=fmin, fmax=fmax, bw=bw)
    return xf.transpose()


def psplot(x, save=True, show=True, filename="psp.html", w=300, h=200, t=None,
           y=None, relative=True, reverse=True, title="PowerSpectrum"):

    im = x.transpose()
    if relative==True:
        im = im / np.max(np.max(im))
        
    im = cv2.resize(im, (w, h))
    fig = go.Figure(
        data=go.Heatmap(z=im, y=y, x=t), 
        layout=go.Layout(
            title=title,
            xaxis=dict(title='Frequency(Hz)'),
            yaxis=dict(title='Channel ID')
        ),
    )
    
    if reverse==True: 
        fig.update_layout(
            yaxis = dict(autorange="reversed")
        )
        
    if save==True:
        plotly.offline.plot(fig, filename=filename)
    
    if show==True:
        fig.show()
    
    return


def customplot(x, save=True, show=True, filename="plot.html"
               , w=300, h=200, t=None, y=None, relative=True
               ,xlabel="T", ylabel="A", title="Plot", reverse=None):

    im = x.transpose()
    print(im.shape)
    if relative==True:
        im = im / np.max(np.max(im))
        
    im = cv2.resize(im, (w, h))
    fig = go.Figure(
        data=go.Heatmap(z=im, y=y, x=t), 
        layout=go.Layout(
            title=title,
            xaxis=dict(title=xlabel),
            yaxis=dict(title=ylabel)
        ),
    )

    if reverse==True: 
        fig.update_layout(
            yaxis = dict(autorange="reversed")
        )

    if save==True:
        plotly.offline.plot(fig, filename=filename)
    
    if show==True:
        fig.show()
    
    return


def psp_plotter(data=None, key='pfc', save=False,
                t1=500, t2=2501, fmin=0, fmax=100,
                normalize_w=False, k=5,
                title="Power spectrum multitaper ",
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
    
    ps_pfc = pspectlamavg(Y, axis=0, fs=1000, fc=150, fmin=fmin, fmax=fmax)
    
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
        
    psplot(ps_pfc, save=save, filename="ps_" + key + ".html", w=1000, h=300,
           t=t, y=y, relative=True, title=title)
    return
    

def coherence_pearson(x, y):

    c = np.corrcoef(x, y)
    return c[0, 1]


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
    
    ps_pfc = pspectlamavg(Y, axis=0, fs=1000, fc=150, fmin=fmin, fmax=fmax)
    
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
    
    c = np.zeros((ps_pfc.shape[1], ps_pfc.shape[1]))
    for i in range(ps_pfc.shape[1]):
        c[i, i] = 1
        for j in range(i+1, ps_pfc.shape[1]):
            u = coherence_pearson(ps_pfc[:, i], ps_pfc[:, j])
            c[i, j] = u
            c[j, i] = u
            
    t = np.linspace(1, 17, 16)
    y = np.linspace(1, 17, 16)
    customplot(c, save=True, show=True, filename="specCoherence.html"
                   , w=16, h=16, t=t, y=y, relative=True
                   ,xlabel="Ch ID", ylabel="Ch ID",
                   title=title)
    return


def coherence_granger(x, y): # Incomplete

    c = np.corrcoef(x, y)
    return c[0, 1]


def granger_plotter(data=None, key='pfc', save=False,
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
    
    ps_pfc = pspectlamavg(Y, axis=0, fs=1000, fc=150, fmin=fmin, fmax=fmax)
    
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
    
    c = np.zeros((ps_pfc.shape[1], ps_pfc.shape[1]))
    for i in range(ps_pfc.shape[1]):
        c[i, i] = 1
        for j in range(i+1, ps_pfc.shape[1]):
            u = coherence_granger(ps_pfc[:, i], ps_pfc[:, j])
            c[i, j] = u
            c[j, i] = u
            
    t = np.linspace(1, 17, 16)
    y = np.linspace(1, 17, 16)
    customplot(c, save=True, show=True, filename="specCoherence.html"
                   , w=16, h=16, t=t, y=y, relative=True
                   ,xlabel="Ch ID", ylabel="Ch ID",
                   title=title)
    return