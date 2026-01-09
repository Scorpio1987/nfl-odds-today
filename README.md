# NFL Odds Today 🏈

A simple CLI tool to fetch and display today's NFL betting odds using [The Odds API](https://the-odds-api.com/).

## Features

- 📊 Fetches moneyline, spread, and totals odds
- 🏆 Highlights best odds across bookmakers
- 📈 Tracks API usage
- 🇺🇸 US bookmakers (FanDuel, DraftKings, BetMGM, etc.)

## Prerequisites

1. **Python 3.8+**
2. **API Key** from [The Odds API](https://the-odds-api.com/) (free tier available)

## Installation

```bash
# Clone the repository
git clone https://github.com/Scorpio1987/nfl-odds-today.git
cd nfl-odds-today

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Set your API key
export ODDS_API_KEY="your_api_key_here"

# Run the script
python main.py
```

## Example Output

```
======================================================================
🏈 NFL ODDS TODAY
   Sunday, January 08, 2026 at 10:30 AM
======================================================================

⏳ Fetching NFL odds...

📈 API Usage: 1 used, 499 remaining

✅ Found 14 NFL games with odds:

──────────────────────────────────────────────────────────────────────
🏈 Dallas Cowboys @ Philadelphia Eagles
   Kickoff: 01:00 PM EST

   📊 BEST ODDS:

   Moneyline:
      Dallas Cowboys: +165 (fanduel)
      Philadelphia Eagles: -195 (draftkings)

   Spread:
      Dallas Cowboys +4.5: -110 (betmgm)
      Philadelphia Eagles -4.5: -108 (fanduel)

   Total:
      Over 48.5: -110 (draftkings)
      Under 48.5: -108 (fanduel)

======================================================================
Data provided by The Odds API (https://the-odds-api.com/)
======================================================================
```

## API Usage

The free tier of The Odds API includes 500 requests per month. Each run of this script uses 1 request.

## Dependencies

- [odds-api-client](https://github.com/Scorpio1987/odds-api-client) - Python client for The Odds API

## License

MIT License
