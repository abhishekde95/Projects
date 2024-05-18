from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score, roc_curve


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
