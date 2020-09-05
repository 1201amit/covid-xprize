import os
import unittest

import pandas as pd

from xprize.xprize_predictor import XPrizePredictor

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = os.path.join(ROOT_DIR, 'fixtures')
EXAMPLE_INPUT_FILE = os.path.join(ROOT_DIR, "../data/input", "20200801_20200804_npis.csv")
DATA_URL = os.path.join(ROOT_DIR, "../data/additional", "OxCGRT_latest.csv")
PREDICTOR_27 = os.path.join(FIXTURES_PATH, "pred27", "predictor.h5")
PREDICTOR_30 = os.path.join(FIXTURES_PATH, "pred30", "predictor.h5")
PREDICTOR_31 = os.path.join(FIXTURES_PATH, "pred31", "predictor.h5")
PREDICTIONS_27 = os.path.join(FIXTURES_PATH, "pred27", "20200801_20200804_predictions.csv")
PREDICTIONS_30 = os.path.join(FIXTURES_PATH, "pred30", "20200801_20200804_predictions.csv")
PREDICTIONS_31 = os.path.join(FIXTURES_PATH, "pred31", "20200801_20200804_predictions.csv")

CUTOFF_DATE = "2020-07-31"
START_DATE = "2020-08-01"
END_DATE = "2020-08-04"

NPI_COLUMNS = ['C1_School closing',
               'C2_Workplace closing',
               'C3_Cancel public events',
               'C4_Restrictions on gatherings',
               'C5_Close public transport',
               'C6_Stay at home requirements',
               'C7_Restrictions on internal movement',
               'C8_International travel controls',
               'H1_Public information campaigns',
               'H2_Testing policy',
               'H3_Contact tracing']


class TestMultiplicativeEvaluator(unittest.TestCase):

    def test_predict(self):
        predictor = XPrizePredictor(PREDICTOR_31, DATA_URL, CUTOFF_DATE, NPI_COLUMNS)
        pred_df = predictor._predict(START_DATE, END_DATE, EXAMPLE_INPUT_FILE)
        self.assertIsInstance(pred_df, pd.DataFrame)

    def test_train(self):
        predictor = XPrizePredictor(None, DATA_URL, CUTOFF_DATE, NPI_COLUMNS)
        model = predictor.train()
        self.assertIsNotNone(model)
