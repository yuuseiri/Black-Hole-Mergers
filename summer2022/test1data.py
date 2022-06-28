import pynbody 
import os
import numpy as np

directory = '/mnt/data0/jillian/ICS/ICInG/IsolatedICsFromMichael/test1/'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and (filename.endswith(".param") == False) and (filename.endswith(".txt") == False):
        i = pynbody.load(f)
        print(i.stars['vel'])
        print(i.stars['pos'])
    else: 
        print("There was a .param or .txt file")
        
        
        
    

