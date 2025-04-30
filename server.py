# server.py
from mcp.server.fastmcp import FastMCP  # Use FastMCP instead of stdio helper
import sqlite3, os, asyncio

# Initialize server instance
mcp = FastMCP("Workout Planner")

# DB setup
DB_PATH = os.getenv("DB_PATH", "data/workouts.db")
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
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

# Define tool for adding a workout
@mcp.tool()
async def add_plan(params: dict):
    c.execute(
      "INSERT INTO workouts (date,exercise,weight,reps) VALUES (?,?,?,?)",
      (params["date"], params["exercise"], params["weight"], params["reps"])
    )
    conn.commit()
    return {"status":"ok", "message":"Plan added"}

# Define tool for fetching plans
@mcp.tool()
async def get_plans(params: dict):
    c.execute(
      "SELECT date,exercise,weight,reps FROM workouts WHERE date BETWEEN ? AND ?",
      (params["start_date"], params["end_date"])
    )
    rows = c.fetchall()
    return {"plans":[{"date":r[0],"exercise":r[1],"weight":r[2],"reps":r[3]} for r in rows]}

if __name__ == "__main__":
    # Launch stdio transport directly via FastMCP
    mcp.run(transport="stdio")
