import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    dbname="postgres",
    user="postgres",
    password="example"
)

cur = conn.cursor()

# Create a dummy table
cur.execute("""
    CREATE TABLE IF NOT EXISTS dummy (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        value INTEGER
    );
""")

conn.commit()
cur.close()
conn.close()