######### Set up Notebook Project (NB Project) #########
print('Launching NB Project ...')
import sys
from os.path import join, realpath

DIR_PROJECT = realpath('..')
print('\tExported variable DIR_PROJECT ({}).'.format(DIR_PROJECT))

DIR_TOOLS = join(DIR_PROJECT, 'tools/')
sys.path.insert(0, DIR_TOOLS)
print('\tExported variable DIR_TOOLS ({}).'.format(DIR_TOOLS))

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
