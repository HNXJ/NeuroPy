import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import plotly
import mne
import cv2


def print_dict_content(dict_=None):
    
    for v in dict_.keys():
        try:
            print("Value: ", v, " || Size: ", dict_[v].shape)
        except:
            print("Value: ", v)

    return


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


def customlineplot(x=None, y=None, save=False, show=True, filename="plot.html"
               ,xlabel="T", ylabel="A", title="Plot"):
    
        print("Plotting, preprocessing ...")
        fig = px.line(x=x, y=y, title=title)    
    
        if save==True:
            plotly.offline.plot(fig, filename=filename)
        
        if show==True:
            fig.show()
        
        print("Done.")
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
                bw=15, trials=None, pink_noise_filter=True): # Deprecated, only for demo
    
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
    

def power_spectrum_density(data=None, save=False,
                t1=500, t2=2501, fmin=0, fmax=100,
                normalize_w=False, k=5,
                bw=15, trials=None, pink_noise_filter=True):
    
    ps_pfc, f = pspectlamnorm(data[t1:t2, :, trials], axis=0, fs=1000, fc=500, fmin=fmin, fmax=fmax)
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
       
    ps_pfc[np.isnan(ps_pfc)] = 0
    return ps_pfc, f


def psd_ratio_plotter(psd=None, freqs=None, title="P. 1"):
    
    bandlabels = ["Delta[0.1-3]", "Theta[3-8]", "Alpha[8-12]"
                  , "L-Beta[12-16]", "M-Beta[16-20]", "U-Beta[20-30]"
                  , "L-Gamma[30-50]", "M-Gamma[50-70]", "U-Gamma[70+]"
                  , "UI-Gamma[100-150]", "UII-Gamma[150-200]", "UIII-Gamma[200-250]"]
    
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
                  , "L-Gamma[30-50]", "M-Gamma[50-70]", "U-Gamma[70-100]"
                  , "UI-Gamma[100-150]", "UII-Gamma[150-200]", "UIII-Gamma[200-250]"]
    
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
    
    c = np.zeros((16, 12))
    d = np.zeros((12))
    
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
        
        elif freqs[i] < 100: # U-Gamma
            c[:, 8] += psd[:, i]
            d[8] += 1
        
        elif freqs[i] < 150.0: # UI-Gamma
            c[:, 9] += psd[:, i]
            d[9] += 1
            
        elif freqs[i] < 200.0: # UII-Gamma
            c[:, 10] += psd[:, i]
            d[10] += 1
            
        elif freqs[i] < 250.0: # UIII-Gamma
            c[:, 11] += psd[:, i]
            d[11] += 1
            
        else:
            pass
    
    for i in range(12):
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
    

def ERP_plot(data=None, title="", save=False, filename="ERP_plot"):
    
    lam = np.mean(data, 2).transpose()
    lam = cv2.resize(lam, (900, 300))
    t = np.linspace(-1500, 3000, 900)
    y = np.linspace(1, 16, 300)
    
    fig = go.Figure(
        data=go.Heatmap(z=lam, y=y, x=t), 
        layout=go.Layout(
            title=title,
            xaxis=dict(title='Time(ms)'),
            yaxis=dict(title='Channel ID')
        ),
    )
    
    if save==True:
        plotly.offline.plot(fig, filename="Files/" + filename + ".html")

    fig.show()
    return


def CSD_plot(data=None, title="", save=False, filename="ERP_plot"):
    
    lam = data
    sig = 2*(10**-4)
    es = 0.4
    
    csd = sig*(lam[:, 0:14, :] - 2*lam[:, 1:15, :] +lam[:, 2:16, :])/(2*(es**2))
    acsd = np.mean(csd, 2).transpose()
    
    acsd = cv2.resize(acsd, (900, 300))
    t = np.linspace(-1500, 3000, 900)
    y = np.linspace(3, 13, 300)
    
    fig = go.Figure(
        data=go.Heatmap(z=acsd, y=y, x=t), 
        layout=go.Layout(
            title=title,
            xaxis=dict(title='Time(ms)'),
            yaxis=dict(title='Channel ID')
        ),
    )
    
    if save==True:
        plotly.offline.plot(fig, filename="Files/" + filename + ".html")
        
    fig.show()
    return


