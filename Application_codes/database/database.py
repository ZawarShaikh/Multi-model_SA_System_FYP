import sqlite3



def create_database():
    # Connect to SQLite database (or create one if it doesn't exist)
    conn = sqlite3.connect('MSA_Prod_Rev_database.db')

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # !------------------- Text Tables ----------------------!
    # Single text input table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS text_reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pid INTEGER NOT NULL, 
            review TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            sentiment_number INTEGER NOT NULL
        )
    ''')
    
    # Text File input table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS text_file_location (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pid INTEGER NOT NULL, 
            text_file_loc LONG TEXT NOT NULL
        )
    ''')
    
    
    
    # !----------------- Audio Tables ------------------!
    # single audio file loc
    cur.execute('''
        CREATE TABLE IF NOT EXISTS audio_file_location (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pid INTEGER NOT NULL,
            audio_file_loc TEXT NOT NULL
        )
    ''')

    # audio folder loc
    cur.execute('''
        CREATE TABLE IF NOT EXISTS audio_folder_location (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pid INTEGER NOT NULL,
            audio_folder_loc TEXT NOT NULL
        )
    ''')


    # Commit the changes to the database
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()