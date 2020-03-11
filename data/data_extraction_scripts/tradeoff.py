"""
Script of extracting and calculating taxon-level tradeoff from the source data (.pickle)
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

#command line arguments
folder = sys.argv[1]
os.chdir('../output_'+folder)

key    = sys.argv[2]
filelist, datalist = get_pickled_data(key)

# taxon-specific enzyme
Enzyme = pd.concat([data.Enzyme_TaxonSeries for data in datalist], axis=1, sort=False)
Enzyme.to_csv('Enzyme_' + folder +'_'+ key + '.csv')

# taxon-specific osmolyte
Osmolyte = pd.concat([data.Osmolyte_TaxonSeries for data in datalist], axis=1, sort=False)
Osmolyte.to_csv('Osmolyte_' + folder +'_'+ key + '.csv')

# taxon-specific growth yield
Yield = pd.concat([data.Growth_yield for data in datalist], axis=1, sort=False)
Yield.to_csv('Yield_' + folder +'_'+ key + '.csv')
