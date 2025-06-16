# End-to-End Insurance Risk Analytics & Predictive Modeling

This project is part of the AlphaCare Insurance Solutions (ACIS) initiative to develop advanced risk and predictive analytics for car insurance in South Africa.

# Task 1: Exploratory Data Analysis (EDA)

### Overview

The goal of Task 1 is to perform a foundational Exploratory Data Analysis (EDA) on historical insurance claim data to uncover patterns in risk and profitability, which will inform marketing strategies and premium optimization.

### Data Description

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

### Repository Structure

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

### How to Run

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

# Task 2: Reproducible and Auditable Data Pipeline with DVC

This project uses **Data Version Control (DVC)** to ensure that all datasets are versioned alongside the codebase, enabling reproducibility, auditability, and compliance with regulatory standards in finance and insurance.

### Overview

- DVC tracks large data files efficiently by storing them outside Git, while metadata files (`.dvc`) are committed to Git.
- A local remote storage directory is configured to hold the actual data files.
- This setup allows any team member or auditor to reproduce analyses or model results exactly, by syncing the correct data versions.

### Setup Instructions

1. **Install DVC**

   pip install dvc

2. **Initialize DVC in the project root**

   dvc init
   git add .dvc .gitignore
   git commit -m "Initialize DVC for data version control"

3. **Configure Local Remote Storage**

   Create a directory on your machine to store DVC-tracked data (outside the Git repo):

   mkdir -p /path/to/local/dvc-storage
   dvc remote add -d localstorage /path/to/local/dvc-storage
   git add .dvc/config
   git commit -m "Configure local DVC remote storage"

4. **Add Datasets to DVC**

   Place your raw dataset in the project (e.g., `data/raw/MachineLearningRating_v3.txt`), then track it with DVC:

   dvc add data/raw/MachineLearningRating_v3.txt
   git add data/raw/MachineLearningRating_v3.txt.dvc .gitignore
   git commit -m "Add raw dataset to DVC tracking"

5. **Push Data to Remote Storage**

   Upload the large data files to the configured remote storage:

   dvc push

6. **Reproducing the Environment**

   To reproduce the exact data versions on another machine or after cloning the repo:

   git clone
   dvc pull

# Task 3: Hypothesis Testing and Risk Analytics

This task involves performing hypothesis testing to identify significant differences in insurance risk metrics across key segments in the dataset. The goal is to support AlphaCare Insurance Solutions (ACIS) in refining their pricing and risk strategies based on data-driven insights.

### Overview

Objective: Test for statistically significant differences in claim frequency, claim severity, and margin across different groups.

### Segments analyzed

Provinces (Gauteng vs. Western Cape)

Zip Codes (selected high-frequency postal codes)

Gender (Male vs. Female)

### Key Performance Indicators (KPIs)

Claim Frequency: Binary indicator (1 if any claim occurred, 0 otherwise).

Claim Severity: Average claim amount given a claim occurred.

Margin: Difference between total premium collected and total claims paid.

### Methodology

Data Preparation:

Cleaned dataset by removing invalid records and columns with excessive missing data.

Converted relevant columns to categorical data types.

Segmentation:

Created subgroups based on Province, Zip Code, and Gender.

Statistical Tests:

Chi-squared test for differences in claim frequency (categorical variable).

Independent t-tests (Welch’s t-test) for differences in claim severity and margin (continuous variables).
