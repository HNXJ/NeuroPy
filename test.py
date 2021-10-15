import scipy.io as sio
from Methods import *
from Granger import *

### Load data and show content of it
data = sio.loadmat('data.mat') # Example data, private access
print_all_content(data)


