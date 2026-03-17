from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Subtract five days from the current date
five_days_ago = today - timedelta(days=5)

# Print the result
print("Today's date:", today.strftime('%Y-%m-%d'))
print("Five days ago:", five_days_ago.strftime('%Y-%m-%d'))

#2
from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Print the results
print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
print("Today:", today.strftime('%Y-%m-%d'))
print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))

#3
from datetime import datetime

# Get current datetime
now = datetime.now()

# Drop microseconds
now_without_microseconds = now.replace(microsecond=0)

# Print the result
print("Current datetime:", now)
print("Datetime without microseconds:", now_without_microseconds)


#4
from datetime import datetime

# Define two dates
date1 = datetime(2026, 2, 25, 12, 0, 0)  # Example date
date2 = datetime(2026, 2, 24, 12, 0, 0)  # Another example date

# Calculate the difference in seconds
time_difference = (date1 - date2).total_seconds()

# Print the result
print(f"The difference between the two dates is {time_difference} seconds.")