import pandas as pd
from feature_engineering import normalize

def score_wallets(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    # Normalize features
    df["norm_health"] = normalize(df["health"])
    df["norm_collateral_ratio"] = normalize(df["collateral_ratio"])
    df["norm_liquidations"] = 1 - normalize(df["liquidations"])
    df["norm_borrow"] = 1 - normalize(df["borrow"])
    df["norm_supply"] = normalize(df["supply"])
    df["norm_asset_count"] = normalize(df["asset_count"])

    # Weighted scoring
    df["score"] = (
        0.3 * df["norm_health"] +
        0.2 * df["norm_collateral_ratio"] +
        0.15 * df["norm_liquidations"] +
        0.15 * df["norm_borrow"] +
        0.1 * df["norm_supply"] +
        0.1 * df["norm_asset_count"]
    ) * 1000

    df["score"] = df["score"].round().astype(int)
    return df[["wallet_id", "score"]]
