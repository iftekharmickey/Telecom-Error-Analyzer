# Telecom-Error-Analyzer

This script was created at [Infozillion Teletech BD Ltd.](https://www.infotelebd.com/) to automate the handling of a manual and repetitive task related to error code analysis from Mobile Network Operators (MNOs) and Internet Protocol Telephony Service Providers (IPTSPs). The script combines and analyzes data from two CSV files, performing data manipulation, filtering, and aggregation to create a consolidated table of error codes for each operator, along with a "Grand Total" summary.

## Dependencies:

- Python (version 3.x)
- pandas (version 1.3.3 or higher)
- numpy (version 1.21.2 or higher)

## Installation:

1. **Python**
   
   - If Python is not installed, download and install it from (https://www.python.org/).

2. **pandas and numpy**

   - Install the required Python libraries using the following command in your terminal or command prompt:

    ```python
    pip install pandas numpy
    ```
    
## Usage:

- Run the script.
- Enter the file names when prompted for the MNO and IPTSP CSV files.
- The script will process the data, perform the necessary calculations, and print the resulting DataFrame with error code summaries.
- The script will also print the resulting DataFrame with error code summaries.
- Subsequently, the script will generate an output CSV file named `combined_output.csv`.

## Script Overview:

1. **Input:**

   - The script prompts the user to enter the file names for the MNO and IPTSP CSV files.
   - The data is loaded into separate DataFrames using pandas.

2. **Data Processing:**

   - The two DataFrames are concatenated vertically (axis=0) to combine the data.
   - Rows with specific values in the 'Filters' column are filtered out.
   - 'null' values in the 'Operators' column are filled with 0.

3. **Data Transformation:**

   - The data is pivoted to create a table with 'Operators' as index, 'Filters' as columns, and the sum of error codes as values.
   - Non-numeric columns are converted to integers, handling non-numeric values gracefully.
   - A 'Total' column is calculated by summing error code columns for each operator.

4. **Grand Total Calculation:**

   - The script calculates the "Grand Total" row by summing error codes across all operators.
   - The 'Grand Total' row is appended to the DataFrame.

5. **Data Cleaning:**

   - Non-finite values (NaN or inf) in the 'Total' column are replaced with 0.
   - The 'Total' column is rounded to the nearest integer.

6. **Output:**

   - The resulting DataFrame is saved to a CSV file named `combined_output.csv`.
   - The script prints the final DataFrame with error code summaries.





