# ETL Pipeline – Ceny mieszkań w Polsce (2023)

Ten projekt to przykładowy pipeline ETL (Extract–Transform–Load) napisany w Pythonie. Celem jest analiza cen nieruchomości w polskich miastach.

# Technologie

- Python
- Pandas
- SQLite
- Matplotlib

# Kroki ETL

1. **Extract** – załadowanie danych z pliku CSV (np. dane z NBP lub Otodom)
2. **Transform** – czyszczenie i przygotowanie danych
3. **Load** – zapis danych do lokalnej bazy SQLite
4. **Analiza** – wyciągnięcie średnich cen m2 w 2023 roku
5. **Wizualizacja** – wykres Top 10 miast wg ceny m2

# Plik wejściowy (`real_estate_data.csv`)

Plik powinien zawierać kolumny:
- `Miasto`
- `Rok`
- `Kwartal`
- `Cena_m2`

Przykład:
```csv
Miasto,Rok,Kwartal,Cena_m2
Warszawa,2023,1,12500
Kraków,2023,1,11300
...
