import csv
def get_header(file_path):
    
    try:
        with open(file_path, mode = 'r', newline = '') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            return header
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
file_path = r'C:\Premier League Analysis\Python Scripts\matches.csv'

header = get_header(file_path)
data_type = {}

# Ask for data types for each column header
for x in header:
    data_type[x] = input(f"What is the data type for the column: {x}? ")

# Start building the CREATE TABLE statement
creator = "CREATE TABLE refgames (id SERIAL PRIMARY KEY, "

# Add each column and its data type to the statement
for y in header:
    creator += f"{y} {data_type[y]}, "

# Remove the trailing comma and space, then close the statement
creator = creator.rstrip(", ") + ");"

print(creator)
