import os
import sys
import unittest
from numpy import number
import pandas as pd
import pandas.api.types as ptypes
from pandas.api import types

sys.path.append(os.path.abspath(os.path.join('../scripts')))
from df_overview import DfOverview


class TestDfOverview(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
        self.cleaner = DfOverview()


if __name__ == '__main__':
    unittest.main()
