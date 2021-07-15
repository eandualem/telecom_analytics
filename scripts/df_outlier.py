import os
import sys
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath(os.path.join('../')))
from log import *

my_logger = get_logger("DfOutlier")
my_logger.debug("Loaded successfully!")


class DfOutlier:
    """
        Give an overview for a given data frame, 
        percentage of outliers in each column and 
        has methods for removeing or replacing outliers.
    """
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def count_outliers(self, Q1, Q3, IQR):
        cut_off = IQR * 1.5
        temp_df = (self.df < (Q1 - cut_off)) | (self.df > (Q3 + cut_off))
        return [len(temp_df[temp_df[col] == True]) for col in temp_df]

    def calc_skew(self):
        return [self.df[col].skew() for col in self.df]

    def percentage(self, list):
        return [str(round(((value/150001) * 100), 2)) + '%' for value in list]

    def find_statistical_information(self, column):
        return self.df.groupby(column).size().agg(['count', 'min', 'max', 'mean', 'median'])

    def remove_outliers(self, columns):
        for col in columns:
            Q1, Q3 = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            cut_off = IQR * 1.5
            lower, upper = Q1 - cut_off, Q3 + cut_off
            self.df = self.df.drop(self.df[self.df[col] > upper].index)
            self.df = self.df.drop(self.df[self.df[col] < lower].index)

    def replace_outliers_with_iqr(self, columns):
        for col in columns:
            Q1, Q3 = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            cut_off = IQR * 1.5
            lower, upper = Q1 - cut_off, Q3 + cut_off

            self.df[col] = np.where(self.df[col] > upper, upper, self.df[col])
            self.df[col] = np.where(self.df[col] < lower, lower, self.df[col])

    def getOverview(self) -> None:
        stat = [self.find_statistical_information(
            column) for column in self.df]
        Q1 = self.df.quantile(0.25)
        Q3 = self.df.quantile(0.75)
        IQR = Q3 - Q1
        _skew = self.calc_skew()
        _outliers = self.count_outliers(Q1, Q3, IQR)
        _min = [round((i[1]), 2) for i in stat]
        _max = [round((i[2]), 2) for i in stat]
        _mean = [round((i[3]), 2) for i in stat]
        _median = [round((i[4]), 2) for i in stat]

        columns = [
            'label',
            'Q1',
            'median',
            'Q3',
            'IQR',
            'skew',
            'number_of_outliers',
            'percentage_of_outliers',
            'min_value',
            'max_value',
            'mean', ]
        data = zip(
            [column for column in self.df],
            Q1,
            _median,
            Q3,
            IQR,
            _skew,
            _outliers,
            self.percentage(_outliers),
            _min,
            _max,
            _mean,
        )
        new_df = pd.DataFrame(data=data, columns=columns)
        new_df.set_index('label', inplace=True)
        return new_df
