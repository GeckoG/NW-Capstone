import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

# URL of the page containing the information
#url = 'https://tf.tfrrs.org/list_data/4045?other_lists=https%3A%2F%2Fupload.tfrrs.org%2Flists%2F4045%2F2023_NCAA_Division_II_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender='

urls = [
    #'https://tf.tfrrs.org/list_data/4517?other_lists=https%3A%2F%2Ftf.tfrrs.org%2Flists%2F4517%2F2024_NCAA_Division_III_Outdoor_Qualifying_List&limit=100&event_type=&year=&gender=',
    'https://tf.tfrrs.org/list_data/4043?other_lists=https%3A%2F%2Fapi.tfrrs.org%2Flists%2F4043%2F2023_NCAA_Division_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://api.tfrrs.org/list_data/3714?other_lists=https%3A%2F%2Fwww.tfrrs.org%2Flists%2F3714%2F2022_NCAA_Division_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://www.tfrrs.org/list_data/3195?other_lists=https%3A%2F%2Ftf.tfrrs.org%2Flists%2F3195%2F2021_NCAA_Division_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://tf.tfrrs.org/list_data/2907?other_lists=https%3A%2F%2Ftf.tfrrs.org%2Flists%2F2907%2F2020_NCAA_Div_III_Outdoor_Qualifying&limit=100&event_type=&year=&gender=',
    'https://tf.tfrrs.org/list_data/2572?other_lists=https%3A%2F%2Fm.tfrrs.org%2Flists%2F2572%2F2019_NCAA_Div_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://m.tfrrs.org/list_data/2283?other_lists=https%3A%2F%2Fm.tfrrs.org%2Flists%2F2283%2F2018_NCAA_Div_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://m.tfrrs.org/list_data/1914?other_lists=https%3A%2F%2Fwww.tfrrs.org%2Flists%2F1914%2F2017_NCAA_Div_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://www.tfrrs.org/list_data/1684?other_lists=https%3A%2F%2Fwww.tfrrs.org%2Flists%2F1684%2F2016_NCAA_Division_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://www.tfrrs.org/list_data/1443?other_lists=https%3A%2F%2Fwww.tfrrs.org%2Flists%2F1443%2F2015_NCAA_Division_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://www.tfrrs.org/list_data/1232?other_lists=https%3A%2F%2Fwww.tfrrs.org%2Flists%2F1232%2F2014_NCAA_Division_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://www.tfrrs.org/list_data/1033?other_lists=https%3A%2F%2Fwww.tfrrs.org%2Flists%2F1033%2F2013_NCAA_Division_III_Outdoor_Qualifying_FINAL&limit=100&event_type=&year=&gender=',
    'https://www.tfrrs.org/list_data/842?other_lists=https%3A%2F%2Fwww.tfrrs.org%2Flists%2F842%2F2012_NCAA_Div_III_Outdoor_Qualifier_List&limit=100&event_type=&year=&gender=',
    'https://www.tfrrs.org/list_data/675?other_lists=https%3A%2F%2Fwww.tfrrs.org%2Flists%2F675%2F2011_NCAA_Division_III_Outdoor_POP_List_FINAL&limit=100&event_type=&year=&gender=',
    'https://www.tfrrs.org/list_data/530?other_lists=https%3A%2F%2Ftf.tfrrs.org%2Flists%2F530%2F2010_NCAA_Division_III_Outdoor_Track__Field&limit=100&event_type=&year=&gender=',
]
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # List of div classes for different events, replace these with the actual classes you're interested in
    event_divs = [
        "row gender_m standard_event_hnd_6",  # Men's 100m
        "row gender_f standard_event_hnd_6",  # Women's 100m
        "row gender_m standard_event_hnd_7",  # Men's 200m
        "row gender_f standard_event_hnd_7",  # Women's 200m
        "row gender_m standard_event_hnd_11",  # Men's 400m
        "row gender_f standard_event_hnd_11",  # Women's 400m
        "row gender_m standard_event_hnd_12",  # Men's 800m
        "row gender_f standard_event_hnd_12",  # Women's 800m
        "row gender_m standard_event_hnd_13",  # Men's 1500m
        "row gender_f standard_event_hnd_13",  # Women's 1500m
        "row gender_m standard_event_hnd_21",  # Men's 5000m
        "row gender_f standard_event_hnd_21",  # Women's 5000m
        "row gender_m standard_event_hnd_22",  # Men's 10000m
        "row gender_f standard_event_hnd_22",  # Women's 10000m
        "row gender_m standard_event_hnd_23",  # Men's HJ
        "row gender_f standard_event_hnd_23",  # Women's HJ
        "row gender_m standard_event_hnd_24",  # Men's PV
        "row gender_f standard_event_hnd_24",  # Women's PV
        "row gender_m standard_event_hnd_25",  # Men's LJ
        "row gender_f standard_event_hnd_25",  # Women's LJ
        "row gender_m standard_event_hnd_26",  # Men's TJ
        "row gender_f standard_event_hnd_26",  # Women's TJ
        "row gender_m standard_event_hnd_27",  # Men's Discus
        "row gender_f standard_event_hnd_27",  # Women's Discus
        #"row gender_m standard_event_hnd_28",  # Men's Hammer
        #"row gender_f standard_event_hnd_28",  # Women's Hammer
        "row gender_m standard_event_hnd_29",  # Men's Javelin
        "row gender_f standard_event_hnd_29",  # Women's Javelin
        "row gender_m standard_event_hnd_30",  # Men's Shot
        "row gender_f standard_event_hnd_30",  # Women's Shot
    ]

    # Create a new Excel workbook
    wb = load_workbook(filename='Data.xlsx')
    division = "NCAA D-III"

    for event_div_class in event_divs:
        # Find the div containing the event
        event_div = soup.find("div", class_=lambda x: x and x == event_div_class)
        if event_div:
            # Extract the event name (assuming it's within an <h3> tag inside our div)
            # Extract the event name and sex
            event, sex = event_div.find("h3").text.strip().split("\n")

            # Remove leading and trailing whitespace
            event = event.strip()
            sex = sex.strip("() ").capitalize()
            #print(event)
            #print(sex)
            # Create a new sheet in the workbook for this event
            ws = wb.active

            # Find the table within the event div
            table = event_div.find("table")

            # Check if table is found
            if table:
                # Extract and write header row to the sheet
                headers = [header.text.strip() for header in table.find_all("th")]

                # Iterate through rows of the table
                for row in table.find_all("tr"):
                    # Extract data from each cell in the row
                    cells = row.find_all("td")
                    if cells:  # Check if row is not empty
                        # Append data from each cell to a list
                        row_data = [cell.text.strip() for cell in cells]
                        rank = row_data[0]
                        athlete = row_data[1]
                        team = row_data[3]
                        mark = row_data[4]
                        if event == "High Jump" or event == "Pole Vault" or event == "Long Jump" or event == "Triple Jump" or event == "Javelin" or event == "Discus" or event == "Shot Put" or event == "Hammer":
                            location = row_data[6]
                            date = row_data[7]
                        else:
                            location = row_data[5]
                            date = row_data[6]
                        insertable_data = [rank, mark, athlete, sex, team, division, event, location, date]
                        print(insertable_data)
                        # Write row_data to the Excel worksheet
                        ws.append(insertable_data)
    # Save the workbook to a file, make sure the filename doesn't contain invalid characters for an Excel sheet name
    wb.save('Data.xlsx')
    print("Saved")