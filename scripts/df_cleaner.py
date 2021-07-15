from log import *
import os
import sys
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../')))

my_logger = get_logger("DfCleaner")
my_logger.debug("Loaded successfully!")


class DfCleaner():
    """
        Has functions for cleans pandas data frame by removing duplicates, 
        droping columns or rows and more.
    """

    def __init__(self):
        pass

    def fixLabel(self, label: list) -> list:
        """convert list of labels to lowercase separated by underscore

        Args:
            label (list): list of labels 

        Returns:
            list: list of labels in lower case, separated by underscore
        """
        label = label.strip()
        label = label.replace(' ', '_').replace('.', '').replace('/', '_')
        return label.lower()

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """drop duplicate rows

        Args:
            df (pd.DataFrame): pandas data frame

        Returns:
            pd.DataFrame: pandas data frame
        """
        df.drop_duplicates(inplace=True)
        return df

    def drop_columns(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """ drop selected columns from data frame

        Args:
            df (pd.DataFrame):  pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame columns dropped
        """
        for col in columns:
            df.drop(col, axis=1, inplace=True)
        return df

    def drop_rows(self, df: pd.DataFrame, column: str, row_value: str) -> pd.DataFrame:
        """drop rows in selected column based on condition given
        Args:
            df (pd.DataFrame): pandas data frame
            column (str): column label
            row_value (str): condition to check againest

        Returns:
            pd.DataFrame: pandas data frame with rows dropped
        """
        df = df.drop(df[df[column] != row_value].index)
        return df

    def columns_too_much_null(self, df: pd.DataFrame, percentage: int) -> pd.DataFrame:
        """drops columns with big persentage of null values

        Args:
            df (pd.DataFrame): pandas data frame
            percentage (int): persentage of null values

        Returns:
            [type]: pandas data frame columns dropped
        """
        columns = []
        for index, row in df.iterrows():
            if float(row["none_percentage"].replace("%", '')) > percentage:
                columns.append(index)

        return columns

    def convert_to_string(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to string

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """

        for col in columns:
            df[col] = df[col].astype("string")
        return df

    def convert_to_numbers(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to number

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """
        for col in columns:
            df[col] = pd.to_numeric(df[col])
        return df

    def convert_to_integer(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to number

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """
        for col in columns:
            df[col] = df[col].astype('int64')
        return df

    def convert_to_datetime(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to datetime

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """
        for col in columns:
            df[col] = pd.to_datetime(df[col])
        return df

    def convert_to_boolean(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """convert selected columns to boolean

        Args:
            df (pd.DataFrame): pandas data frame
            columns (list): list of column labels

        Returns:
            pd.DataFrame: pandas data frame with converted data types
        """
        for col in columns:
            df[col] = df[col].astype("bool")
        return df

    def converter(self, df: pd.DataFrame, column, scale):
        df[column] = df[column] * scale
        return df

    def fix_missing_ffill(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(method='ffill')
        return df

    def fix_missing_bfill(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(method='bfill')
        return df

    def fill_with_mode(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(df[col].mode()[0])
        return df

    def fill_with_mean(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(df[col].mean())
        return df

    def fill_with_median(self, df: pd.DataFrame, columns):
        for col in columns:
            df[col] = df[col].fillna(df[col].median())
        return df

    def percent_missing(self, df):
        totalCells = np.product(df.shape)
        missingCount = df.isnull().sum()
        totalMissing = missingCount.sum()
        return str(round(((totalMissing/totalCells) * 100), 2))
