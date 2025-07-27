import pandas as pd
from config import WALLETS_CSV_URL

def get_wallets():
    df = pd.read_csv(WALLETS_CSV_URL)
    return df.iloc[:, 0].dropna().unique().tolist()
