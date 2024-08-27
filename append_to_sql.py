import MySQLdb
import pandas as pd
from sqlalchemy import create_engine

def append_to_sql(csv_file, connection_str, table_name):
    
        # Read the CSV file into a Pandas DataFrame
        loan = pd.read_csv(csv_file, low_memory=False, dtype="unicode", encoding="latin1")
        
        # Create a SQLAlchemy engine
        engine = create_engine(connection_str)
        
        # Append the DataFrame to the SQL table
        loan.to_sql(table_name, con=engine, if_exists='append', index=False)
        
        print(f"Data appended to {table_name} successfully.")


# Example usage:
if __name__ == "__main__":
    csv_file = r'C:\Users\ELCOT\Downloads\loan.csv'  # Replace with the path to your CSV file
    connection_str = 'mysql+mysqlconnector://root:%40Harini123@localhost:3306/loan'  # Using MySQL Connector/Python
    table_name = 'loan'  # Replace with the name of your SQL table
    
    append_to_sql(csv_file, connection_str, table_name)