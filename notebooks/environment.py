######### Set up Notebook Project (NB Project) #########
print('Launching NB Project ...')
import sys
from os.path import join, realpath

DIR_PROJECT = realpath('..')
print('\tExported variable DIR_PROJECT ({}).'.format(DIR_PROJECT))

DIR_TOOLS = join(DIR_PROJECT, 'tools/')
sys.path.insert(0, DIR_TOOLS)
print('\tExported variable DIR_TOOLS ({}), and added it to the path.'.format(DIR_TOOLS))

DIR_DATA = join(DIR_PROJECT, 'data/')
print('\tExported variable DIR_DATA ({}).'.format(DIR_DATA))

DIR_RESULT = join(DIR_PROJECT, 'results/')
print('\tExported variable DIR_RESULT ({}).'.format(DIR_RESULT))

DIR_MEDIA = join(DIR_PROJECT, 'media/')
print('\tExported variable DIR_MEDIA ({}).'.format(DIR_MEDIA))

######### Set up project specific parameters #########
import numpy as np
import pandas as pd
import matplotlib as mpl
from statsmodels.sandbox.stats.multicomp import multipletests
from matplotlib.backends.backend_pdf import PdfPages
mpl.rcParams['figure.figsize'] = (8, 5)
mpl.rcParams['figure.max_open_warning'] = 100
sys.path.insert(0, DIR_TOOLS)
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
