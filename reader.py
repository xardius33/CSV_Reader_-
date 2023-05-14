import csv

def read_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

# Usage
file_path = 'data.csv'  # Replace with your CSV file path
read_csv(file_path)
