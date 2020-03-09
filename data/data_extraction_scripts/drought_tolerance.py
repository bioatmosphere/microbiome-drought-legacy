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
    """
    Derive a list of data files to be extracted for data.
    """
    datalist = []

    filelist_19   = glob.glob(key+'[1-9].pickle')
    filelist_1019 = glob.glob(key+'1[0-9].pickle')
    filelist_2029 = glob.glob(key+'2[0-9].pickle')
    filelist_3039 = glob.glob(key+'3[0-9].pickle')
    filelist_4040 = glob.glob(key+'40.pickle')

    filelist = filelist_19 + filelist_1019 + filelist_2029 + filelist_3039 + filelist_4040
    filelist.sort(reverse=False)

    for file in filelist:
        with open(file,"rb") as f:
            data = pickle.load(f)
        datalist.append(data)

    return filelist, datalist


def community_drought(data):
    """
    Calculate community-level drought tolerance
    """

    Relative_mass = data.MicrobesSeries.div(data.MicrobesSeries.sum(axis=0),axis=1)
    drought_tol   = data.Microbial_traits['Drought_tolerance']
    community_drought = Relative_mass.mul(drought_tol,axis=0).sum(axis=0)

    return community_drought



folder = sys.argv[1]  # string;
key    = sys.argv[2]  # string;

os.chdir('../output_'+folder)

#call function get_pickled_data()
filelist, datalist = get_pickled_data(key)

#call function community_drought()
drought_tol = pd.concat([community_drought(data) for data in datalist], axis=1, sort=False)


# rename columns with file names
filelist_new = [int(item[:-7]) for item in filelist]
drought_tol.columns = filelist_new
filelist_sorted = sorted(filelist_new,reverse=False)
drought_tol = drought_tol[filelist_sorted]


#export to csv
drought_tol.to_csv('Drought' + '_' + folder + '.csv')


