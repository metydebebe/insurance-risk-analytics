# End-to-End Insurance Risk Analytics & Predictive Modeling

This project is part of the AlphaCare Insurance Solutions (ACIS) initiative to develop advanced risk and predictive analytics for car insurance in South Africa.

# Insurance Risk Analytics - Task 1: Exploratory Data Analysis (EDA)

## Project Overview

The goal of Task 1 is to perform a foundational Exploratory Data Analysis (EDA) on historical insurance claim data to uncover patterns in risk and profitability, which will inform marketing strategies and premium optimization.

## Data Description

The dataset covers insurance policies and claims from February 2014 to August 2015, containing over 1 million records with 52 features including:

- **Policy details:** UnderwrittenCoverID, PolicyID, TransactionMonth
- **Client information:** Gender, MaritalStatus, Citizenship, Language, Bank, etc.
- **Location:** Province, PostalCode, MainCrestaZone, SubCrestaZone
- **Vehicle details:** Make, Model, VehicleType, RegistrationYear, Cylinders, Kilowatts, etc.
- **Financials:** TotalPremium, TotalClaims, SumInsured, CalculatedPremiumPerTerm
- **Plan and coverage:** CoverCategory, CoverType, ExcessSelected, etc.

## Methodology

1. **Data Loading and Cleaning:**  
   Load pipe-separated data, parse dates, convert categorical variables, and handle missing values by dropping or imputing as appropriate.

2. **Descriptive Statistics:**  
   Summarize key financial variables to understand central tendency, spread, and anomalies.

3. **Loss Ratio Calculation:**  
   Compute Loss Ratio and analyze its variation across different segments.

4. **Visualization:**  
   Use histograms, boxplots, scatter plots, and line charts to explore distributions, outliers, correlations, and temporal trends.

5. **Documentation:**  
   Provide detailed comments explanations.

## Repository Structure

insurance-risk-analytics/
│
├── data/
│ ├── raw/ # Original raw data files
│ ├── processed/ # Cleaned and processed data files
│
├── notebooks/
│ └── task-1-eda.ipynb # EDA notebook with code and markdown
│
├── src/
│ ├── data_processing.py # Data loading and preprocessing functions
│ ├── eda_utils.py # Helper functions for EDA visualizations and stats
│
├── figures
│
├── requirements.txt # Python dependencies
├── README.md # Project overview and instructions
└── .github/
└── workflows/
└── ci.yml # GitHub Actions workflow for CI/CD

---

## How to Run

1. Clone the repository:

git clone https://github.com/metydebebe/insurance-risk-analytics.git
cd insurance-risk-analytics

2. Create and activate a Python virtual environment:

conda create --name insurance-risk-analytics python=3.11
conda activate insurance-risk-analytics

3. Install dependencies:

pip install -r requirements.txt

4. Run the EDA notebook:

- Open `notebooks/task-1-eda.ipynb` in Jupyter Lab or Notebook.
- Follow the notebook cells to reproduce the analysis and visualizations.
