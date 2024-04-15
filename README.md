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
- **top100avg_nofield.csv** - top100avg.csv with field event rows removed (used for testing purposes only)

### Notebooks
- **EDA.ipynb** - Exploratory data analysis (Initial graphing)
- **models.ipynb** - Model building, training, and selection
- **model_scaling.ipynb** - Notebook for custom feature scaling model
- **presentation.ipynb** - Organized presentation of results

## Project Introduction

The goal of this project is to find trends in the top-100 performances of each year across various track and field events. Ultimately, a model was created to forecast the top-100 average for future years. There were several steps to this project, each of which encompassed one or more of the NWMSU Data Analytics program objectives. The process was as follows:

1. Scrape the data from results databases on the internet
2. Clean the data
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






| Model on Entire Data      | RMSE       | MAE        | R^2       |
|---------------------------|------------|------------|-----------|
| Linear Regression         | 117.72177  | 95.72364   | 0.71382   |
| Linear with Feature Scaling | 121.16606 | 88.08427  | 0.70197   |
| Ridge Regression          | 117.72402  | 95.72757   | 0.71381   |
| Lasso Regression          | 117.89145  | 96.06475   | 0.71299   |
| Decision Tree Regression  | 22.18599   | 13.01396   | 0.98984   |
| `Random Forest Regression`  | 17.06535   | `10.74354`   | `0.99399`   |
| Support Vector Regression | 221.39544  | 184.32384  | -0.01220  |
| Gradient Boosting Regression | 39.44551 | 28.18553   | 0.96787  |
| Prophet (Time Series)     | 285.64590  | 235.14233  | -0.77249  |
| VAR (Time Series)         | 215.25424  | 182.99602  | -0.00654  |
| ARIMA (Time Series)       | LinAlg Error |          |           |

| Model on Individual Subsets | RMSE      | MAE        | R^2     |
|-----------------------------|-----------|------------|---------|
| `Linear Regression`           | `16.0445`   | 12.1210    | `0.9945`  |


## Results

With the Individual Subset Linear Regression model performing best with the training and testing data, that model was selected to project the 2024 point values. The choice was not difficult, as the only models that emerged with similar performance metrics were the tree-based models, which are incapable of making projections such as these. With this study being conducted in April 2024, the actual values for most divisions will be available within a few weeks of the project's completion. The indications of the training, however, suggest most of the projections will be within 20 points.

### Model Forecast

While the process for achieving the most accurate forecasts is quite complex, the results themselves are rather straightforward. The model projects several events (exactly half in the professional ranks) to see a decline in top-100 average point values. These events saw stronger rises in recent year(s), and the projection is suggesting a regression to the mean. It is important to understand that these are still following an upward linear trend, and the decline is due to the 2023 value being above the trendline. With 2024 being an Olympic year, these projections of decline may be more accurate for high school and college divisions, and the global division may see inaccuracies due to the Olympic Games.

### Variation Across Events

Each discipline in track and field appears to be on its own trajectory, with enough underlying factors for each one, making it distinct from the others. To better understand which events are advancing at faster rates, the charts like those shown in figures 2 and 3 were zero-shifted from 2010. This illustrates the change since 2010 without any initial bias. With a common starting point, Figure 7 makes it easier to view which events have seen the most growth since 2010, without the initial bias of some events starting higher than others. Figure 7 only shows values for the Global Women's leaderboard, but other divisions show similar results. In most divisions, the high jump is revealed to be the most stagnant over the time period, while the 100 meter is generally among the top growing events. Some events, like the shot put, vary widely between divisions. Overall, however, very few events, regardless of division, have seen notable decline. Of the ones that have seen a lower value in 2023 than 2010, all of them come from field events. The uniform growth of the running events raises questions, since both running and field events share a long history of maximal human performance. That characteristic should provide similar growth trajectories, so it appears that there may be an underlying force, unique to the running events, that is impacting these statistics. Early speculation would suggest 'super spikes' as this force, but research has yet to confirm this claim.

![Zero Based Graph](/Images/result1.png)

### Similarities Between Events

While there are clear differences among each event, division, and sex, there are also visable similarities. In most cases, there is an upward trend, particularly in the running events. Several distance events have seen a spike in more recent years. In the case of divisions, it appears that NAIA and NCAA D-III are a few years behind NCAA D-I and D-II, with their rises appearing to mirror the latter group's changes about two years later. Additionally, the worldwide division shows a cycle that matches the Olympic Games. The figure above illustrates this nicely, with visable peaks in 2012 and 2016. It can safely be concluded that there are inherent similarities across events and divisions, but as the model results indicate, those similarities are not beneficial towards modeling with the information collected in this study.

## Conclusion

Given the results of this project, it does not appear that there is a meaningful relationship between events (within or outside the same division and/or sex), division (within or outside the same event and/or sex), or sex (within or outside the same division and/or event). While there may be similarities between series with one or more common traits (same division, sex, or event), but external series data should not be used in projections, as it was shown to be a detriment to model performance. Models are best suited to be trained on their own individual subset, even if the sample size is small. Additionally, the relationship among the 13-year timeframe studied was shown to be linear across all subsets. Projections beyond a few years is not recommended with this model, as the sample size is relatively small. Expanding the dataset to several decades may reveal a different shaped curve, and the linear nature may only be relevant to a small time period.


## Future Work

Further research is suggested on this topic to further examine the human performance trends in the sport of track and field. Results from this study suggest a deeper view should be taken at individual subsets (ie. event/sex/division combinations) over a longer period of time, rather than multiple subsets over a short period of time. World Athletics, known in this project as the 'World' division, contains the largest backlog of performances, so it is the prime prospect for this kind of investigation.  

Additionally, given the amount of data collected during this project, it would be advantageous to create a tool for readers to easily view filtered subsets of the data, rather than be limited to the figures shown in this report. A web app has been proposed, made with Shiny for Python, to reactively build graphs based on user-input filters. This way, readers can conduct their own exploratory analysis of the data, and stimulate new ideas for additional research. 
