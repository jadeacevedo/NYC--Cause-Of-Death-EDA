# NYC--Cause-Of-Death-EDA

This repository contains a modular Python project that analyzes the leading causes of death in New York City from 2007 to the present. By examining trends across different years, sexes, and race/ethnicities, this analysis aims to highlight critical public health patterns.

The data is fetched directly from the [NYC Open Data API](https://catalog.data.gov/dataset/new-york-city-leading-causes-of-death-ce97f), cleaned using Regular Expressions and Pandas, and visualized using interactive Plotly charts.

## Project Structure

```text
nyc-death-analysis/
├── data/                   # Directory for datasets (gitignored)
│   └── .gitkeep
├── output/                 # Directory for generated HTML charts
├── src/                    # Source code modules
│   ├── __init__.py
│   ├── data_loader.py      # Logic for fetching API / loading JSON
│   ├── processor.py        # Regex data cleaning and transformation
│   ├── analysis.py         # Pivot tables and statistical aggregations
│   └── visualization.py    # Plotly interactive charts
├── main.py                 # Central execution script
├── requirements.txt        # Python library dependencies
└── README.md               # Project documentation
----------------------------------------------------
## Insights and key findings 
1. The Dominance of Heart Disease and Cancer
Analysis: Looking at the overall top causes of death, "Diseases of the Heart" and "Malignant Neoplasms" (Cancer) vastly outnumber all other causes. The drop-off in total deaths between these top two and the third leading cause is steep.

Conclusion: Public health initiatives, funding, and preventative care in NYC must continue to heavily prioritize cardiovascular health and cancer screenings. These two areas represent the most significant threat to public health across all demographics.

2. Distinct Mortality Profiles by Sex
Analysis: When breaking down the top causes by sex, we see structural differences in mortality. While heart disease and cancer are the leading killers for both men and women, the secondary causes diverge. Males historically show higher rates of mortality from external causes (like accidents, suicide, and assault) and Parkinson's. Females show higher rates of mortality from Cerebrovascular Disease (Strokes), Alzheimer's, and Hypertension.

Conclusion: Healthcare interventions and public safety messaging need to be gender-aware. For men, mental health support, violence prevention, and accident awareness are critical areas for intervention. For women, early screening for strokes, blood pressure management, and elder care support are paramount.

3. The Rise of Neurodegenerative and Age-Related Diseases
Analysis: The trend lines over time (particularly looking at the 2014–2017 period and beyond) show a distinct upward trajectory for diseases like Alzheimer's, Parkinson's, and Hypertension. Parkinson's, in particular, emerged as a major cause in later years.

Conclusion: This trend strongly suggests an aging population in New York City. As life expectancy generally increases, people are living long enough to develop late-onset neurodegenerative diseases. The city's healthcare infrastructure must prepare for this by expanding geriatric care, long-term assisted living facilities, and specialized neurological care.

Overall Summary
The data paints a picture of a city where the primary medical battles are chronic, long-term illnesses (Heart Disease, Cancer). However, the most urgent growing threat to the healthcare system is the rapid rise in age-related cognitive and neurodegenerative diseases.
