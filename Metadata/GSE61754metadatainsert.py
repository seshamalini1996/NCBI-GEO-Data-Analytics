import psycopg2
import csv

# Connect to the database
conn = psycopg2.connect(
    host="turbo.katrina.colostate.edu",
    database="mohan",
    user="mohan",
    password="mohan"
)
# Open the CSV file
with open('GSE61754_Metadata.csv', 'r') as csvfile:
    # Create a CSV reader object
    csvreader = reader = csv.reader(csvfile)
     
    # Skip the header row
    next(csvreader)
    # Loop through the rows in the CSV file
    for row in csvreader:
        # Extract the values from the row
        col0 = row[0]
        col1 = row[1]
        col2 = row[2]
        col3 = row[3]
        col4 = row[4]
        col5 = row[5]
        col6 = row[6]
        col7 = row[7]
        cur = conn.cursor()

        # Execute a SQL query
        cur = conn.cursor()
        #cur.execute("INSERT INTO mytable (accession, title, tissue,timepoint,shedding,symptomatic,virus,subject) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)", (col1, col2, col4,col5,col6,col7,col8,col9))
        cur.execute("INSERT INTO gse61754_metadata (accession, title, sourcename,timepoint,vaccinationStatus,symptomSeverity,seroconversion,viralShedding) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)", (col0,col1, col2,col3,col4,col5,col6,col7))
        conn.commit()
        # Close the database connection
    conn.close()
