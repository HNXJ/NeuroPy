import plotly.graph_objects as go
import numpy as np

import plotly
import mne # Multitaper spectrums
import cv2

import pickle


def save_list(l, filename="List0.txt"):
        
    with open(filename, "wb") as f_temp:
        pickle.dump(l, f_temp)
    
    print("Saved.")
    return


def load_list(filename="List0.txt"):
    
    with open(filename, "rb") as f_temp:
        l = pickle.load(f_temp)
    
    print("Loaded.")
    return l

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
        plotly.offline.plot(fig, filename="Files/ERP_" + key + ".html")

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
        plotly.offline.plot(fig, filename="Files/ACSD_" + key + ".html")
        
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
                                          n_jobs=1, verbose=False)
        return f[0], f[1]
    
    x = x - np.mean(np.mean(x))
    _fft = np.fft.fft(x, axis=axis)
    k = fs/fc
    n = np.int(np.ceil(_fft.shape[axis]/k))
    return _fft[:n, :, :]


def pspectlamavg(x, axis=0, fs=1000, fc=1000, fmin=0, fmax=100, bw=15):
    x = np.mean(x, 2)
    xf, _ = pspectlam(x.transpose(), axis=axis, fs=fs, fc=fc, fmin=fmin, fmax=fmax, bw=bw)
    return xf.transpose()


def pspectlamnorm(x, axis=0, fs=1000, fc=1000, fmin=0, fmax=100, bw=15):
    _t, _ = pspectlam(x[:, :, 0].transpose(), axis=axis, fs=fs,
                                fc=fc, fmin=fmin, fmax=fmax, bw=bw)
    xf = np.zeros((x.shape[1], _t.shape[1], x.shape[2]))
    for i in range(x.shape[2]):
        xf[:, :, i], f = pspectlam(x[:, :, i].transpose(), axis=axis, fs=fs,
                                fc=fc, fmin=fmin, fmax=fmax, bw=bw)
    return xf, f


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
        plotly.offline.plot(fig, filename="Files/" + filename)
    
    if show==True:
        fig.show()
    
    return


def customplot(x, save=True, show=True, filename="plot.html"
               , w=300, h=200, t=None, y=None, relative=True
               ,xlabel="T", ylabel="A", title="Plot", reverse=None
               ,xtext=False, xtext_labels=[]):
    
    print("Plotting, preprocessing ...")
    im = x.transpose()
    if relative==True:
        im = im / np.max(np.max(im))
       
    if xtext==True:
        
        im = cv2.resize(im, (w, h))
        fig = go.Figure(
            data=go.Heatmap(z=im, y=y, x=xtext_labels), 
            layout=go.Layout(
                title=title,
                xaxis=dict(title=xlabel),
                yaxis=dict(title=ylabel)
            ),
        )
    
    else:
        
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
        plotly.offline.plot(fig, filename="Files/" + filename)
    
    if show==True:
        fig.show()
    
    print("Done.")
    return


def psp_plotter(data=None, key='pfc', save=False,
                t1=500, t2=2501, fmin=0, fmax=100,
                normalize_w=False, k=5,
                title="Power spectrum multitaper ",
                bw=15, trials=None, pink_noise_filter=True):
    
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
    
    if pink_noise_filter==True:
        for i in range(ps_pfc.shape[0]):
            ps_pfc[i, :] = pink_noise_inverse_filter(x=ps_pfc[i, :], w=7)
    
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
    

def power_spectrum_density(data=None, key='pfc', save=False,
                t1=500, t2=2501, fmin=0, fmax=100,
                normalize_w=False, k=5,
                bw=15, trials=None, pink_noise_filter=True):
    
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
    
    ps_pfc, f = pspectlamnorm(Y, axis=0, fs=1000, fc=150, fmin=fmin, fmax=fmax)
    piv = np.mean(ps_pfc, 0)
    piv = np.mean(piv, 1)
    
    if pink_noise_filter==True:
        for i in range(ps_pfc.shape[0]):
            for t in range(len(trials)):
                ps_pfc[i, :, t] = pink_noise_inverse_filter(x=ps_pfc[i, :, t], w=15, piv=piv)
    
    if normalize_w==True:
        for i in range(ps_pfc.shape[0]-k):
            if k > 0:
                ps_pfc[i, :] /= np.max(np.max(ps_pfc[i:i+k, :]))
            else:
                ps_pfc[i, :] /= np.max(np.max(ps_pfc[i, :]))
        if k > 0:
            for i in range(ps_pfc.shape[0]-k, ps_pfc.shape[0]):
                ps_pfc[i, :] /= np.max(np.max(ps_pfc[i, :]))
        
    return ps_pfc, f


def psd_ratio_plotter(psd=None, freqs=None, title="P. 1"):
    
    bandlabels = ["Delta[0.1-3]", "Theta[3-8]", "Alpha[8-12]"
                  , "L-Beta[12-16]", "M-Beta[16-20]", "U-Beta[20-30]"
                  , "L-Gamma[30-50]", "M-Gamma[50-70]", "U-Gamma[70+]"]
    
    if psd.shape[1] > 9:
        c = psd_ratio_matrix(psd=psd, freqs=freqs)
    else:
        c = psd
        
    customplot(c, save=True, show=True, filename= title +".html"
                   , w=9, h=16, t=np.arange(9), y=np.ones(16)*16-np.arange(16), relative=True
                   ,xlabel="Band", ylabel="Ch", title=title, reverse=True
                   ,xtext=True, xtext_labels=bandlabels)
    return


def psd_ratio_compare_plotter(psd1=None, psd2=None, freqs=None, title="P. 1"):
    
    bandlabels = ["Delta[0.1-3]", "Theta[3-8]", "Alpha[8-12]"
                  , "L-Beta[12-16]", "M-Beta[16-20]", "U-Beta[20-30]"
                  , "L-Gamma[30-50]", "M-Gamma[50-70]", "U-Gamma[70+]"]
    
    if psd1.shape[1] > 9:
        c1 = psd_ratio_matrix(psd=psd1, freqs=freqs)
        c2 = psd_ratio_matrix(psd=psd2, freqs=freqs)
    else:
        c1 = psd1
        c2 = psd2
        
    customplot(c1/c2, save=True, show=True, filename= title +".html"
                   , w=9, h=16, t=np.arange(9), y=np.ones(16)*16-np.arange(16), relative=True
                   ,xlabel="Band", ylabel="Ch", title=title, reverse=True
                   ,xtext=True, xtext_labels=bandlabels)
    return


def psd_ratio_matrix(psd=None, freqs=None):
    
    c = np.zeros((16, 9))
    d = np.zeros((9))
    
    for i in range(freqs.shape[0]):
        
        if freqs[i] < 3.0: # Delta
            c[:, 0] += psd[:, i]
            d[0] += 1
        
        elif freqs[i] < 8.0: # Theta
            c[:, 1] += psd[:, i]
            d[1] += 1
        
        elif freqs[i] < 12.0: # Alpha
            c[:, 2] += psd[:, i]
            d[2] += 1
        
        elif freqs[i] < 16.0: # L-Beta
            c[:, 3] += psd[:, i]
            d[3] += 1
        
        elif freqs[i] < 20.0: # M-Beta
            c[:, 4] += psd[:, i]
            d[4] += 1
        
        elif freqs[i] < 30.0: # U-Beta
            c[:, 5] += psd[:, i]
            d[5] += 1
        
        elif freqs[i] < 50.0: # L-Gamma
            c[:, 6] += psd[:, i]
            d[6] += 1
        
        elif freqs[i] < 70.0: # M-Gamma
            c[:, 7] += psd[:, i]
            d[7] += 1
        
        elif freqs[i] >= 70.0: # U-Gamma
            c[:, 8] += psd[:, i]
            d[8] += 1
        
        else:
            pass
    
    for i in range(9):
        c[:, i] /= d[i]
        
    return c
    

def taper_window(w=5):
    
    tw = np.zeros(w)
    for i in range(w):
        if i < w/2:
            tw[i] = i+1
        else:
            tw[i] = w-i
    
    return tw/np.sum(tw)
    

def pink_noise_inverse_filter(x=None, w=5, piv=None):
    
    try: 
        
        if piv==None:
            piv = x
            
    except:
        pass
    
    k = np.int(w/2)
    n = np.max(x.shape)
    
    h = taper_window(w)
    y = np.convolve(piv**-1, h)
    h = np.ones(w)/w
    
    y = np.convolve(y[w-k:n+w-k], h)
    return np.multiply(x, y[w-k:n+w-k])
    

def get_trials(c=None, mode='Block', l=0, r=600):
    
    t = []
    for i in range(l, r):
        
        if mode=='block': # Expected, predictable
            if c[i]==0:
                t.append(i)
        elif mode=='trial': # Enexpected, random
            if c[i]:
                t.append(i)
                
    return t

