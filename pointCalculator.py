import json
import openpyxl

# Load the JSON file
with open('data.json') as f:
    data = json.load(f)

# Load the Excel file
workbook = openpyxl.load_workbook('Cleaned-Data.xlsx')
sheet = workbook.active

# Iterate through rows
for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming data starts from row 2
    sex = row[3]  # Pull the sex from column D
    event = row[6]  # Pull the event from column G
    result = row[1] # Pull the result from column B


    # Access the data using keys from the Excel file
    if sex in data and event in data[sex]:
        coeffs = data[sex][event]
        resultShift = coeffs["resultShift"]
        conversionFactor = coeffs["conversionFactor"]
        pointShift = coeffs["pointShift"]

        # Calculating the score
        score = (conversionFactor * (result + resultShift)^2 + pointShift)

        # Write the score to column K
        sheet.cell(row=row[0], column=11).value = score  # Column K corresponds to index 11 (Python uses 0-based indexing)

    else:
        print(f"Data not found for {sex} {event}")

# Save the modified Excel file
workbook.save('Cleaned-Data-modified.xlsx')
