import sqlite3



# !------------------- Functions for retrieval --------------------------!
# Function to get all info from the database
def get_all_audio_info():
    # Connect to the database
    conn = sqlite3.connect('MSA_Prod_Rev_database.db')
    cur = conn.cursor()

    # Execute a query to fetch all users
    cur.execute('SELECT * FROM audio_file_location')
    rows = cur.fetchall()

    # Close the connection
    conn.close()

    return rows

# Function to get all file loc from the database
def get_all_folder_info():
    # Connect to the database
    conn = sqlite3.connect('MSA_Prod_Rev_database.db')
    cur = conn.cursor()

    # Execute a query to fetch all users
    cur.execute('SELECT * FROM audio_folder_location')
    rows = cur.fetchall()

    # Close the connection
    conn.close()

    return rows



# !------------------- Functions to add data ------------------------!
# Function to add info into database
def add_audio_info(pid, audio_file):
    # Connect to the database
    conn = sqlite3.connect('MSA_Prod_Rev_database.db')
    cur = conn.cursor()

    # Insert a new user
    cur.execute('''
        INSERT INTO audio_file_location (pid, audio_file_loc)
        VALUES (?, ?)
    ''', (pid, (audio_file, ))
    )
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
# Function to add folder location into the database
def add_audio_folder(pid, folder_loc):
    # Connect to the database
    conn = sqlite3.connect('MSA_Prod_Rev_database.db')
    cur = conn.cursor()

    # Insert a new users
    cur.execute('''
        INSERT INTO audio_folder_location (pid, audio_folder_loc)
        VALUES (?, ?)
    ''', (pid, (folder_loc, ))
    )
    # Commit the changes and close the connection
    conn.commit()
    conn.close()




if __name__ == "__main__":
    # Add a new user
    #add_text_info('This product is just fine', 'neutral', 2)
    #add_text_file('./Application_codes/text_file_uploads/Balanced_final_valid_data.csv')
    
    
    # Get and print all single texts
    users = get_all_audio_info()
    for user in users:
        print(f'Uploaded and Recordrd Audios: {user}')
        
    # Get and print all uploaded text files
    file_info = get_all_folder_info()
    for file in file_info:
        print(f'File Locations: {file}')
