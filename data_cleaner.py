import pandas as pd

# 1. Load the dirty data
df = pd.read_csv('motorsport_employee_records.csv')
print({f"Original shape: {df.shape}"})

# 2. Drop completely empty rows
# 'how="all"' means ONLY drop the row if EVERY single column is NaN
df = df.dropna(how='all')

# 3. Drop exact duplicate rows
df = df.drop_duplicates()

print({f"Shape after initial purge: {df.shape}"})


# ---- CLEANING SALARY COLUMN ----
# 4. Force everything to be a string temporarily to manipulate the text

df['salary'] = df['salary'].astype(str)

# 5. Strip out the dollar signs and commas, replacing them with nothing ('')
df['salary'] = df['salary'].str.replace('$','',regex=False)
df['salary'] = df['salary'].str.replace(',','',regex=False)

# 6. Force the column to become a numeric data type (float)
# errors='coerce' as safety net: if it hits a word it can't convert, it turns into a NaN (null) instead of crashing
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')

# Data review after changes
print("\n--- NEW SALARY DATA TYPE ---")
print(df['salary'].dtype)
print("\n--- FIRST 5 SALARIES ---")
print(df['salary'].head())


# --- STANDARDIZING DEPARTMENTS ---

# 7. Check current 'department' column
print("\n--- DEPARTMENTS BEFORE CLEANING ---")
print(df['department'].value_counts())

# 8. Build the translation dictionary
# Format is: {'Wrong Spelling': 'Correct Spelling'}
dept_corrections = {
    'ENG': 'Engineering',
    'Enginering': 'Engineering',
    'Aero': 'Aerodynamics',
    'Sales': 'Sales & Marketing',
    'Pit-Crew': 'Pit Crew',
    'Logstics': 'Logistics'
}

# 9. Apply the translation
# .replace() looks at the dictionary. If it finds a match, it swaps it. 
# If a word is already correct and not in the dictionary, it just leaves it alone.
df['department'] = df['department'].replace(dept_corrections)

# 10. Check our work
print("\n--- DEPARTMENTS AFTER CLEANING ---")
print(df['department'].value_counts())


# ---- FIXING DATES ----

# 11. Force the string column into proper datetime objects
# format='mixed' tells pandas to look at every single cell individually 
# and try to figure out the formatting on its own

df['join_date'] = pd.to_datetime(df['join_date'], format='mixed', errors='coerce')

print("\n---- NEW JOIN DATE DATA TYPE ----")
print(df['join_date'].dtype)

print("\n---- FIRST 5 STANDARDIZED DATES ----")
print(df['join_date'].head())


# ---- HANDLING MISSING DATA ----
# 12. Drop rows where critical data is missing
# subset=['salary', 'join_date'] tells pandas to only remove the row if the salary OR join_date is missing
df = df.dropna(subset=['salary', 'join_date'])


# 13. Fill in the missing non-critical data
# We don't want to drop employees just because HR forgot their email
# Fill the NaN values with a standard placeholder
df['email_address'] = df['email_address'].fillna('missing_email@email.com')

print("\n---- FINAL NULL COUNT ----")
print(df.isnull().sum())

print(f"\n---- FINAL SHAPE ----")
print(df.shape)


# ---- DATA ANALYSIS ----

# 14. Group the data by Department
# Count the unique Employee IDs (headcount) and sum the Salaries (payroll)

department_summary = df.groupby('department').agg(
    Headcount = ('employee_id', 'count'),
    Total_Payroll = ('salary', 'sum')
).reset_index()

# 15. Format the Total Payroll back into a readable currency format for the final report
# We do this at the very end so the math is already finished.

department_summary['Total_Payroll'] = department_summary['Total_Payroll'].apply(lambda x: f"${x:,.2f}")

# 16. Print the final report
print("\n--- EXECUTIVE DEPARTMENT SUMMARY ---")
print(department_summary.to_string(index=False))

# 17. Export the clean data for Tableau/Visualization
df.to_csv('clean_motorsport_data.csv', index=False)
department_summary.to_csv('department_payroll_summary.csv', index=False)