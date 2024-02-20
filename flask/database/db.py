import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('example.db',check_same_thread=False)
c = conn.cursor()

# Tabloyu oluştur
c.execute('''CREATE TABLE IF NOT EXISTS text (
                id INTEGER PRIMARY KEY,
                sentence TEXT NOT NULL,
                predict TEXT NOT NULL)''')

# Yeni veri ekle
def add_user(sentence, predict):
    c.execute("INSERT INTO text (sentence, predict) VALUES (?, ?)", (sentence, predict))
    conn.commit()

# Tüm veriyi listele
def list_users():
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    user_list = []
    for user in users:
        user_list.append(user)
    return user_list

