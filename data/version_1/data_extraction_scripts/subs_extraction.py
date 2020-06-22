"""
Script of extracting data of substrate-specific mass 
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

    return filelist,datalist

folder = sys.argv[1]
key    = sys.argv[2]

os.chdir('../output_'+folder)
filelist, datalist = get_pickled_data(key)

sub = pd.concat([data.SubstratesSeries for data in datalist], axis=1, sort=False)

# export to csv
sub.to_csv('Substrates' + '_' + folder + '_' + key + '.csv')