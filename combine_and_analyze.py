import pandas as pd
import numpy as np

# Ask for the MNO and IPTSP file names
mno_file_name = input("Enter the MNO file name: ")
iptsp_file_name = input("Enter the IPTSP file name: ")

# Load and process the first input file: MNO file
mno_df = pd.read_csv(mno_file_name, thousands=',')

# Load and process the second input file: IPTSP file
iptsp_df = pd.read_csv(iptsp_file_name, thousands=',')

# Combine the two DataFrames
combined_df = pd.concat([mno_df, iptsp_df], axis=0, ignore_index=True, sort=False)

# Filter out rows with 'others' and 'Total' in the 'Filters' column
combined_df = combined_df[~combined_df['Filters'].isin(['others', 'Total', 'Other Error Responses'])]

# Fill 'null' values with 0 in the 'Operators' column
combined_df['Operators'] = combined_df['Operators'].fillna(0)

# Pivot the data to create the desired table
result_df = combined_df.pivot_table(index='Operators', columns='Filters', values='Operators', aggfunc='sum', fill_value=0)

# Convert non-numeric columns to integers while handling non-numeric values gracefully
numeric_cols = result_df.columns.difference(['Operators'])
result_df[numeric_cols] = result_df[numeric_cols].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

# Calculate the 'Total' column by summing all error code columns for each operator
result_df['Total'] = result_df[numeric_cols].sum(axis=1)

# Calculate the "Grand Total" row
grand_total_row = result_df[numeric_cols].sum().to_frame().T
grand_total_row.index = ['Grand Total']  # Set the index to 'Grand Total'

# Calculate the total for the "Grand Total" row
grand_total_row['Total'] = grand_total_row[numeric_cols].sum(axis=1).values[0]

# Add the "Grand Total" row to the DataFrame
result_df = result_df._append(grand_total_row)

# Replace non-finite values (NaN or inf) with 0 in the 'Total' column
result_df['Total'] = result_df['Total'].replace([np.nan, np.inf, -np.inf], 0)

# Round the 'Total' column to the nearest integer
result_df['Total'] = result_df['Total'].round().astype(int)

# Rename the 'Filters' column to 'ANS'
result_df.columns.name = 'ANS'

# Save the output to a CSV file
result_df.to_csv('combined_output.csv')

# Print the updated DataFrame
print(result_df)
