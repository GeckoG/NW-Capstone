import requests
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Define the base URL pattern
base_url = "https://ks.milesplit.com/rankings/events/high-school-{}/outdoor-track-and-field/{}?year={}&accuracy=fat&league={}&page={}"

# Define the parameters to iterate over
gender_groups = ['girls', 'boys']
event_groups = ['100m', '200m', '400m', '800m', '1600m', '3200m', 'LJ', 'TJ','HJ','PV','S','D','J']  # Add other events as needed
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2021, 2022, 2023]
league_ids = [4735, 4742, 4745]  # Adjust this based on the desired league IDs
max_pages = 2  # Maximum number of pages to scrape

driver = webdriver.Firefox()

# Define the credentials for signing in
username = "mattgoeckel13@gmail.com"
password = "Eequalsmc^2"

# Load the sign-in page
driver.get("https://ks.milesplit.com/login")

# Wait for the sign-in page to load
time.sleep(2)

# Find the username and password fields and enter the credentials
username_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(username)
password_field.send_keys(password)

# Submit the sign-in form
password_field.send_keys(Keys.RETURN)
time.sleep(5)

workbook = load_workbook('Data.xlsx')
ws = workbook.active

# Iterate over gender, event, year, league ID, and page number combinations
for gender in gender_groups:
    for event in event_groups:
        for year in years:
            for league_id in league_ids:
                for page_num in range(1, max_pages + 1):
                    # Generate URL
                    url = base_url.format(gender, event, year, league_id, page_num)
                    print(url)
                    # Fetch the page content
                    driver.get(url)
                    time.sleep(3)
                    response = driver.page_source

                    soup = BeautifulSoup(response, 'html.parser')
                    # Process the page content
                    # Example: Extract data from the page
                    table = soup.find("table")

                    for row in table.find_all("tr"):
                        # Extract data from each cell in the row
                        cells = row.find_all("td")
                        if cells:  # Check if row is not empty
                        # Append data from each cell to a list
                            row_data = [cell.text.strip() for cell in cells]
                            rank = row.find('td', class_='rank').text.strip()
                            mark = row.find('td', class_='time').text.strip()
                            athlete = row.find('div', class_='athlete').text.strip()
                            team = row.find('div', class_='team').text.strip()
                            location = row.find('div', class_='meet').text.strip().split('\n')[0]
                            date = row.find('time', class_='start').text.strip()
                            division = ""
                            if league_id == 4735:
                                division = "Kansas 1A"
                            elif league_id == 4742:
                                division = "Kansas 3A"
                            elif league_id == 4745:
                                division = "Kansas 6A"
                            insertable_data = [rank, mark, athlete, gender, team, division, event, location, date]
                            print(insertable_data)
                            ws.append(insertable_data)
                        else:
                            print(f"Failed to fetch URL: {url}")
driver.quit()
workbook.save('Data.xlsx')