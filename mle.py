from __future__ import division

from scipy import optimize
import numpy as np
import sys

from snsample import loglike,sort_and_cut,getindices
from getsplines import spl


def m2ll(p): #-2*loglikelihood  
    ndim = p.size
    npars = ndim
    return -2*llike(p,ndim,npars)

if __name__ == '__main__':

    Z = np.loadtxt('jla.tsv')
    COVd = np.load('covmat/stat.npy')
    for i in ['cal', 'model', 'bias', 'dust', 'sigmaz', 'sigmalens', 'nonia']:
        COVd += np.load('covmat/'+i+'.npy')

    # initialise likelihood / input data and model
    model = int(sys.argv[1]) #1=ts, 3=flatlcdm
    z_cut = 0.033
    zdep = 0
    case = 1

    ipars = getindices(zdep,case)
    tempInt = spl.ts if model == 1 else spl.lcdm

    # get data
    Z, COVd, tempInt = sort_and_cut(z_cut,Z,COVd,tempInt)
    zcmb = Z[:,0]
    zhel = Z[:,6]
    tri = Z[:,1:4]
    snset = Z[:,5]

    llike = loglike(model,zdep,case,ipars,zcmb,zhel,tri,snset,COVd,tempInt)

    # starting parameters
    guess_ts = np.array([0.778, 0.134, 0.105, 0.809, 3.13, -0.0211, 0.00474, -19.1, 0.0108])
    guess_fl = np.array([0.365, 0.134, 0.106, 0.808, 3.14, -0.0215, 0.00473, -19.0, 0.0107])
    guess = guess_ts if model == 1 else guess_fl

    bounds = ((0.001,0.99),(None,None),(None,None),(0,None),(None,None),
              (None,None),(0,None),(None,None),(0,None))

    MLE = optimize.minimize(m2ll, guess, bounds=bounds, method='SLSQP', tol=1e-8)
    print MLE

