
from sqlalchemy import (
    create_engine,
    insert,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    Float,
    text,
)

# Export engine, metadata_obj, and receipts for use in other modules
__all__ = ["engine", "metadata_obj", "receipts"]

try:
    engine = create_engine("sqlite:///receipts.db")
    print("Engine created")
except ImportError:
    print("Error importing SQLAlchemy")
metadata_obj = MetaData()

# create city SQL table
table_name = "receipts"
receipts = Table(
    table_name,
    metadata_obj,
    Column("receipt_id", Integer, primary_key=True),
    Column("customer_name", String(16), primary_key=True),
    Column("price", Float),
    Column("tip", Float),
)
metadata_obj.create_all(engine)

rows = [
    {"receipt_id": 1, "customer_name": "Alan Payne", "price": 12.06, "tip": 1.20},
    {"receipt_id": 2, "customer_name": "Alex Mason", "price": 23.86, "tip": 0.24},
    {"receipt_id": 3, "customer_name": "Woodrow Wilson", "price": 53.43, "tip": 5.43},
    {"receipt_id": 4, "customer_name": "Margaret James", "price": 21.11, "tip": 1.00},
]

# Check if data already exists before inserting
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT COUNT(*) FROM receipts"))
        count = result.scalar()

        if count == 0:
            # Only insert data if table is empty
            for row in rows:
                stmt = insert(receipts).values(**row)
                with engine.begin() as conn:
                    conn.execute(stmt)
            print(f"{len(rows)} rows inserted")
        else:
            print(f"Table already contains {count} rows, skipping data insertion")
except Exception as e:
    print(f"Error checking/inserting rows: {e}")

    

