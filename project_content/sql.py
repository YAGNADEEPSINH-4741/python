import sqlite3

# Connect to database (creates file if it does not exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    marks INTEGER
)
""")

# INSERT (Create)
cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", ("Rahul", 20, 85))
cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", ("Yagna", 21, 90))

conn.commit()

# SELECT (Read)
print("Student Records:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# UPDATE
cursor.execute("UPDATE students SET marks = 95 WHERE name = 'Yagna'")
conn.commit()

print("\nAfter Update:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# DELETE
cursor.execute("DELETE FROM students WHERE name = 'Rahul'")
conn.commit()

print("\nAfter Delete:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()