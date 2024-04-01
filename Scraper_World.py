import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

# Define the base URL pattern
base_url = "https://worldathletics.org/records/toplists/{}/{}/{}/senior/{}"

# Define the gender and event groups to iterate over
gender_groups = ['women', 'men']
event_groups = ['sprints/100-metres',
                'sprints/200-metres',
                'sprints/400-metres',
                'middlelong/800-metres',
                'middlelong/1500-metres',
                'middlelong/5000-metres',
                'middlelong/10000-metres',
                'jumps/high-jump',
                'jumps/pole-vault',
                'jumps/long-jump',
                'jumps/triple-jump',
                'throws/shot-put',
                'throws/discus-throw',
                'throws/javelin-throw']  # Add other event groups as needed

# Define the range of years to iterate over
start_year = 2010
end_year = 2023

workbook = load_workbook('Data.xlsx')
ws = workbook.active

# Iterate over gender, event, and year combinations
for gender in gender_groups:
    for event in event_groups:
        for year in range(start_year, end_year + 1):
            # Construct the URL
            url = base_url.format(event, 'all', gender, year)
            
            # Fetch the page content
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Process the page content as needed
                sex = gender.capitalize()
                eventname = event.split('/')[-1].replace('-', ' ').capitalize()
                division = "World"

                table = soup.find("table", class_="records-table")
                # Example: Print the URL for demonstration
                print(url)
                # Example: Extract data from the page
                for row in table.find_all("tr"):
                    # Extract data from each cell in the row
                    cells = row.find_all("td")
                    if cells:  # Check if row is not empty
                        # Append data from each cell to a list
                        row_data = [cell.text.strip() for cell in cells]
                        rank = row_data[0]
                        athlete = row_data[3]
                        team = row_data[5]
                        mark = row_data[1]
                        location = row_data[8]
                        date = row_data[9]
                        insertable_data = [rank, mark, athlete, sex, team, division, eventname, location, date]
                        print(insertable_data)
                        ws.append(insertable_data)
                
            else:
                print(f"Failed to fetch URL: {url}")

workbook.save('Data.xlsx')