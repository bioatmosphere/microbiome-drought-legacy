"""
Script of extracting data and calculating community level drought tolerance from the source data (.pickle)
"""

import numpy as np
import pandas as pd
import pickle
import sys
import os
import glob
import output




# define a function of extracting data from files in .pickle 
def get_pickled_data(key):
    datalist = []
    filelist = glob.glob(key+'.pickle')
    filelist.sort(reverse=False)
    for file in filelist:
        with open(file,"rb") as f:
            data = pickle.load(f)
        datalist.append(data)

    return filelist, datalist



folder = sys.argv[1]
key = sys.argv[2]

os.chdir('../output_'+folder)

filelist, datalist = get_pickled_data(key)
microbe_traits = pd.concat([data.Microbial_traits for data in datalist], axis=1, sort=False)


microbe_traits.to_csv('Mic_traits' + folder +'_'+ key + '.csv')