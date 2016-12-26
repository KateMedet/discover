
######### Import libraries #########
import os
import sys

import matplotlib as mpl

mpl.rcParams['figure.figsize'] = (8, 5)
mpl.rcParams['figure.max_open_warning'] = 100

######### Set up Simpli NB Project directories #########
DIR_PROJECT = os.path.join('/Users/kateme/discover')
DIR_CODE = os.path.join(DIR_PROJECT, 'code')
DIR_DATA = os.path.join(DIR_PROJECT, 'data')
DIR_RESULT = os.path.join(DIR_PROJECT, 'results')
DIR_MEDIA = os.path.join(DIR_PROJECT, 'media')

######### Set up tools #########
sys.path.insert(0, '../code')
import ccal


### Load expressional signatures ###
ccle_signatures = ccal.read_gct('/Users/kateme/discover/data/CCLE_Expression_Entrez_2012-04-06_plus_Achilles.SELECTED_TISSUES_PATHWAYS.gct')
ccle_hNSC_G3_150_UP = ccle_signatures.ix['hNSC_G3_150_UP']
sanger_signatures = ccal.read_gct('/Users/kateme/discover/data/Sanger_Expression.out.SELECTED_TISSUES_PATHWAYS.gct')
sanger_hNSC_G3_150_UP = sanger_signatures.ix['hNSC_G3_150_UP']

### Load drug sensitivities ###
ccle_drug_sensitivity = ccal.read_gct('/Users/kateme/discover/data/CCLE_Drug_Sensitivity.gct')
ctrp_drug_sensitivity = ccal.read_gct('/Users/kateme/discover/data/CTRPv2.2_2015_pub.gct')
sanger_drug_sensitivity = ccal.read_gct('/Users/kateme/discover/data/drug_sensitivity.out.SELECTED.gct')