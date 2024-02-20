import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('example.db',check_same_thread=False)
c = conn.cursor()

# Tabloyu oluştur
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL)''')

# Yeni veri ekle
def add_user(name, age):
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

# Tüm veriyi listele
def list_users():
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    user_list = []
    for user in users:
        user_list.append(user)
    return user_list

