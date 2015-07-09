import MySQLdb
import sys
from secret import config

# Database configuration saved in secret.py
# The secret.py file should contain something like this
# config = {
#     'host': 'localhost',
#     'user': 'root',
#     'passwd': 'SECRET',
# }
def assays_db():
    """
    Connect to MySQL, and attempt to create or select the assays database.
    Then, create a new, blank assays table, and return it.
    """
    db = MySQLdb.connect(**config)
    cursor = db.cursor()
    # Seelct DB, or create if none exists.
    try:
        db.select_db('assays')        
    except:
        # Create a database
        try:
            cursor.execute("CREATE DATABASE assays;")
            db.select_db('assays')
        except:
            print "Database creation or selection failed."
            sys.exit(1)
        

    # Create a blank table to store lab data.
    try:
        cursor.execute("DROP TABLE IF EXISTS assays;")
        cursor.execute("""
            CREATE TABLE assays (
                certificate VARCHAR(20) NOT NULL,
                sample_id VARCHAR(20) NOT NULL,
                material VARCHAR(20) NOT NULL,
                method VARCHAR(20),
                units VARCHAR(10),
                run INT,
                value DECIMAL(13,5)   
            );
        """)
    except:
        print "Unable to create a new assays table."
        sys.exit(1)
    
    return cursor
