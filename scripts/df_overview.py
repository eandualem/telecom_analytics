from log import *
import os
import sys
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath(os.path.join('../')))

my_logger = get_logger("DfOverview")
my_logger.debug("Loaded successfully!")


class DfOverview:
    """
        Give an overview for a given data frame, 
        like null persentage for each columns, 
        unique value percentage for each columns and more
    """

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def missing_value(self) -> None:
        nullSum = self.df.isna().sum()
        return [col for col in nullSum]

    def unique_values(self) -> None:
        return [self.getUniqueCount(column) for column in self.df]

    def percentage(self, list):
        return [str(round(((value/150001) * 100), 2)) + '%' for value in list]

    def getOverview(self) -> None:
        stat = df.describe()
        _count = [stat[column]['count'] for column in stat]
        _min = [stat[column]['min'] for column in stat]
        _max = [stat[column]['max'] for column in stat]
        _mean = [stat[column]['mean'] for column in stat]
        _median = [stat[column]['50%'] for column in stat]

        columns = [
            'label',
            'unique_value_count',
            'unique_percentage',
            'none_count',
            'none_percentage',
            'min_value',
            'max_value',
            'mean',
            'median',
            'dtype']
        data = zip(
            [column for column in self.df],
            _count,
            self.percentage(_count),
            self.missing_value(),
            self.percentage(self.missing_value()),
            _min,
            _max,
            _mean,
            _median,
            self.df.dtypes
        )
        new_df = pd.DataFrame(data=data, columns=columns)
        new_df.set_index('label', inplace=True)
        return new_df
