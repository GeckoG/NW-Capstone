# Variance and Trajectory of Collective Performance Advancements across Track and Field Disciplines

## In this Repository

This repository is part of a larger project for the NWMSU Data Analytics Capstone. Full project information is available below in this README.md. The official final report is available on [Overleaf](www.overleaf.com)

Below is an explanation of each file (in chronological order) and its relation to the project:

### Data Collection
- **requirements.txt** - The required python packages for this project
- **Scraper_D1.py** - Takes NCAA-D1 performances from TFRRS.com and adds them to the dataset
- **Scraper_D2.py** - Scraper_D1.py but for Division II
- **Scraper_D3.py** - Scraper_D1.py but for Division III
- **Scraper_NAIA.py** - Scraper_D1.py but for NAIA
- **Scraper_HS.py** - Adds Kansas HS performances from MileSplit.com to the dataset
- **Scraper_World.py** - Adds performances from the World Athletics Global Leaderboard to the dataset
- **Data.xlsx** - The full spreadsheet of all the raw, scraped data.

### Data Cleaning & Manipulation
- **Cleaned_Data.xlsx** - Dataset after basic cleaning
- **Cleaned_Data.csv** - Cleaned_Data.xlsx converted to csv
- **pointCalculator.py** - Adds a feature of World Athletics points to each performance
- **coefficients.json** - Required constants for pointCalculator.py
- **top100avg_calculator.py** - Creates a separate dataset of top-100 averages for each gender/event/year
- **top100avg.csv** - The dataset produced by top100avg_calculator.py

### Notebooks
- **EDA.ipynb** - Exploratory data analysis (Initial graphing)
- **models.ipynb** - Model building, training, and selection
- **presentation.ipynb** - Organized presentation of results

## Project Introduction

The goal of this project is to find trends in the top-100 performances of each year across various track and field events. Ultimately, a model was created to forecast the top-100 average for future years. There were several steps to this project, each of which encompassed one or more of the NWMSU Data Analytics program objectives. The process was as follows:

1. Scrape the data from results databases on the internet
2. Clean the data into 
3. Exploratory Data Analysis
4. Statistical analysis & manipulation
5. Model Building
6. Calculating Results



### Related Works

Several previous projects & studies have been conducted that are similar in nature to this one. However, none have been as comprehensive as this. Some have studied explicitly the [advancement of records](link) or the single top time each year, but the outliers at the top do not represent the sport as a whole. Others have used the top-100 performances, but [focused on a single event group](link), like sprints, and covered a shorter period of time. Lastly, similar sports, such as swimming, [have created similar datasets](link), but aimed to answer different questions in their studies.

## Dataset Information

The dataset consists of performances from:

- [MileSplit.com](ks.milesplit.com/results) - A website with a database of High School results
- [TFRRS.org](tfrrs.org) - The college Track & Field Results Reporting System
- [WorldAthletics.org](worldathletics.org/records/toplists) - The governing body of Track & Field

Each website provided data for various divisions of the sport, allowing us to see data and trends from every level of the sport, from beginner experience to Olympic competition.

| Division      | Website         | Notes |
|---------------|-----------------|-------|
| Kansas 1A     | MileSplit       | Extra Small High Schools (<100 Students)
| Kansas 3A     | MileSplit       | Small High Schools (200-400 Students)
| Kansas 6A     | MileSplit       | Large High Schools (1500+ Students)
| NAIA          | TFRRS           | Non-NCAA Colleges, Generally Less Competitive
| NCAA D-III    | TFRRS           | Non-Scholarship Colleges
| NCAA D-II     | TFRRS           | Middle Competitive Level of College
| NCAA D-I      | TFRRS           | Highest Competitive Level of College
| World         | World Athletics | Professional Athletes

For each division, 14 events were scraped:

- 100m
- 200m
- 400m
- 800m
- 1500m (1600m for HS)
- 5000m (3200m for HS)
- 10000m (HS not Included)
- Long Jump
- Triple Jump
- High Jump
- Pole Vault
- Shot Put
- Discus
- Javelin

The raw dataset included 8 fetures, shown in the example below:

| Rank | Performance | Name         | Team        | Division | Event | Location/Meet      | Date      |
|------|-------------|--------------|-------------|----------|-------|--------------------|-----------|
| 19   | 1:55.52     | Matt Goeckel | NW Missouri | NCAA-DII | 800m  | Concordia Twilight | 5/13/2022 | 

### Limitations

- No unofficial or time-trial results were included. Only official performances from each website were scraped.

- Only wind-legal marks were taken from TFRRS and WA. However, most MileSplit marks did not come with wind readings. All marks without a reading were accepted. Of the marks with a recorded wind reading, only the legal ones were accepted.

-  TFRRS does not include marks from the National Championships, Olympic Trials, or Olympics on their lists, even if the athlete competed there. This likely skews ALL collegiate averages down.

- The high school divisions are only one subset of one state, while colleges are nationwide, and the global leaderboard includes every country. It is important to understand the varying scopes when viewing across divisions. Large gaps between divisions are expected. Likely exascerbating the competitive gap between High School/College and College/Professional.

## Data Curation & Preparation

There were several points of emphasis to clean before the dataset was usable:

- Some TFRRS data points included an @ symbol to indicate an altitude conversion. This needed to be removed.
- MileSplit field events were recorded in Feet-Inches (Ex. 14-9.25) and needed to be converted to Meters.
- MileSplit used "Boys" and "Girls" instead of "Men" and "Women". This needed changed.
- TFRRS and World Athletics added "Throw" to the end of "Discus" and "Javelin". This needed removed.
- World Athletics formatted it's events like this: "100 metres", and TFRRS like this: "100 Meters". This was changed to match MileSplits "100m"
- All 3 websites used a different date format. This needed to be standardized.
- Times are in MM:SS.ss format, but needed to be converted to only seconds for easier math.

Analysis on Names, Teams, and Location was not done, but if it were, the following cleaning would have also been required:

- World Athletics country codes must be converted to country names
- TFRRS naming is (Last, First), MileSplit is (First Last), and World Athletics is (First LAST). This would need standardized.
- MileSplit & TFRRS use meet name instead of location. This would need changed.

### World Athletics Points

Comparing performances across events has always been a topic in Track & Field. For the purposes of this project, comparison of performances across events would make the analysis *much* easier. Luckily, World Athletics provides a points system, scaled to each event from 0 to 1400, with 1400 being the pinnacle of human achievement. The scale is updated every 4 years to account for changes within the sport. The most recent update was in 2022.

World Athletics does not provide an equation for points calculations, but instead provides a [table](link) in pdf format. Luckily, former work on [this page](link) provides the equations, and [their corresponding repo](link) provides the equation's 2022 coefficients for each event. Using these, the pointCalculator.py file was created, adding a 9th feature to the dataset: Points.

### Top 100 Average Dataset

Lastly, it was time to create a top-100 average for each combonation event, division, gender, and year. Since this did not have the same features as the original dataset, it was saved to a new file, top100avg.csv. Using top100avg_calculator.py, the csv file was created with 5 features: Event, Sex, Division, Year, and Points. In this case, Points is the average points value of the top-100 (aka all the values that were originally scraped) within the specified event/sex/division/year.

**Challenging Moment:** when I first reached this point, the original top100avg_calculator.py created a dataset with point values spread out over each year, like this

| Event | Sex | Division | 2010 Points | 2011 Points | 2012 Points | ... | 2023 Points |
|-------|-----|----------|-------------|-------------|-------------|-----|-------------|
| 100m  | Men | NAIA     | 784         |         789 |         791 | ... | 802         |

However, this led to significant issues when attempting to train models. It took heavy thought to find the issue. Since my mind naturally went to this structure, it made sense to me. I struggled to see why the models didn't understand it the way I did. Eventually, I found that this way worked. The new data contains the same information, but spread across many more rows.

| Event | Sex | Division | Year | Points |
|-------|-----|----------|------|--------|
| 100m  | Men | NAIA     | 2010 | 784    |
| 100m  | Men | NAIA     | 2011 | 789    |
| 100m  | Men | NAIA     | 2012 | 791    |
| ...   | ... | ...      | ...  | ...    |
| 100m  | Men | NAIA     | 2023 | 802    |


## Exploratory Analysis

Now that everything is in place, it's time to explore the data itself. The first graph to be built was the average points vs time. Instead of having 200+ lines on the graph, it makes sense to filter it. Eventually, there will be a web app to quickly filter, details can be found in the future works section (at the bottom of this page). I arbitrarily filtered to Women's Division II, removed the 2020 data (due to the influence of COVID-19), and produced the following graph.

![Sample Filtered Graph](/Images/EDA2.png)

Several other filters were applied during the EDA process, and the full exploratory analysis can be found in EDA.ipynb.
A similar graph was created to show the average point total across all events for each division, showing the disparity across levels. Keep in mind the limitations from above, however, that gaps between High School/College and College/World may be exaggerated. Comparison between levels of high school and between levels of college provides a more accurate depiction.

![Division Separation](/Images/EDA10.png)

**Challenging Moment:** During the EDA process, the heatmap below was generated to view the distribution of top collegiate marks over the course of the season. Notably, there were no marks during the time period of the National Championships, which led to the discovery (outlined in "Limitations") that TFRRS does not include the national meets in their lists. This was a difficult discovery, since many season best marks are recorded at those meets, skewing the collegiate numbers down. However, since it is uniform across all collegiate marks and years, it shouldn't affect the end model. It will just reflect the national qualifying list, rather than the annual leaderboard.

![Performance Date Heatmap](/Images/EDA7.png)

## Model Building

Brief introduction to the ML model and the process of building one.


| Model on Poorly Structured Data | RMSE      | MAE       | R^2     |
|---------------------------|-----------|-----------|---------|
| Linear Regression         | 12.0338   | 9.8392    | 0.9973  |
| Ridge Regression          | 12.0285   | 9.8337    | 0.9973  |
| Lasso Regression          | 14.4212   | 11.5965   | 0.9962  |
| Decision Tree Regression  | 38.6747   | 21.3415   | 0.9725  |
| Random Forest Regression  | 27.1530   | 16.7773   | 0.9864  |
| Support Vector Regression | 203.5704  | 169.8433  | 0.2379  |
| Gradient Boosting Regression | 31.0387 | 16.5701   | 0.9823  |



| Model on Restructured Data | RMSE       | MAE        | R^2       |
|---------------------------|------------|------------|-----------|
| Linear Regression         | 117.72177  | 95.72364   | 0.71382   |
| Ridge Regression          | 117.72402  | 95.72757   | 0.71381   |
| Lasso Regression          | 117.89145  | 96.06475   | 0.71299   |
| Decision Tree Regression  | 22.18599   | 13.01396   | 0.98984   |
| Random Forest Regression  | 17.06535   | 10.74354   | 0.99399   |
| Support Vector Regression | 221.39544  | 184.32384  | -0.01220  |
| Gradient Boosting Regression | 39.44551 | 28.18553   | 0.96787   |


## Results

Brief introduction to the results of the model(s)

### Model Forecast

Detailed look at where the model(s) say each discipline will project to.

### Variation Across Events

Detailed look at how the historical progression differs among disciplines.

### Similarities Between Events

(IF NEEDED) Dive into the details of if there are similarities in the progression
of each discipline, and why that may be the case

## Conclusion

Come to a final stance on the main points outlined at the beginning, using the
results from this study as the evidence for such a claim

## Future Work

Determine what the next possible steps will be in researching this topic. (Larger
sample size, different approach, narrower/broader scope, etc.)