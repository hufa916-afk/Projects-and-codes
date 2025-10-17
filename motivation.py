import random
import datetime
import os

# List of motivational quotes
quotes = [
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Don't watch the clock; do what it does. Keep going.",
    "Dream it. Wish it. Do it.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you."
]

# Check current time
now = datetime.datetime.now()
if now.hour == 11 and now.minute == 0:
    quote = random.choice(quotes)
    
    # macOS
    os.system(f'say "{quote}"')
