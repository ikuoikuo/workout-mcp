#!/usr/bin/env bash
python db_init.py --path /app/data/workouts.db
exec python server.py --db /app/data/workouts.db
