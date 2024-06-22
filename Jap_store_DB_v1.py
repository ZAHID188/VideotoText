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

def jp_insert_into_database(vid_D,vid_t,jap_t,en_t,zh_t):
    sql = "INSERT INTO All_Text (vid_directory,vid_tittle, Jap_text,en_text,cn_text) VALUES (%s, %s, %s,%s,%s)"
    values = (vid_D,vid_t,jap_t,en_t,zh_t)
    cursor.execute(sql, values)
    db.commit()
    db.close()
    print("Data inserted successfully!")


def jp_get_value(x):
    # Execute the SQL query
    query = "SELECT * FROM All_Text WHERE vid_tittle = %s"
    values = (x,)
    cursor.execute(query,values)
    # Fetch the results
    results = cursor.fetchall()
    # Print the results
    # for row in results:
    #     print(f"ID: {row[0]}")
    #     print(f"Video Directory: {row[1]}")
    #     print(f"Video Title: {row[2]}")
    #     print(f"Japanese Text: {row[3]}")
        

    db.close()
    return results


# NewdatabaseCreate()
# jp_insert_into_database('sasd','sasd','sasd')
# jp_get_value('vid1.mp4')