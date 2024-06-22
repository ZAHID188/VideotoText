import mysql.connector

db = mysql.connector.connect(
host="127.0.0.1",
port=3306,
user="zahid",
password="1234",
database="VIDEO_TO_TEXT"
)
cursor = db.cursor()


def NewdatabaseCreate():
    # Get a cursor object to execute SQL queries
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS All_Text(  
         id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary Key', 
         vid_directory TEXT,
         vid_tittle TEXT,
         Jap_text TEXT,
         en_text TEXT,
         cn_text TEXT);""")
    print("New Database Created")
    

def jp_insert_into_database(vid_D,vid_t,jap_t):
    # Prepare the SQL query
    sql = "INSERT INTO All_Text (vid_directory,vid_tittle, Jap_text) VALUES (%s, %s, %s)"
    values = (vid_D,vid_t,jap_t)
    # Execute the SQL query
    cursor.execute(sql, values)
    # Commit the changes and close the connection
    db.commit()
    db.close()
    print("Data inserted successfully!")

# NewdatabaseCreate()
# jp_insert_into_database()


