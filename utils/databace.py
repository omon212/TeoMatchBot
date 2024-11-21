import sqlite3
import random

connect = sqlite3.connect("./user_data.db")
cursor = connect.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY,
          user_id INTEGER,
          age INTEGER NULL,
          gender TEXT NULL,
          lfgender TEXT NULL,
          city TEXT NULL,
          name TEXT NULL,
          description TEXT NULL,
          photo1 TEXT NULL,
          photo2 TEXT NULL,
          photo3 TEXT NULL,
          likes TEXT NULL,
          language TEXT NUll,
          instagram_username TEXT NULL
          )""")


async def save_age(user_id, age):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute("UPDATE users SET age = ? WHERE user_id = ?", (age, user_id))
    else:
        cursor.execute("INSERT INTO users (user_id, age) VALUES (?, ?)", (user_id, age))
    connect.commit()


async def save_gender(user_id, gender):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute("UPDATE users SET gender = ? WHERE user_id = ?", (gender, user_id))
    else:
        cursor.execute("INSERT INTO users (user_id, gender) VALUES (?, ?)", (user_id, gender))
    connect.commit()


async def save_lfgender(user_id, lfgender):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute("UPDATE users SET lfgender = ? WHERE user_id = ?", (lfgender, user_id))
    else:
        cursor.execute("INSERT INTO users (user_id, lfgender) VALUES (?, ?)", (user_id, lfgender))
    connect.commit()


async def save_city(user_id, city):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute("UPDATE users SET city = ? WHERE user_id = ?", (city, user_id))
    else:
        cursor.execute("INSERT INTO users (user_id, city) VALUES (?, ?)", (user_id, city))
    connect.commit()


async def save_name(user_id, name):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id))
    else:
        cursor.execute("INSERT INTO users (user_id, name) VALUES (?, ?)", (user_id, name))
    connect.commit()


async def save_description(user_id, description):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute("UPDATE users SET description = ? WHERE user_id = ?", (description, user_id))
    else:
        cursor.execute("INSERT INTO users (user_id, description) VALUES (?, ?)", (user_id, description))
    connect.commit()


async def save_photo(user_id, photo1):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute("UPDATE users SET photo1 = ? WHERE user_id = ?", (photo1, user_id))
    else:
        cursor.execute("INSERT INTO users (user_id, photo1) VALUES (?, ?)",
                       (user_id, photo1))
    connect.commit()


async def user_data(user_id, ):
    user = cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    return user


async def check_user(user_id, ):
    user = cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    if user:
        return user
    else:
        return False


async def select_random():
    cursor.execute("SELECT id FROM users WHERE photo1 IS NOT NULL")
    valid_user_ids = [row[0] for row in cursor.fetchall()]

    if not valid_user_ids:
        return "404"
    else:
        random_id = random.choice(valid_user_ids)
        cursor.execute("SELECT * FROM users WHERE id = ?", (random_id,))
        user_data = cursor.fetchone()
        return user_data if user_data else "404"
