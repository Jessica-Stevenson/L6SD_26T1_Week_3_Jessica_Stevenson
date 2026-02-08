import pandas as pd

import numpy as np

s = pd.Series() 
print("Pandas Series: ", s) 
data = np.array(['C', 'l', 'a', 'i', 'r', '-', 'O', 'b', 's', 'c', 'u', 'r']) 
  
s = pd.Series(data) 
print("Pandas Series:\n", s)