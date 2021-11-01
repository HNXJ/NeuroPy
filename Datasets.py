import scipy.io as sio
# import numpy as np

# import Methods
# import Connect
# import Viewer
import pickle


class Dataset:
    
    """
        This class is the core data handler of this toolbox. 
        
        For easier and better using of functions, try to put your data
        on this class.
        
        Put raw loaded file in self.data; recordings in self.signals and so on.
    """
    
    def __init__(self, type="lam"):
        
        self.signals = dict()
        self.cues = None
        self.cue_types = []
        self.data = None
        
        return
    
    def load_laminar_data(self, path="Data/"):
        
        """
        This function is only for A.M Bastos's lab data loading.
        """
        print("Loading data...")
        self.data = sio.loadmat(path + "data.mat")
        self.cues = sio.loadmat(path + "cues.mat")['c']
        print("Loaded.")
        
        self.signals['pfc'] = self.data['lfp'][:, 0:16, :]
        self.signals['p7a'] = self.data['lfp'][:, 16:32, :]
        self.signals['v4'] = self.data['lfp'][:, 32:48, :]
        self.cue_types = ['block', 'trial']
        
        return
        
    def print_all_content(self):
        """
        If your dataset is a python dictionary or a matlab .mat file loaded by 
        Scipy.IO, you can call this method on it in order to check its content.
        """
        for v in self.data.keys():
            try:
                print("Value: ", v, " || Size: ", self.data[v].shape)
            except:
                print("Value: ", v)
    
        return
        
    def get_trials(self, key='cue_type', l=0, r=100):
        
        """
        Cue ID extractor. It will give you ID of trials that are in [l<id<r] 
        and also are from "key" type.
        """
        t = []
        for i in range(l, r):
            
            for j in range(len(self.cue_types)):
                if key==self.cue_types[j]:
                    if self.cues[i]==j:
                        t.append(i)
                    
        return t
    

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
    

    