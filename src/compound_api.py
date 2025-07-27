import requests
from config import COMPOUND_GRAPH_URL

def run_query(query: str):
    response = requests.post(COMPOUND_GRAPH_URL, json={'query': query})
    if response.status_code != 200:
        raise Exception(f"GraphQL query failed: {response.status_code}, {response.text}")
    return response.json()

def get_wallet_features(wallet: str) -> dict:
    query = f"""
    {{
      account(id: "{wallet.lower()}") {{
        id
        tokens {{
          symbol
          supplyBalanceUnderlying
          borrowBalanceUnderlying
        }}
        health
        countLiquidations
      }}
    }}
    """
    result = run_query(query)
    data = result.get("data", {}).get("account", {})

    if not data:
        return {
            "wallet_id": wallet,
            "supply": 0,
            "borrow": 0,
            "health": 0,
            "liquidations": 0,
            "asset_count": 0
        }

    tokens = data.get("tokens", [])
    return {
        "wallet_id": wallet,
        "supply": sum(float(t.get("supplyBalanceUnderlying", 0) or 0) for t in tokens),
        "borrow": sum(float(t.get("borrowBalanceUnderlying", 0) or 0) for t in tokens),
        "health": float(data.get("health", 0) or 0),
        "liquidations": int(data.get("countLiquidations", 0) or 0),
        "asset_count": len(tokens),
    }
