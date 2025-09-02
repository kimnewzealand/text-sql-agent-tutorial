from smolagents import tool, CodeAgent, InferenceClientModel
from sqlalchemy import text
from tables import engine
import os
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

@tool
def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the database. Returns results as a simple string format.

    Available tables:

    1. 'receipts' table:
        Columns:
        - receipt_id: INTEGER (primary key)
        - customer_name: VARCHAR(16) (primary key)
        - price: FLOAT
        - tip: FLOAT

    2. 'waiters' table:
        Columns:
        - receipt_id: INTEGER (primary key, foreign key to receipts.receipt_id)
        - waiter_name: VARCHAR(16) (primary key)

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += str(tuple(row)) + "\n"
    return output.strip()


agent = CodeAgent(
    tools=[sql_engine],
    model=InferenceClientModel("meta-llama/Meta-Llama-3-8B-Instruct", token=HF_API_KEY),
)

agent.run("Which waiter got the highest tip percentage?")