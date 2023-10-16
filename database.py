import sqlite3
import bcrypt  # CHANGE 

def setup_database():
    """
    Sets up our database. 
    """
    # Data
    connect_db = sqlite3.connect('users.db')

    cursor = connect_db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    connect_db.commit()
    connect_db.close()


def create_user(first_name, last_name, username, password):
    """
    Insert a new user into our database.
    """
    connect_db = sqlite3.connect('users.db')
    cursor = connect_db.cursor()

    try:
        cursor.execute("INSERT INTO users (first_name, last_name, username, password) VALUES (?, ?, ?, ?)", (first_name, last_name, username, password))
        connect_db.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        connect_db.close()
    return True


def get_all_users():
    """
    Retrieve all users from the database.
    """
    connect_db = sqlite3.connect('users.db')        
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()
    connect_db.close()

    return users


def get_user(username):
    """
    Get a user from the database using the username. 
    """
    connect_db = sqlite3.connect('users.db')        
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))

    user = cursor.fetchone()
    connect_db.close()

    return user


def get_user_by_id(id):
    """
    Get a user from the database using the id. 
    """
    connect_db = sqlite3.connect('users.db')        
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (id,))

    user = cursor.fetchone()
    connect_db.close()

    return user


# Not Login must be called from a URI
# NOTE: MAKE SURE THAT WE CAN ACCESS BCRYPT 
# CREATE OUR OWN HASH FUNCITON. 

# Look at flask. 
def hash_passwords(password):
    """
    Secure Our Login Screen 
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def check_password(password, hashed_password):
    """
    Checks a password against the hashed version of the 
    password. 
    """
    return bcrypt.checkpw(password.encode(), hashed_password)


#print(get_all_users())
# setup_database()
#print(create_user("Bob", "Johnson", "UserName", "Hello!"))
# create_user("adfs", "afsd", "UserNameTwo", "Hello!")
# create_user("adsf", "Johnlkjson", "UserNameFive", "Hello!")

# print(get_user("UserName"))
# print(get_user("UserNameTwo"))
# print(get_user("UserNameFive"))