import csv

input_file = "data.csv"
output_file = "cleaned_data.csv"

with open(input_file, newline="", mode="r") as infile:
    reader = csv.reader(infile)
    rows = [row for row in reader if any(row)]

with open(output_file, newline="", mode="w") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)

print("CSV file cleaned successfully.")
