from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI()

@app.get("/top10")
def get_top10():
    conn = sqlite3.connect("real_estate.db")
    query = """
        SELECT city, year, AVG(price_per_m2) as avg_price
        FROM real_estate_prices
        WHERE year = 2023
        GROUP BY city, year
        ORDER BY avg_price DESC
        LIMIT 10
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_dict(orient="records")
