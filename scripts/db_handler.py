from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from scripts.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# Create PostgreSQL connection string
def create_connection_string():
    return f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def save_to_postgres(df, table_name):
    """
    Save a DataFrame to a PostgreSQL table.
    """
    try:
        # Create an SQLAlchemy engine
        engine = create_engine(create_connection_string())
        
        # Save the DataFrame to the PostgreSQL table
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Data successfully saved to table '{table_name}'.")
    
    except SQLAlchemyError as e:
        print(f"Error saving data to PostgreSQL: {e}")


