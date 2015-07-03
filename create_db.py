import _mysql
import sys
from secret import config

# Database configuration saved in secret.py
# The secret.py file should contain something like this
# config = {
#     'host': 'localhost',
#     'user': 'root',
#     'passwd': 'SECRET',
# }

db = _mysql.connect(**config)

# Include logic to drop database if it exists already.
# ...

# Create a database
try:
    db.query("CREATE DATABASE assays;")
except:
    print "Databse creation failed."
    sys.exit(1)
    
assays_db = _mysql.connect(db='assays', **config)

# Create a table to store lab data.
try:
    assays_db.query("""
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
    print "Unable to create assays table."