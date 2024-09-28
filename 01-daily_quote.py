#!/usr/bin/env python3
# Mihir Kalyanthaya
# 9/28/24
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "'Be yourself; everyone else is already taken.'",
    "'Be the change that you wish to see in the world.'",
    "'If you tell the truth, you don't have to remember anything.'",
    "'The only thing we have to fear is fear itself.'"
]

def get_quote_of_the_day(quotes):
    todays_quote = None
    todays_quote = random.choice(quotes) 
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))
    print(f"{date.today()}: {get_quote_of_the_day(quotes)}")
# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt 
# WSL Terminal Cron job
0 8 * * * /usr/bin/python3 "C:\Users\mihir\OneDrive\Desktop\01-daily_quote.py" >> "C:\Users\mihir\OneDrive\Desktop\daily_quote.txt" 2>&1
