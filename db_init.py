import sqlite3, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", required=True)
args = parser.parse_args()

conn = sqlite3.connect(args.path)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS workouts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date TEXT,
  exercise TEXT,
  weight REAL,
  reps INTEGER
)
""")
conn.commit()
conn.close()
