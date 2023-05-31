import csv

filename = 'data.csv'

# Open the file in read mode
with open(filename, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Read the CSV data row by row
    for row in reader:
        # Print each row
        print(', '.join(row))
