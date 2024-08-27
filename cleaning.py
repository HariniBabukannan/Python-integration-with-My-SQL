import pandas as pd
import sqlalchemy

def fetch_and_clean_data(connection_str, table_name, cleaned_table_name):
    # Create a SQLAlchemy engine
    engine = sqlalchemy.create_engine(connection_str)

    # Fetch the data from the table
    with engine.connect() as connection:
        loan = pd.read_sql_table(table_name, con=connection)

    # Debug: Print columns of loan DataFrame
    print("Columns in loan DataFrame:", loan.columns)

    # Perform data cleaning
    remove_null_values = [" income_annum"]
    for column in remove_null_values:
        loan = loan[~loan[column].isnull()]
        

    # Convert specific columns from object to numeric
    columns_to_convert = [' bank_asset_value', ' cibil_score', ' commercial_assets_value',
                          ' income_annum', ' loan_amount', ' loan_term',
                          ' luxury_assets_value', ' no_of_dependents',
                          ' residential_assets_value', 'loan_id']
    for col in columns_to_convert:
        loan[col] = pd.to_numeric(loan[col], errors='coerce')
        
    # Append cleaned data back to the SQL table
    with engine.connect() as connection:
        loan.to_sql(cleaned_table_name, con=connection, if_exists='replace', index=False)
    print(f"Cleaned data appended to {cleaned_table_name} successfully.")

if __name__ == "__main__":
    # Example usage:
    connection_str = 'mysql+mysqlconnector://root:%40Harini123@localhost:3306/loan'  # Replace with your actual connection string
    table_name = 'loan'  # Replace with your actual table name
    cleaned_table_name = 'cleaned_data'  # Replace with your desired cleaned table name

    fetch_and_clean_data(connection_str, table_name, cleaned_table_name)
