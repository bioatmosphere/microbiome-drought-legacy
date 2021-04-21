"""
Script of extracting data of substrates
December 2020
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
    #single run
    filelist = glob.glob(key+'_'+'20201'+'.pickle')
    
    ## ensemble runs--20
    filelist_19   = glob.glob(key + '_' + '2020' + '[1-9].pickle')
    filelist_1019 = glob.glob(key + '_' + '2020' + '1[0-9].pickle')
    filelist_2020 = glob.glob(key + '_' + '2020' + '20.pickle')
    filelist = filelist_19 + filelist_1019 + filelist_2020

    #filelist_2029 = glob.glob(key+'2[0-9].pickle')
    #filelist_3039 = glob.glob(key+'3[0-9].pickle')
    #filelist_4040 = glob.glob(key+'40.pickle')
    #filelist = filelist_19 + filelist_1019 + filelist_2029 + filelist_3039 + filelist_4040

    filelist.sort(reverse=False)
    for file in filelist:
        with open(file,"rb") as f:
            data = pickle.load(f)
        datalist.append(data)

    return filelist, datalist

site = sys.argv[1]    # base site name
key = sys.argv[2]     # target site

os.chdir('../output_'+site)

filelist, datalist = get_pickled_data(key)
## sub-specific mass
#sub = pd.concat([data.SubstratesSeries for data in datalist], axis=1, sort=False)
## total mass
sub = pd.concat([data.SubstratesSeries.sum(axis=0) for data in datalist], axis=1, sort=False)

# rename column names with file names
#filelist_new = [int(item[:-7]) for item in filelist]
#sub.columns = filelist_new
#filelist_sorted = sorted(filelist_new,reverse=False)
#sub = sub[filelist_sorted]

# export to csv
sub.to_csv('data/' + 'Sub_' + site +'_'+ key + '.csv')
