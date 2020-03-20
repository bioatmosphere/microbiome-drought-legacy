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
    
    #filelist_19   = glob.glob(key+'[1-9].pickle')
    #filelist_1019 = glob.glob(key+'1[0-9].pickle')
    #filelist_2029 = glob.glob(key+'2[0-9].pickle')
    #filelist_3039 = glob.glob(key+'3[0-9].pickle')
    #filelist_4040 = glob.glob(key+'40.pickle')    # 202040

    filelist_4149 = glob.glob(key+'4[1-9].pickle') # 41 - 49
    filelist_5059 = glob.glob(key+'5[0-9].pickle')
    filelist_6069 = glob.glob(key+'6[0-9].pickle')
    filelist_7079 = glob.glob(key+'7[0-9].pickle')
    filelist_8089 = glob.glob(key+'8[0-9].pickle')
    filelist_9099 = glob.glob(key+'9[0-9].pickle')

    filelist_100109 = glob.glob(key+'10[0-9].pickle')
    filelist_110119 = glob.glob(key+'11[0-9].pickle')
    filelist_120129 = glob.glob(key+'12[0-9].pickle')
    filelist_130139 = glob.glob(key+'13[0-9].pickle')
    filelist_140149 = glob.glob(key+'14[0-9].pickle')
    filelist_150159 = glob.glob(key+'15[0-9].pickle')
    filelist_160169 = glob.glob(key+'16[0-9].pickle')
    filelist_170179 = glob.glob(key+'17[0-9].pickle')
    filelist_180189 = glob.glob(key+'18[0-9].pickle')
    filelist_190199 = glob.glob(key+'19[0-9].pickle')

    #filelist = filelist_19 + filelist_1019 + filelist_2029 + filelist_3039 + filelist_4040
    filelist = filelist_4149 + filelist_5059 + filelist_6069 + filelist_7079 + filelist_8089 + filelist_9099 +\
        filelist_100109 + filelist_110119 + filelist_120129 + filelist_130139 + filelist_140149 +\
            filelist_150159 + filelist_160169 + filelist_170179 + filelist_180189 + filelist_190199
    filelist.sort(reverse=False)

    for file in filelist:
        with open(file,"rb") as f:
            data = pickle.load(f)
        datalist.append(data)

    return filelist, datalist



folder = sys.argv[1]  # e.g.: basex2, basex10_dis
key    = sys.argv[2]  # 2020


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
sub.to_csv('Sub_41' + '_' + folder + '.csv')