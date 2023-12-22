import pandas as pd
from sqlalchemy import create_engine, text

# Create a PostgreSQL database connection using sqlalchemy
# Replace the connection URL with your PostgreSQL database details
# Format: 'postgresql://username:password@host:port/database_name'
def extract_table_name(query):
    # Split the query by whitespace and find the table name after "FROM"
    tokens = query.split()
    from_index = tokens.index("FROM")
    table_name = tokens[from_index + 1]
    # Remove any trailing punctuation or quotation marks
    table1_name = table_name.split("_")
    return table1_name[0]
db_url = 'postgresql://mohan:mohan@turbo.katrina.colostate.edu:5432/mohan'
engine = create_engine(db_url)

# Define your SQL queries for the tables
#query1 = text("select * FROM gse73072_metadata")
#query2 = text("SELECT * FROM gse61754_metadata")
query1= text("select * from gse73072_dee4")
query2= text("SELECT * FROM gse73072_dee1")
query3= text("SELECT * FROM gse73072_dee2")
query4= text("SELECT * FROM gse73072_dee3")
query5= text("SELECT * FROM gse73072_dee5")
query6= text("SELECT * FROM gse73072_duke")
query7= text("SELECT * FROM gse73072_uva")
query8= text("SELECT * FROM gse61754_value")
query9= text("SELECT * FROM gse118223_values")

# Fetch data using pandas' read_sql function
with engine.connect() as connection:
    df1 = pd.read_sql_query(query1, connection)
    df2 = pd.read_sql_query(query2, connection)
    df3 = pd.read_sql_query(query3, connection)
    df4 = pd.read_sql_query(query4, connection)
    df5 = pd.read_sql_query(query5, connection)
    df6 = pd.read_sql_query(query6, connection)
    df7 = pd.read_sql_query(query7, connection)
    df8 = pd.read_sql_query(query8, connection)
    df9 = pd.read_sql_query(query9,connection)
# Combine the dataframes vertically to align the data
merged_df = pd.concat([df1, df2, df3,df4,df5,df6,df7,df7,df8,df9], axis=0, ignore_index=True, sort=False)
#merged_df = pd.concat([df1], axis=0, ignore_index=True, sort=False)
# Save the merged dataframe to a CSV file
merged_df.to_csv('sample1.csv', index=False)

print("Aligned data saved to sample1.csv")

