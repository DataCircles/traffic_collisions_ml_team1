import numpy as np
import pandas as pd
from catboost import CatBoostRegressor, Pool
from sklearn.model_selection import train_test_split, KFold
from sklearn import metrics
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

class agg_catboost:
    """
    Catboost training wrapper to store relevant info and make results analysis prettier
    """
    def __init__(self, df, y, feats):
        self.df = df
        self.y = y
        self.feats = feats

    def train_model(self, splits=5, random_state=100):
        """
        Function to train and store catboost mean squared error on multiple k-folds
        INPUT
            df           : pandas DataFrame with training features
            y            : Series - target column
            feats        : list - categorical df columns to train model with 
            splits       : int - number of k-fold splits (default=5)
            random_state : int (deafult=5)
        OUTPUT
            theoreticals     : list
            mses             : list
            feat_importances : list
        """
        kf = KFold(n_splits=splits, shuffle=True, random_state=random_state)

        clf = CatBoostRegressor(verbose=False)

        mses, theoreticals, feat_importances = [], [], []

        for i, (train_index, test_index) in enumerate(kf.split(self.df, self.y)):
            X_train, X_test = self.df.iloc[train_index], self.df.iloc[test_index]
            y_train, y_test = self.y.iloc[train_index], self.y.iloc[test_index]
            
            cat_pool = Pool(X_train, y_train, cat_features=self.feats)
            clf.fit(cat_pool)
            y_hat = clf.predict(X_test)
            means = np.full(shape=y_test.shape, fill_value=y_test.mean())
            
            theoreticals.append(metrics.mean_squared_error(y_test, means))
            mses.append(metrics.mean_squared_error(y_test, y_hat))
            feat_importances.append([round(f, 2) for f in clf.feature_importances_])
        
        self.theoreticals = theoreticals
        self.mses = mses
        self.feat_importances = feat_importances
    
        return f'Training on {splits} k-folds complete'

    def print_metrics(self, round_=False):
        for err, theor, fi in zip(self.mses, self.theoreticals, self.feat_importances):
            if round_:
                print (f'base_mse: {round(theor, 3)}, actual: {round(err, 3)} \n feature_importances: {fi}\n')
            else:
                print (f'base_mse: {theor}, actual: {err} \n feature_importances: {fi}\n')

        return

    def plot_feature_importances(self, title='Feature Importances on Catboost Model'):
        fig, ax = plt.subplots()

        for i, feat in enumerate(self.df.columns):
            ax.barh(feat, width=np.mean([f[i] for f in self.feat_importances]))

        ax.set_title(title)

        plt.tight_layout()

        return