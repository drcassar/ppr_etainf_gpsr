from pprint import pprint

import pandas as pd
from matplotlib import pyplot as plt

from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import median_absolute_error as MedAE
from sklearn.metrics import mean_absolute_error as MAE


###############################################################################
#                                  Functions                                  #
##############################################################################+

def predict_etainf(Tg, m):
    log_etainf = 0.97 - 0.14 * (Tg / m) 
    return log_etainf


def R2_1p(y_true, y_pred):
    return 1 - sum((y_true - y_pred)**2) / sum(y_true**2)


###############################################################################
#                                    Config                                   #
##############################################################################+

DATAPATH = r'dump/fit_results.csv'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': 'DejaVu Serif',
    'axes.formatter.limits': [-2, 5],
    'axes.formatter.useoffset': False,
    'axes.formatter.use_mathtext': True,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.top': True,
    'ytick.right': True,
    'legend.framealpha': 1,
    'legend.edgecolor': 'k',
    'figure.figsize': [5 ,5],
    'errorbar.capsize': 5,
    'mathtext.fontset': 'dejavuserif',
})


###############################################################################
#                                 Calculations                                #
##############################################################################+


data = pd.read_csv(DATAPATH)
ninf_pred = predict_etainf(data.Tg, data.m)
ninf_true = data.ninf.values

metrics = {}

metrics['RMSE'] = MSE(ninf_true, ninf_pred, squared=False)
metrics['MAE'] = MAE(ninf_true, ninf_pred)
metrics['MedAE'] = MedAE(ninf_true, ninf_pred)
metrics['R2'] = R2_1p(ninf_true, ninf_pred)

print()
pprint(metrics)


###############################################################################
#                                     Plot                                    #
##############################################################################+

fig, axe = plt.subplots(
    ncols=1,
    nrows=1,
    figsize=(5, 5),
    dpi=150,
)

axe.plot(ninf_true, ninf_pred, marker='o', ls='none', markeredgecolor='black',)

axe.axvline(-2.93, ls='--', c='gray')
axe.axhline(-2.93, ls='--', c='gray')

axe.set_xlabel('$\log_{10}(\eta_\infty)$ (MYEGA regression)')
axe.set_ylabel('$\log_{10}(\eta_\infty)$ (Predicted by new equation)')

fig.savefig(
    r'plots/test_new_equation.png',
    dpi=150,
    bbox_inches='tight',
    pad_inches=2e-2,
)

plt.close(fig)
