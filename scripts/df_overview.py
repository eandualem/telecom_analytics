import pandas as pd


class DfOverview:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def missingValue(self) -> None:
        nullSum = self.df.isna().sum()
        return [col for col in nullSum]

    def uniqueValues(self) -> None:
        return [self.getUniqueCount(column) for column in self.df]

    def percentage(self, list):
        return [str(round(((value/150001) * 100), 2)) + '%' for value in list]

    def findStatisticalInformation(self, column):
        return self.df.groupby(column).size().agg(['count', 'min', 'max', 'mean', 'median'])

    def getOverview(self) -> None:
        stat = [self.findStatisticalInformation(column) for column in self.df]
        _count = [int(i[0]) for i in stat]
        _min = [round((i[1]), 2) for i in stat]
        _max = [round((i[2]), 2) for i in stat]
        _mean = [round((i[3]), 2) for i in stat]
        _median = [round((i[4]), 2) for i in stat]

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
            self.missingValue(),
            self.percentage(self.missingValue()),
            _min,
            _max,
            _mean,
            _median,
            self.df.dtypes
        )
        new_df = pd.DataFrame(data=data, columns=columns)
        new_df.set_index('label', inplace=True)
        return new_df
