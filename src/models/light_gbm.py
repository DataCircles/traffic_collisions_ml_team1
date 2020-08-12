import lightgbm as lgb
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, confusion_matrix, auc, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns




def predictions(gbm, X_test, y_test):
    # Do prediction and get AUC score
    y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)
    auc_score = roc_auc_score(y_test, y_pred)
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label='AUC: {:2.2f}'.format(auc_score))
    ax.legend(loc='lower right')
    ax.set_title('ROC Curve')
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.plot(np.linspace(0,1,100), np.linspace(0,1,100), '--')
    plt.savefig('reports/figures/lightgbm_roc.png')
    return fig


def light_gbm(X, y, name=None):
    X_train, X_test, y_train, y_test = train_test_split(X,y)
    
    # Create dataset for lightgbm
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

    # specify configuration
    params = {
            'boosting_type': 'gbdt',
            'objective': 'binary',
            'num_leaves': 31,
            'learning_rate': 0.01,
            'feature_fraction': 0.8,
            'bagging_fraction': 0.8,
            'bagging_freq': 5,
            'verbose': 0
    }

    gbm = lgb.train(params, 
                    lgb_train, 
                    num_boost_round=20, 
                    valid_sets=lgb_eval, 
                    early_stopping_rounds=5)

    #gbm.save_model('lgbm_model.txt')
    label = f'Feature Importance for {name}'
    lgb.plot_importance(gbm, title=label)
    plt.savefig('reports/figures/lightgbm_importance_allcollisions.png')
    
    
    fig = predictions(gbm, X_test, y_test)   
    
    return fig