import requests
import time
import json
from datetime import datetime

BASE_URL = "https://fapi.binance.com/fapi/v1"
SYMBOL = "BTCUSDT"
SLEEP_SECONDS = 60
OUTPUT_FILE = "funding_rates.jsonl"

def get_funding_rate():
    url = f"{BASE_URL}/fundingRate"
    params = {"symbol": SYMBOL, "limit": 1}

    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()

    data = resp.json()

    if not data:
        return None

    latest = data[0]

    return {
        "symbol": latest["symbol"],
        "fundingRate": float(latest["fundingRate"]),
        "fundingTime": latest["fundingTime"],
        "fetchedAt": datetime.utcnow().isoformat()
    }

def main():
    print(f"Tracking funding rate for {SYMBOL} every {SLEEP_SECONDS}s")

    while True:
        try:
            rate_data = get_funding_rate()

            if rate_data:
                line = json.dumps(rate_data)

                print(
                    f"[{rate_data['fetchedAt']}] "
                    f"{rate_data['fundingRate']}"
                )

                with open(OUTPUT_FILE, "a") as f:
                    f.write(line + "\n")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(SLEEP_SECONDS)

if __name__ == "__main__":
    main()
