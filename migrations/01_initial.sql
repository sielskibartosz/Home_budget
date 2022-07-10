CREATE TABLE category(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT
)

CREATE TABLE entry(
id INTEGER PRIMARY KEY AUTOINCREMENT,
category_id INTEGER,
name TEXT,
amount FLOAT,
created_at TIMESTAMP CURRENT_TIMESTAMP
)