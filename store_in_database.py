import mysql.connector




# ----
db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="zahid",
    password="1234",
    database="VIDEO_TO_TEXT"
)

# Get a cursor object to execute SQL queries
cursor = db.cursor()
cursor.execute("""
  CREATE TABLE IF NOT EXISTS translations(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key', 
    original_Jap TEXT,
    english TEXT,
    chinese TEXT);""")

# Define the data to be inserted
jap = "jajajajajaja"
eng = "eeeee"
cn="casda"

# Prepare the SQL query
sql = "INSERT INTO translations (original_Jap, english, chinese) VALUES (%s, %s,%s)"
values = (jap,eng,cn)

# Execute the SQL query
cursor.execute(sql, values)

# Commit the changes and close the connection
db.commit()
db.close()

print("Data inserted successfully!")


# ------


'''

translations = [
    {'original': 'Hello, how are you?', 'translated': 'こんにちは、調子はどうですか?'},
    {'original': 'I like dogs.', 'translated': '私は犬が好きです。'},
    {'original': 'The weather is nice today.', 'translated': '今日の天気はいいですね。'}]
def store_in_mysql(translations):
    conn = mysql.connector.connect(
        host="Localhost",
        user="zahid",
        password="1234",
        database="VIDEO_TO_TEXT"
    )
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS translations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        original TEXT,
        english TEXT,
        chinese TEXT
    )
    """)
    for t in translations:
        cursor.execute("""
        INSERT INTO translations (original)
        VALUES (%s,)
        """, (t['original']))
    conn.commit()
    cursor.close()
    conn.close()

store_in_mysql(translations)

'''