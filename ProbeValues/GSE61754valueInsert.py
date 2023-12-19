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
# Set the path to your CSV file
csv_file = "GSE61754_Value.csv"

# Open the CSV file
with open(csv_file, 'r') as file:
    # Read the CSV data
    csv_data = csv.reader(file)
    
    # Get the first row as column names
    columns = next(csv_data)[1:]
    
    # Get the table name
    table_name = "gse61754_value"
    
    # Generate the ALTER TABLE statements
    alter_table_query = ""
    for column in columns:
        alter_table_query += f"ALTER TABLE {table_name} ADD COLUMN {column} TEXT;\n"
    
    # Execute the ALTER TABLE statements
    cur.execute(alter_table_query)
    
    # Insert the data into the table
    count = 0
    for row in csv_data:
       insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})"
       print("The query output ", count)
       cur.execute(insert_query, row)
       count +=1

# Commit the changes and close the database connection
conn.commit()
cur.close()
conn.close() 