import csv

input_file = 'C:/Premier League Analysis/Python Scripts/attredone.csv'
output_file = 'C:/Premier League Analysis/Python Scripts/attredone_cleaned.csv'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    headers = next(reader)
    writer.writerow(headers)  # Write the header row

    for row in reader:
        # Clean the attendance column (assuming it is the 5th column, index 4)
        if row[4] != '':
            row[4] = row[4].replace(',', '')  # Remove commas from the attendance field
        writer.writerow(row)
