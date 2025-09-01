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

try:
    engine = create_engine("sqlite:///:memory:")
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

try:
    for row in rows:
        stmt = insert(receipts).values(**row)
        with engine.begin() as connection:
            cursor = connection.execute(stmt)
    print(f"{len(rows)} rows inserted")
except Exception as e:
    print(f"Error inserting rows: {e}")

with engine.connect() as con:
    rows = con.execute(text("""SELECT * from receipts"""))
    print(f"Connected to database with {len(rows.all())} rows")
    for row in rows:
        print(f"The row is {row}")