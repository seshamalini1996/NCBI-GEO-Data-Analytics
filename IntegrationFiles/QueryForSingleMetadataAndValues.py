import psycopg2
import csv

# Connect to the database
conn = psycopg2.connect(
    host="turbo.katrina.colostate.edu",
    database="mohan",
    user="mohan",
    password="mohan"
)
cur = conn.cursor()

# Run the first query to retrieve the desired column names
column_query = "SELECT accession FROM gse118223_metadata WHERE timepoint ='0' "
cur.execute(column_query)
column_results = cur.fetchall()
#column_results = cur.fetchone()[0] 
#column_names = [result[0] for result in column_results]
default_column_names = ["probe_id"]
# Construct the second query with the retrieved column names
column_names =  default_column_names + [result[0] for result in column_results]
columns_str = ', '.join(column_names)
second_query = f"SELECT {columns_str} FROM gse118223_values;"

# Execute the second query
cur.execute(second_query)
result = cur.fetchall()

# Print the query result
#for row in result:
#    print(row)

# Close the database connection
cur.close()
conn.close()
# Create and write data to the CSV file
csv_filename = "result_file.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row with column names
    writer.writerow(column_names)
    
    # Write the data rows
    for row in result:
        writer.writerow(row)

        