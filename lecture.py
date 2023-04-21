from cs50 import SQL

db = SQL("sqlite:///merch.db")

rows = db.execute("SELECT * FROM registrants)

for row in rows:
    print(f"{row['name']} registered")