import pandas as pd
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="turbo.katrina.colostate.edu",
    database="mohan",
    user="mohan",
    password="mohan"
)

# Run the first query to retrieve the desired column names for the first dataset
column_query = "SELECT accession FROM gse118223_metadata WHERE timepoint ='0' "
df1 = pd.read_sql_query(column_query, conn)
default_column_names = ["probe_id"]
column_names = default_column_names + df1["accession"].tolist()
columns_str = ', '.join(column_names)

# Construct the second query with the retrieved column names for the first dataset
second_query = f"SELECT {columns_str} FROM gse118223_values;"
df_result = pd.read_sql_query(second_query, conn)

# Run the second query to retrieve the desired column names for the second dataset
column_query1 = "SELECT accession FROM gse61754_metadata WHERE timepoint ='0' "
df2 = pd.read_sql_query(column_query1, conn)
default_column_names1 = ["probe_id"]
column_names1 = default_column_names1 + df2["accession"].tolist()
columns_str1 = ', '.join(column_names1)

# Construct the second query with the retrieved column names for the second dataset
second_query1 = f"SELECT {columns_str1} FROM gse61754_value;"
df_result1 = pd.read_sql_query(second_query1, conn)

# Combine the results of both datasets
combined_result = pd.concat([df_result, df_result1], axis=0, ignore_index=True,sort=False)
# Save the combined result to a CSV file
csv_filename = "combined_result_file1.csv"
combined_result.to_csv(csv_filename, index=False)

# Close the database connection
conn.close()

print(f"Combined result saved to {csv_filename}")
