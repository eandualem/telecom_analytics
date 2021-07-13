import pandas as pd

class DfCleaner():

  def __init__(self):
    pass

  def fixLabel(self, label):
    label = label.strip()
    label = label.replace(' ', '_').replace('.', '').replace('/', '_')
    return label.lower()

  def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
    df.drop_duplicates(inplace=True)
    return df

  def drop_columns(self, df: pd.DataFrame, columns) -> pd.DataFrame:
    df = df.drop(columns, axis=1, inplace=True)
    return df

  def drop_rows(self, df: pd.DataFrame, column, row_value) -> pd.DataFrame:
    df = df.drop(df[df['lang'] != 'en'].index)
    return df

  def columns_too_much_null(self, df: pd.DataFrame, percentage: int):
    columns = []
    for index, row in df.iterrows():
      if float(row["none_percentage"].replace("%", '')) > percentage:
          columns.append(index)

    return columns

  def converter(self, df: pd.DataFrame, column, scale):
    df[column] = df[column] * scale
    return df

  def fix_missing_ffill(self, df: pd.DataFrame, col):
    df[col] = df[col].fillna(method='ffill')
    return df[col]

  def fix_missing_bfill(self, df: pd.DataFrame, col):
      df[col] = df[col].fillna(method='bfill')
      return df[col]

  def percent_missing(self, df):
      totalCells = np.product(df.shape)
      missingCount = df.isnull().sum()
      totalMissing = missingCount.sum()
      return str(round(((totalMissing/totalCells) * 100), 2))
