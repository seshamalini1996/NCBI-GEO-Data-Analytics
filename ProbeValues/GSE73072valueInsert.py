import psycopg2
import csv

# Connect to the database
conn = psycopg2.connect(
    host="turbo.katrina.colostate.edu",
    database="postgres",
    user="SMohan",
    password="temporary1"
)
cur = conn.cursor()
# Set the path to your CSV file
csv_file = "GSE73072_values.csv"

# Open the CSV file
with open(csv_file, 'r') as file:
    # Read the CSV data
    csv_data = csv.reader(file)
    
    # Get the first row as column names
    columns = next(csv_data)[2467:2887]
    
    # Get the table name
    table_name = "gse73072_dee1"
    
    # Generate the ALTER TABLE statements
    alter_table_query = ""
    for column in columns:
        alter_table_query += f"ALTER TABLE {table_name} ADD COLUMN {column} TEXT;\n"
    
    # Execute the ALTER TABLE statements
    cur.execute(alter_table_query)
    # Insert the data into the table
    for row in csv_data:
        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s']* 421)})"
        cur.execute(insert_query,[row[0]]+ row[2467:2887])


# Commit the changes and close the database connection
conn.commit()
cur.close()
conn.close() 