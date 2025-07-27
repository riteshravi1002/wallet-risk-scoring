# main.py

import logging
import os
import pandas as pd
from fetch_wallets import get_wallets
from compound_api import get_wallet_features
from feature_engineering import compute_features
from scoring import score_wallets

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

OUTPUT_PATH = "data/wallet_scores.csv"

def main():
    logging.info("🚀 Starting wallet risk scoring pipeline...")

    wallets = get_wallets()
    logging.info(f"📥 {len(wallets)} wallets fetched.")

    processed = []
    for i, wallet in enumerate(wallets, 1):
        logging.info(f"🔄 ({i}/{len(wallets)}) Processing {wallet}...")
        try:
            features = get_wallet_features(wallet)
            processed.append(features)
        except Exception as e:
            logging.warning(f"⚠️ Error processing {wallet}: {e}")

    if not processed:
        logging.warning("⚠️ No wallets were processed successfully.")
        return

    logging.info(f"✅ Data collection complete. {len(processed)} wallets processed.")

    df = compute_features(processed)
    scored_df = score_wallets(df)

    # Check before accessing the score column
    if scored_df.empty or "score" not in scored_df.columns:
        logging.warning("⚠️ No active wallets found or scoring failed.")
        return

    scored_df.loc[:, "score"] = scored_df["score"].fillna(0).astype(int)

    os.makedirs("data", exist_ok=True)
    scored_df.to_csv(OUTPUT_PATH, index=False)

    # Summary logs
    logging.info("✅ Scoring complete.")
    logging.info(f"📦 Output saved to: {OUTPUT_PATH}")
    logging.info("📊 Summary:")
    logging.info(f" - Wallets scored: {len(scored_df)}")
    logging.info(f" - Score range: {scored_df['score'].min()} to {scored_df['score'].max()}")
    logging.info(f" - Average score: {scored_df['score'].mean():.2f}")

    print("\n✅ All done!")
    print(f"📦 Output: {OUTPUT_PATH}")
    print("📊 Summary:")
    print(f" - Wallets: {len(scored_df)}")
    print(f" - Score range: {scored_df['score'].min()} to {scored_df['score'].max()}")
    print(f" - Average score: {scored_df['score'].mean():.2f}")


if __name__ == "__main__":
    main()
