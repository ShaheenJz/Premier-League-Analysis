import csv
from datetime import datetime
import re

# List of date strings in the given format
dates = [
    "28th May 2023", "28th May 2023", "28th May 2023", "28th May 2023",
    "28th May 2023", "28th May 2023", "28th May 2023", "28th May 2023",
    "28th May 2023", "28th May 2023", "25th May 2023", "24th May 2023",
    "22nd May 2023", "21st May 2023", "21st May 2023", "21st May 2023",
    "20th May 2023", "20th May 2023", "20th May 2023", "20th May 2023",
    "20th May 2023", "20th May 2023", "18th May 2023", "15th May 2023",
    "14th May 2023", "14th May 2023", "14th May 2023", "13th May 2023",
    "13th May 2023", "13th May 2023", "13th May 2023", "13th May 2023",
    "13th May 2023", "8th May 2023", "8th May 2023", "8th May 2023",
    "7th May 2023", "7th May 2023", "6th May 2023", "6th May 2023",
    "6th May 2023", "6th May 2023", "6th May 2023", "4th May 2023",
    "3rd May 2023", "3rd May 2023", "2nd May 2023", "1st May 2023",
    "30th April 2023", "30th April 2023", "30th April 2023", "30th April 2023",
    "30th April 2023", "29th April 2023", "29th April 2023", "29th April 2023",
    "27th April 2023", "27th April 2023", "27th April 2023", "26th April 2023",
    "26th April 2023", "26th April 2023", "26th April 2023", "25th April 2023",
    "25th April 2023", "25th April 2023", "23rd April 2023", "23rd April 2023",
    "22nd April 2023", "22nd April 2023", "22nd April 2023", "22nd April 2023",
    "21st April 2023", "17th April 2023", "16th April 2023", "16th April 2023",
    "15th April 2023", "15th April 2023", "15th April 2023", "15th April 2023",
    "15th April 2023", "15th April 2023", "15th April 2023", "9th April 2023",
    "9th April 2023", "8th April 2023", "8th April 2023", "8th April 2023",
    "8th April 2023", "8th April 2023", "8th April 2023", "8th April 2023",
    "8th April 2023", "5th April 2023", "5th April 2023", "4th April 2023",
    "4th April 2023", "4th April 2023", "4th April 2023", "3rd April 2023",
    "2nd April 2023", "2nd April 2023", "1st April 2023", "1st April 2023",
    "1st April 2023", "1st April 2023", "1st April 2023", "1st April 2023",
    "1st April 2023", "19th March 2023", "18th March 2023", "18th March 2023",
    "18th March 2023", "18th March 2023", "18th March 2023", "17th March 2023",
    "15th March 2023", "15th March 2023", "12th March 2023", "12th March 2023",
    "12th March 2023", "12th March 2023", "11th March 2023", "11th March 2023",
    "11th March 2023", "11th March 2023", "11th March 2023", "11th March 2023",
    "6th March 2023", "5th March 2023", "5th March 2023", "4th March 2023",
    "4th March 2023", "4th March 2023", "4th March 2023", "4th March 2023",
    "4th March 2023", "4th March 2023", "1st March 2023", "1st March 2023",
    "26th February 2023", "25th February 2023", "25th February 2023",
    "25th February 2023", "25th February 2023", "25th February 2023",
    "25th February 2023", "24th February 2023", "19th February 2023",
    "19th February 2023", "18th February 2023", "18th February 2023",
    "18th February 2023", "18th February 2023", "18th February 2023",
    "18th February 2023", "18th February 2023", "18th February 2023",
    "15th February 2023", "13th February 2023", "12th February 2023",
    "12th February 2023", "11th February 2023", "11th February 2023",
    "11th February 2023", "11th February 2023", "11th February 2023",
    "11th February 2023", "11th February 2023", "8th February 2023",
    "5th February 2023", "5th February 2023", "4th February 2023",
    "4th February 2023", "4th February 2023", "4th February 2023",
    "4th February 2023", "4th February 2023", "4th February 2023",
    "3rd February 2023", "23rd January 2023", "22nd January 2023",
    "22nd January 2023", "22nd January 2023", "21st January 2023",
    "21st January 2023", "21st January 2023", "21st January 2023",
    "21st January 2023", "21st January 2023", "19th January 2023",
    "18th January 2023", "15th January 2023", "15th January 2023",
    "15th January 2023", "14th January 2023", "14th January 2023",
    "14th January 2023", "14th January 2023", "14th January 2023",
    "14th January 2023", "13th January 2023", "12th January 2023",
    "5th January 2023", "4th January 2023", "4th January 2023",
    "4th January 2023", "4th January 2023", "3rd January 2023",
    "3rd January 2023", "3rd January 2023", "2nd January 2023",
    "1st January 2023", "1st January 2023", "31st December 2022",
    "31st December 2022", "31st December 2022", "31st December 2022",
    "31st December 2022", "31st December 2022", "30th December 2022",
    "30th December 2022", "28th December 2022", "27th December 2022",
    "27th December 2022", "26th December 2022", "26th December 2022",
    "26th December 2022", "26th December 2022", "26th December 2022",
    "26th December 2022", "26th December 2022", "13th November 2022",
    "13th November 2022", "12th November 2022", "12th November 2022",
    "12th November 2022", "12th November 2022", "12th November 2022",
    "6th November 2022", "6th November 2022", "6th November 2022",
    "6th November 2022", "6th November 2022", "5th November 2022",
    "5th November 2022", "5th November 2022", "5th November 2022",
    "5th November 2022", "30th October 2022", "30th October 2022",
    "29th October 2022", "29th October 2022", "29th October 2022",
    "29th October 2022", "29th October 2022", "29th October 2022",
    "29th October 2022", "29th October 2022", "24th October 2022",
    "23rd October 2022", "23rd October 2022", "23rd October 2022",
    "23rd October 2022", "23rd October 2022", "22nd October 2022",
    "22nd October 2022", "22nd October 2022", "22nd October 2022",
    "20th October 2022", "20th October 2022", "19th October 2022",
    "19th October 2022", "19th October 2022", "19th October 2022",
    "19th October 2022", "18th October 2022", "18th October 2022",
    "16th October 2022", "16th October 2022", "16th October 2022",
    "16th October 2022", "16th October 2022", "15th October 2022",
    "15th October 2022", "15th October 2022", "15th October 2022",
    "14th October 2022", "10th October 2022", "9th October 2022",
    "9th October 2022", "9th October 2022", "9th October 2022",
    "8th October 2022", "8th October 2022", "8th October 2022",
    "8th October 2022", "8th October 2022", "3rd October 2022",
    "2nd October 2022", "2nd October 2022", "1st October 2022",
    "1st October 2022", "1st October 2022", "1st October 2022",
    "1st October 2022", "1st October 2022", "1st October 2022",
    "18th September 2022", "18th September 2022", "17th September 2022",
    "17th September 2022", "17th September 2022", "16th September 2022",
    "16th September 2022", "4th September 2022", "4th September 2022",
    "3rd September 2022", "3rd September 2022", "3rd September 2022",
    "3rd September 2022", "3rd September 2022", "3rd September 2022",
    "3rd September 2022", "1st September 2022", "31st August 2022",
    "31st August 2022", "31st August 2022", "31st August 2022",
    "31st August 2022", "30th August 2022", "30th August 2022",
    "30th August 2022", "28th August 2022", "28th August 2022",
    "28th August 2022", "27th August 2022", "27th August 2022",
    "27th August 2022", "27th August 2022", "27th August 2022",
    "27th August 2022", "27th August 2022", "21st August 2022",
    "21st August 2022", "21st August 2022", "20th August 2022",
    "20th August 2022", "20th August 2022", "20th August 2022",
    "20th August 2022", "20th August 2022", "15th August 2022",
    "14th August 2022", "14th August 2022", "13th August 2022",
    "13th August 2022", "13th August 2022", "13th August 2022",
    "13th August 2022", "13th August 2022", "13th August 2022",
    "7th August 2022", "7th August 2022", "7th August 2022",
    "6th August 2022", "6th August 2022", "6th August 2022",
    "6th August 2022", "6th August 2022", "6th August 2022", "5th August 2022"
]

def convert_date(date_str):
    # Define regex pattern to extract day, month, and year
    pattern = r"(\d+)(?:st|nd|rd|th) (\w+) (\d{4})"
    match = re.match(pattern, date_str)
    
    if match:
        day, month, year = match.groups()
        # Convert month name to month number
        month_number = datetime.strptime(month, "%B").month
        # Format the date as DD/MM/YY
        formatted_date = datetime(int(year), month_number, int(day)).strftime("%d/%m/%y")
        return formatted_date
    else:
        return None

# Convert all dates
converted_dates = [convert_date(date) for date in dates]

# Write the converted dates to a CSV file
with open('Z:\Docs\HDD Documents\SQL Project\converted_dates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date'])  # Write header
    for date in converted_dates:
        writer.writerow([date])

print("Dates have been written to 'converted_dates.csv'")
