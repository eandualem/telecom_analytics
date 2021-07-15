import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../')))
from log import *

my_logger = get_logger("DfSelector")
my_logger.debug("Loaded successfully!")


class DfSelector():

    def __init__(self):
        pass

    def filter_by_count(self, df, column):
        new_df = df[column].value_counts(ascending=False).reset_index().copy()
        new_df = new_df.rename(
            columns={'index': column, column: "count"})
        return new_df

    def find_agg(self, df: pd.DataFrame, agg_column: str, agg_metric: str, col_name: str, top: int, order=False) -> pd.DataFrame:
        new_df = df.groupby(agg_column)[agg_column].agg(agg_metric).reset_index(name=col_name).\
            sort_values(by=col_name, ascending=order)[:top]
        return new_df
