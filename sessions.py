import sqlite3
conn = sqlite3.connect('sessions.db')
cursor = conn.cursor()

def insert(mobile, origin = None, destination = None):
    """ Adds user to the database, always identifies via the mobile no. There is no requirement for an immediate location
    or destination"""
    
    cursor.execute('INSERT INTO sessions VALUES (?,?,?)', (mobile, origin, destination))
    conn.commit()

def add_origin(mobile, origin):
    """Adds the user's origin, finding the user via the mobile"""
    cursor.execute('UPDATE sessions SET origin = ? WHERE mobile == ? ', (origin, mobile))
    conn.commit()

def add_destination(mobile, destination):
    """ Adds the user's destination, finding the user via the mobile"""
    print type(destination)
    print type(mobile)
    cursor.execute('UPDATE sessions SET destination = ? WHERE mobile == ? ', (destination, mobile))
    conn.commit()

def retrive_data(mobile):
    """ Returns the User's information, finding the user via the mobile"""
    cursor.execute('SELECT * FROM sessions WHERE mobile == ?', (mobile,))
    return cursor.fetchone()
    
def delete(mobile):
    "Deletes all of the user's information, finding the user via the mobile"""
    cursor.execute('DELETE FROM sessions WHERE mobile == ?', (mobile,))
    conn.commit()
    
def save_time(mobile, req_time):
    #Finds the user via mobile, adds requested time
    cursor.execute('UPDATE sessions SET time = ? WHERE mobile == ?', (req_time, mobile))
    conn.commit()
