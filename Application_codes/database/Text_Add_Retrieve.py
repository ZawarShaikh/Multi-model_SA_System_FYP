import sqlite3



# !------------------- Functions for retrieval --------------------------!
# Function to get all info from the database
def get_all_text_info():
    # Connect to the database
    conn = sqlite3.connect('MSA_Prod_Rev_database.db')
    cur = conn.cursor()

    # Execute a query to fetch all users
    cur.execute('SELECT * FROM text_reviews')
    rows = cur.fetchall()

    # Close the connection
    conn.close()

    return rows

# Function to get all file loc from the database
def get_all_text_files_info():
    # Connect to the database
    conn = sqlite3.connect('MSA_Prod_Rev_database.db')
    cur = conn.cursor()

    # Execute a query to fetch all users
    cur.execute('SELECT * FROM text_file_location')
    rows = cur.fetchall()

    # Close the connection
    conn.close()

    return rows



# !------------------- Functions to add data ------------------------!
# Function to add info into database
def add_text_info(pid, review, sentiment, sentiment_number):
    # Connect to the database
    conn = sqlite3.connect('MSA_Prod_Rev_database.db')
    cur = conn.cursor()

    # Insert a new user
    cur.execute('''
        INSERT INTO text_reviews (pid, review, sentiment, sentiment_number)
        VALUES (?, ?, ?, ?)
    ''', (pid, review, sentiment, sentiment_number))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
# Function to add file location into the database
def add_text_file(pid, file_loc):
    # Connect to the database
    conn = sqlite3.connect('MSA_Prod_Rev_database.db')
    cur = conn.cursor()

    # Insert a new users
    cur.execute('''
        INSERT INTO text_file_location (pid, text_file_loc)
        VALUES (?, ?)
    ''', (pid, (file_loc, ))
    )
    # Commit the changes and close the connection
    conn.commit()
    conn.close()




if __name__ == "__main__":
    # Add a new user
    #add_text_info('This product is just fine', 'neutral', 2)
    #add_text_file('./Application_codes/text_file_uploads/Balanced_final_valid_data.csv')
    
    
    # Get and print all single texts
    users = get_all_text_info()
    for user in users:
        print(f'Snngle Text: {user}')
        
    # Get and print all uploaded text files
    file_info = get_all_text_files_info()
    for file in file_info:
        print(f'File Locations: {file}')
