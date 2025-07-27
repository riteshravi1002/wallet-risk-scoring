import pandas as pd

def compute_features(wallet_data: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(wallet_data)
    df["collateral_ratio"] = df["supply"] / (df["borrow"] + 1e-6)
    df.fillna(0, inplace=True)
    return df

def normalize(series: pd.Series) -> pd.Series:
    return (series - series.min()) / (series.max() - series.min() + 1e-9)
