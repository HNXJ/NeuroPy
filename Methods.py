# from matplotlib import pyplot as plt ### Not used

import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import plotly
import cv2


def print_all_content(data=None):
    
    for v in data.keys():
        try:
            print("Value: ", v, " || Size: ", data[v].shape)
        except:
            print("Value: ", v)


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


def pspectlam(x, axis=0, fs=1000, fc=500):
    x = x - np.mean(np.mean(x))
    _fft = np.fft.fft(x, axis=axis)
    k = fs/fc
    n = np.int(np.ceil(_fft.shape[axis]/k))
    return _fft[:n, :, :]


def pspectlamavg(x, axis=0, fs=1000, fc=1000):
    xf = pspectlam(x, axis=axis, fs=fs, fc=fc)
    return np.abs(np.mean(xf, 2))


def psplot(x, save=True, show=True, filename="psp.html", w=300, h=200, t=None, y=None, relative=True):

    im = x.transpose()
    if relative==True:
        im = im / np.max(np.max(im))
        
    im = cv2.resize(im, (w, h))
    fig = go.Figure(
        data=go.Heatmap(z=im, y=y, x=t), 
        layout=go.Layout(
            title="Power spectrum/ ",
            xaxis=dict(title='Frequency(Hz)'),
            yaxis=dict(title='Channel ID')
        ),
    )

    if save==True:
        plotly.offline.plot(fig, filename=filename)
    
    if show==True:
        fig.show()
    
    return


def customplot(x, save=True, show=True, filename="plot.html"
               , w=300, h=200, t=None, y=None, relative=True
               ,xlabel="T", ylabel="A", title="Plot"):

    im = x.transpose()
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

    if save==True:
        plotly.offline.plot(fig, filename=filename)
    
    if show==True:
        fig.show()
    
    return


def psp_plotter(data=None, key='pfc', save=False):
    
    lam1 = data['lfp'][:, 0:16, :]
    lam2 = data['lfp'][:, 16:32, :]
    lam3 = data['lfp'][:, 32:48, :]
    
    if key=='pfc':
        Y = lam1[500:2501, :, :]
    elif key=='p7a':
        Y = lam2[500:2501, :, :]
    elif key=='v4':
        Y = lam3[500:2501, :, :]
    else:
        print('Not in set')
        return
    
    ps_pfc = pspectlamavg(Y, axis=0, fs=1000, fc=150)
    
    t = np.linspace(0, 150, 1000)
    y = np.linspace(1, 16, 300)
        
    psplot(ps_pfc, save=save, filename="ps_" + key + ".html", w=1000, h=300, t=t, y=y, relative=True)
    
    

    
    
    