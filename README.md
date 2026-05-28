# Binance Funding Tracker

Fetches the latest funding rate for BTCUSDT from Binance Futures API every 60 seconds and appends it to a JSON lines file.

## Why
- Demonstrates working with a public REST API
- Basic data persistence (append-only logging)
- Readable, minimal code

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run: `python funding_tracker.py`
3. Stop with `Ctrl+C`. Data is logged in `funding_rates.jsonl`.

## Entry point
The script uses the standard Python `if __name__ == "__main__"` guard, so it can be executed directly or imported cleanly in other modules without side effects.

## Sample Output

[2025-01-15T12:00:01] 0.0001
[2025-01-15T12:01:01] 0.00015

### Terminal screenshot
<!-- Add your own screenshot or GIF here -->
![Funding tracker terminal](screenshots/funding_tracker.png)

## Limitations
- No API key needed (public endpoint)
- Basic error handling; not intended for production without additional guards

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

