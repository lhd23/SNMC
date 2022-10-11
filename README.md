# Apparent cosmic acceleration from type Ia supernova

This is the analysis code used in the paper Dam, Heinesen, and Wiltshire,
[Mon. Not. Roy. Astron. Soc. 472 (2017) 835](https://doi.org/10.1093/mnras/stx1858)
[[arxiv](https://arxiv.org/abs/1706.07236)].

## Update

07/10/2022: fixes a bug in `distmod.py` that was affecting the
distance moduli of a single data point (thanks to Zac Lane).

## Dependencies and data requirements

This code requires [NumPy](https://numpy.org/), [SciPy](https://www.scipy.org/),
and [PyMultiNest](https://github.com/JohannesBuchner/PyMultiNest) 
(a Python interface of [MultiNest](https://arxiv.org/abs/0809.3437)).

The JLA dataset and covariance matrices used in this analysis 
are not supplied here; they can be downloaded from
[here](http://cdsarc.u-strasbg.fr/viz-bin/qcat?J/A+A/568/A22)
and [here](http://supernovae.in2p3.fr/sdss_snls_jla/covmat_v6.tgz).
In addition, the covariances used in this code have been converted from
FITS format to .npy format; these can be downloaded 
[here](https://doi.org/10.5281/zenodo.831360).
Please cite the respective papers if these products are used in published work.

## Running the code

The dataset used in the analysis computes redshifts in the CMB frame
from JLA heliocentric redshifts. Running `python build.py`
generates the data file `jla.tsv` used in this analysis
ordered as follows

```
zcmb, mb, x1, c, logMass, survey id, zhel, RA, DEC
```

Next, for fast likelihood evaluation, run `python distmod.py`
to produce a look-up table of luminosity distances for each
SNIa and for different cosmological parameter(s).

Running the main script `snsample.py` computes the evidence 
for the model specified by the following command line options:

```
model = int(sys.argv[1])    # 1=Timescape, 2=Empty, 3=Flat
z_cut = float(sys.argv[2])  # redshift cut e.g. 0.033
zdep = int(sys.argv[3])     # redshift dependence in mean stretch and colour distributions (0 or 1)
case = int(sys.argv[4])     # redshift light curve model (1-8)
nsigma = int(sys.argv[5])   # 1, 2 or 3 sigma omega/fv prior
nlive = int(sys.argv[6])    # number of live points used in sampling
tol = float(sys.argv[7])    # stop evidence integral when next contribution less than tol
```