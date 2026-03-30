# NYC--Cause-Of-Death-EDA

This repository contains a modular Python project that analyzes the leading causes of death in New York City from 2007 to the present. By examining trends across different years, sexes, and race/ethnicities, this analysis aims to highlight critical public health patterns.

The data is fetched directly from the [NYC Open Data API](https://catalog.data.gov/dataset/new-york-city-leading-causes-of-death-ce97f), cleaned using Regular Expressions and Pandas, and visualized using interactive Plotly charts.
Methodology & Data Processing

The dataset contains over 1,300 records detailing yearly death counts, crude death rates, and age-adjusted death rates. To prepare the data for analysis, a custom text-processing pipeline was implemented using Regular Expressions (Regex) to strip out complex ICD (International Classification of Diseases) codes, standardizing the cause-of-death descriptions. The core analysis relies on complex aggregations and pivot tables to calculate the mean death counts and age-adjusted rates across multidimensional demographic groupings.

**Key Dimensions Explored**

* Aggregate Mortality: Identifying the absolute highest killers in the city regardless of demographic lines.

* Gender Disparities: Analyzing how mortality profiles diverge between males and females.

* Temporal Trends: Tracking the rise and fall of specific diseases over a multi-year horizon (focusing heavily on the 2014–2017 shift).

* Demographic Vulnerabilities: Cross-referencing race/ethnicity with specific diseases to identify vulnerable subpopulations (e.g., heart disease in young minority males).

**Core Insights Derived from the EDA**

* The "Big Two" Dominance: The EDA overwhelmingly confirms that Diseases of the Heart and Malignant Neoplasms (Cancer) are the apex public health threats in NYC, vastly outnumbering all other causes of death combined.

* Divergent Risk Profiles by Sex: The visualizations reveal that secondary mortality causes are highly gendered. Males experience significantly higher mortality from external/behavioral factors (Assault, Suicide, Accidents), whereas females face higher mortality from physiological and age-related conditions (Cerebrovascular Disease, Alzheimer's, Hypertension).

* The Aging Population Curve: Time-series analysis uncovered a steep, statistically significant increase in deaths caused by Alzheimer’s, Hypertension, and Parkinson’s disease starting around 2014. This strongly indicates a demographic shift toward an aging population, highlighting a growing need for geriatric and neurodegenerative healthcare infrastructure.

----------------------------------------------------
## Insights and key findings 

### 1. The Dominance of Heart Disease and Cancer

Analysis: Looking at the overall top causes of death, "Diseases of the Heart" and "Malignant Neoplasms" (Cancer) vastly outnumber all other causes. The drop-off in total deaths between these top two and the third leading cause is steep.
<img width="1103" height="928" alt="newplot (2)" src="https://github.com/user-attachments/assets/e31c6414-674c-4842-91a0-546910161918" />

Conclusion: Public health initiatives, funding, and preventative care in NYC must continue to heavily prioritize cardiovascular health and cancer screenings. These two areas represent the most significant threat to public health across all demographics.

### 2. Distinct Mortality Profiles by Sex

Analysis: When breaking down the top causes by sex, we see structural differences in mortality. While heart disease and cancer are the leading killers for both men and women, the secondary causes diverge. Males historically show higher rates of mortality from external causes (like accidents, suicide, and assault) and Parkinson's. Females show higher rates of mortality from Cerebrovascular Disease (Strokes), Alzheimer's, and Hypertension.
<img width="1103" height="928" alt="newplot" src="https://github.com/user-attachments/assets/f3986e1b-7d35-433f-bdd9-c46c1ffae360" />

Conclusion: Healthcare interventions and public safety messaging need to be gender-aware. For men, mental health support, violence prevention, and accident awareness are critical areas for intervention. For women, early screening for strokes, blood pressure management, and elder care support are paramount.

### 3. The Rise of Neurodegenerative and Age-Related Diseases

Analysis: The trend lines over time (particularly looking at the 2014–2017 period and beyond) show a distinct upward trajectory for diseases like Alzheimer's, Parkinson's, and Hypertension. Parkinson's, in particular, emerged as a major cause in later years.
<img width="1103" height="928" alt="newplot (3)" src="https://github.com/user-attachments/assets/8f65dd8c-927b-4fe5-b5f6-7a45dc7e7f84" />

Conclusion: This trend strongly suggests an aging population in New York City. As life expectancy generally increases, people are living long enough to develop late-onset neurodegenerative diseases. The city's healthcare infrastructure must prepare for this by expanding geriatric care, long-term assisted living facilities, and specialized neurological care.

Overall Summary
The data paints a picture of a city where the primary medical battles are chronic, long-term illnesses (Heart Disease, Cancer). However, the most urgent growing threat to the healthcare system is the rapid rise in age-related cognitive and neurodegenerative diseases.

------------------------------------------------------------------------------------------
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
