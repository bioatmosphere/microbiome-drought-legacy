"""
Script of extracting data from pickle files obtained from ensemble simulations
"""

import numpy as np
import pandas as pd
import output
import pickle
import os
import glob
import sys

# define a function of extracting data from files in .pickle 
def get_pickled_data(key):
    datalist = []
    filelist = glob.glob(key+'*')
    filelist.sort(reverse=False)
    for file in filelist:
        with open(file,"rb") as f:
            data = pickle.load(f)
        datalist.append(data)

    return filelist,datalist
    


folder = sys.argv[1]
key    = sys.argv[2]

# derive the data of substrates
os.chdir('../output_' + folder)
filelist,datalist = get_pickled_data(key)

sub = pd.concat([data.SubstratesSeries.sum(axis=0) for data in datalist], axis=1, sort=False)
# rename columns with file names
filelist_new = [int(item[:-7]) for item in filelist]
sub.columns = filelist_new
filelist_sorted = sorted(filelist_new,reverse=False)
sub = sub[filelist_sorted]

#export to csv
sub.to_csv('Sub' + '_' + folder + '.csv')

