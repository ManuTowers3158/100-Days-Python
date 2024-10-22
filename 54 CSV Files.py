import csv  # Import the CSV module for handling CSV files

total = 0.0  # Initialize a variable to store the total

# Open the CSV file for reading
with open("Support Files/Costs.csv") as file:
    reader = csv.DictReader(file)  # Create a CSV DictReader object to read rows as dictionaries
    for row in reader:
        print(row["Net Total"])  # Print the "Net Total" for each row
        total += float(row["Net Total"])  # Add the "Net Total" to the overall total

print(f"Total: {total}")  # Print the final total
