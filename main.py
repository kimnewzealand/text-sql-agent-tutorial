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
    Allows you to perform SQL queries on the table. Returns a string representation of the result.
    The table is named 'receipts'. Its description is as follows:
        Columns:
        - receipt_id: INTEGER
        - customer_name: VARCHAR(16)
        - price: FLOAT
        - tip: FLOAT

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output


agent = CodeAgent(
    tools=[sql_engine],
    model=InferenceClientModel("meta-llama/Meta-Llama-3-8B-Instruct", token=HF_API_KEY),
)

agent.run("Who got the highest tip percentage?")