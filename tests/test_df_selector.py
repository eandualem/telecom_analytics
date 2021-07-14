import os
import sys
import unittest
from numpy import number
import pandas as pd
import pandas.api.types as ptypes
from pandas.api import types

sys.path.append(os.path.abspath(os.path.join('../scripts')))
from df_selector import DfSelector


class TestDfSelector(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
        self.cleaner = DfSelector()



if __name__ == '__main__':
    unittest.main()
