# 🏎️ Dirty Data Task: Motorsport Payroll & Headcount

## 📌 The Business Problem
A professional motorsport racing team needed an accurate headcount and payroll forecast for the upcoming season. However, their HR and Payroll systems were heavily fragmented. The raw data contained missing values, conflicting date formats, duplicate records, and mixed data types that crashed their BI tools.

## 🛠️ The Solution
Build an automated data cleaning pipeline in Python (Pandas) to ingest, sanitize, and aggregate the dirty data into a production-ready format.

## 🔍 Key Data Cleaning Steps Executed:
* **Structural Purge:** Removed purely empty rows and exact duplicates.
* **Data Type Conversion:** Stripped financial formatting ($,) and forced pandas to recognize payroll as numeric floats.
* **Categorical Standardization:** Used dictionary mapping to standardize brutal typos across department names (e.g., 'ENG', 'Enginering' -> 'Engineering').
* **Datetime Standardization:** Unified multiple conflicting date formats (YYYY-MM-DD, MM/DD/YY) into standard datetime objects.
* **Targeted Imputation:** Handled missing data by dropping rows missing critical financial metrics while utilizing placeholder imputation for non-critical descriptive text (emails).

## 📊 The Data Output
The Python script outputs two pristine CSV files:
1. `clean_motorsport_data.csv`: 895 verified, clean employee records.
2. `department_payroll_summary.csv`: An aggregated executive summary of headcount and total payroll by department. 

## 📈 Executive Dashboard (Tableau)
**[View the Live Interactive Dashboard Here] https://public.tableau.com/views/MotorsportTeamPayrollHeadcount/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link**

<img alt="Payroll_By_Dept_Dash" src="https://github.com/user-attachments/assets/0c9f7f97-3add-41ed-a4c0-2e5277e75e2a" />

To make the cleaned data actionable for the Team Principal, I connected the aggregated summary to Tableau Public and built a dark-mode executive dashboard:
* **The Payroll Engine:** A sorted horizontal bar chart highlighting the budget distribution, instantly revealing Sales & Marketing as the highest cost center ($19.2M).
* **Headcount Distribution:** A custom dual-axis doughnut chart visualizing the exact proportion of the 895 verified employees across the five departments.
