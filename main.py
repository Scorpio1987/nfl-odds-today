#!/usr/bin/env python3
"""
NFL Odds Today - Fetch today's NFL moneyline odds.

Usage:
    export ODDS_API_KEY="your_api_key"
    python main.py
"""

import os
import sys
from datetime import datetime, timezone
from typing import List

from odds_api import (
    OddsAPIClient,
    Sports,
    Regions,
    Markets,
    OddsFormat,
    EventOdds,
    AuthenticationError,
    OddsAPIError,
)


def print_header():
    """Print application header."""
    print("\n" + "=" * 60)
    print("🏈 NFL MONEYLINE ODDS TODAY")
    print(f"   {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}")
    print("=" * 60)


def print_event_odds(event: EventOdds):
    """Print moneyline odds for a single event."""
    print(f"\n{'─' * 60}")
    print(f"🏈 {event.away_team} @ {event.home_team}")
    print(f"   Kickoff: {event.commence_time.strftime('%I:%M %p')}")
    
    if not event.bookmakers:
        print("   No odds available")
        return
    
    # Get best moneyline odds
    best_odds = event.get_best_odds("h2h")
    
    if best_odds:
        print("\n   📊 BEST MONEYLINE ODDS:")
        for team, (price, bookmaker) in best_odds.items():
            print(f"      {team}: {price:.2f} ({bookmaker})")
    
    # Show odds from each bookmaker
    print("\n   📚 ALL BOOKMAKERS:")
    for bookmaker in event.bookmakers:
        for market in bookmaker.markets:
            if market.key == "h2h":
                odds_str = " | ".join(
                    f"{o.name}: {o.price:.2f}" for o in market.outcomes
                )
                print(f"      {bookmaker.title}: {odds_str}")


def fetch_nfl_odds() -> List[EventOdds]:
    """Fetch NFL moneyline odds from The Odds API."""
    api_key = os.environ.get("ODDS_API_KEY")
    
    if not api_key:
        print("\n❌ ERROR: ODDS_API_KEY environment variable not set!")
        print("\nTo get an API key:")
        print("  1. Visit https://the-odds-api.com/")
        print("  2. Sign up for a free account")
        print("  3. Set the environment variable:")
        print("     export ODDS_API_KEY='your_api_key_here'")
        sys.exit(1)
    
    try:
        client = OddsAPIClient(api_key=api_key)
        
        # Fetch NFL moneyline odds only
        odds = client.get_odds(
            sport_key=Sports.NFL,
            regions=Regions.US,
            markets=Markets.HEAD_TO_HEAD,  # Moneyline only
            odds_format=OddsFormat.DECIMAL,
        )
        
        # Print API usage
        if client.usage:
            print(f"\n📈 API Usage: {client.usage.requests_used} used, "
                  f"{client.usage.requests_remaining} remaining")
        
        client.close()
        return odds
        
    except AuthenticationError:
        print("\n❌ ERROR: Invalid API key!")
        print("Please check your ODDS_API_KEY environment variable.")
        sys.exit(1)
    except OddsAPIError as e:
        print(f"\n❌ API Error: {e}")
        sys.exit(1)


def main():
    """Main entry point."""
    print_header()
    
    print("\n⏳ Fetching NFL moneyline odds...")
    odds = fetch_nfl_odds()
    
    if not odds:
        print("\n📭 No NFL games scheduled.")
        return
    
    print(f"\n✅ Found {len(odds)} NFL games:")
    
    for event in odds:
        print_event_odds(event)
    
    print("\n" + "=" * 60)
    print("Data provided by The Odds API (https://the-odds-api.com/)")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
