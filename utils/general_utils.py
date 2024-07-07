from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import moment, probplot
from sklearn.metrics import roc_auc_score, roc_curve
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import acf, adfuller, q_stat


def plot_correlogram(
    x: pd.Series, lags: int = None, title: str = None
) -> None:
    lags = min(10, int(len(x) / 5)) if lags is None else lags
    with sns.axes_style("whitegrid"):
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 8))
        fig.tight_layout(pad=5)

        x.plot(ax=axes[0][0], title="Residuals")
        x.rolling(21).mean().plot(ax=axes[0][0], c="k", lw=1)
        q_p = np.max(q_stat(acf(x, nlags=lags), len(x))[1])
        stats = f"Q-Stat: {np.max(q_p):>8.2f}\nADF: {adfuller(x)[1]:>11.2f}"
        axes[0][0].text(
            x=0.02, y=0.85, s=stats, transform=axes[0][0].transAxes
        )

        probplot(x, plot=axes[0][1])
        mean, var, skew, kurtosis = moment(x, moment=[1, 2, 3, 4])
        s = f"Mean: {mean:>12.2f}\nSD: {np.sqrt(var):>16.2f}\nSkew: {skew:12.2f}\nKurtosis:{kurtosis:9.2f}"
        axes[0][1].text(x=0.02, y=0.75, s=s, transform=axes[0][1].transAxes)

        plot_acf(x=x, lags=lags, zero=False, ax=axes[1][0])
        plot_pacf(x, lags=lags, zero=False, ax=axes[1][1])
        axes[1][0].set_xlabel("Lag")
        axes[1][1].set_xlabel("Lag")

        fig.suptitle(title, fontsize=14)
        sns.despine()
        fig.tight_layout()
        fig.subplots_adjust(top=0.9)


def plot_aucroc_curve(
    true_value: Any, predicted_value: Any, ax=None, plot=True
):
    """Function for plotting auc roc curve"""

    ## Model performance
    auc_roc_score = roc_auc_score(true_value, predicted_value)

    if plot:
        if ax is None:
            fig, ax = plt.subplots(1, 1, figsize=(6, 6))
            fig.tight_layout(pad=5)

        fpr, tpr, _ = roc_curve(true_value, predicted_value)
        ax.plot(fpr, tpr, label="Classifier; AUC=%0.4f" % (auc_roc_score))
        ax.set_xlabel("False positive rate", fontsize=15)
        ax.set_ylabel("True positive rate", fontsize=15)
        ax.legend()

        return auc_roc_score, ax

    else:
        return auc_roc_score


def multiindex_to_singleindex(df: pd.DataFrame) -> pd.DataFrame:
    """Change multiindex to single index for multindex pandas dataframe"""
    df.columns = ["_".join(col) for col in df.columns.values]

    return df
