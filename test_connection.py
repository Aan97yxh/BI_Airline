
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, URL

load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

engine = create_engine(url)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version()"))
        print("KONEKSI BERHASIL!")
        print(result.scalar())

except Exception as e:
    print("KONEKSI GAGAL!")
    print(e)

finally:
    engine.dispose()
