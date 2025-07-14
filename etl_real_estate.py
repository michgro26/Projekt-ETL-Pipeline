import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

CSV_FILE = "real_estate_data.csv"

# Tworzenie przykładowego pliku jeśli nie istnieje
def create_sample_csv():
    sample_data = pd.DataFrame({
        'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań'],
        'Rok': [2023]*5,
        'Kwartal': [1, 1, 1, 1, 1],
        'Cena_m2': [13000, 11500, 11200, 11000, 10500]
    })
    sample_data.to_csv(CSV_FILE, index=False)
    print(f"📄 Przykładowy plik '{CSV_FILE}' został utworzony.")

if not os.path.exists(CSV_FILE):
    print(f"⚠️ Plik '{CSV_FILE}' nie istnieje. Tworzę przykładowy...")
    create_sample_csv()

# === ETL ===
df = pd.read_csv(CSV_FILE)
df.columns = df.columns.str.strip().str.lower()
df.rename(columns={'miasto': 'city', 'rok': 'year', 'kwartal': 'quarter', 'cena_m2': 'price_per_m2'}, inplace=True)
df.dropna(inplace=True)

conn = sqlite3.connect("real_estate.db")
df.to_sql("real_estate_prices", conn, if_exists="replace", index=False)

query = """
SELECT city, year, AVG(price_per_m2) as avg_price
FROM real_estate_prices
WHERE year = 2023
GROUP BY city, year
ORDER BY avg_price DESC
LIMIT 10
"""
result_df = pd.read_sql(query, conn)
print("\nTop 10 miast wg średniej ceny m2 (2023):")
print(result_df)

# Wizualizacja
if not result_df.empty:
    plt.figure(figsize=(10, 6))
    plt.bar(result_df['city'], result_df['avg_price'], color='teal')
    plt.title("Top 10 miast wg średniej ceny m2 (2023)")
    plt.xlabel("Miasto")
    plt.ylabel("Średnia cena za m2 [PLN]")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("top10_avg_prices.png")
    plt.show()

conn.close()
print("\n✅ Pipeline zakończony sukcesem.")
