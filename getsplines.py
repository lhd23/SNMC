from __future__ import division
from scipy import interpolate
import numpy as np

class spl(object):
    Ntotal = 740

    interp = np.load('tabledL_ts.npy')
    oms = np.linspace(0.00,0.99,100)
    oms[0] = 0.001
    ts = []
    for i in range(Ntotal):
        ts.append(interpolate.InterpolatedUnivariateSpline(oms, interp[i]))

    interp = np.load('tabledL_lcdm.npy')
    oms = np.linspace(0,1.0,101)
    ols = np.linspace(0,1.0,101)
    lcdm = []
    for i in range(Ntotal):
        lcdm.append(interpolate.RectBivariateSpline(oms, ols, interp[i]))
