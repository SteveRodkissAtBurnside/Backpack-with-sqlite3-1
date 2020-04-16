'''Write your project here or copy and paste your code from VSCode and test it here to make sure it works- note this is an experiment and is optional. Don't stress if it isn't working!    :) '''

import sqlite3

DATABASE_FILENAME = "backpack.db"
db = None

def get_db():
  #connect and return the db if it doesn't already exist
  global db
  if db==None:
     db = sqlite3.connect(DATABASE_FILENAME)
  return db

def close_db():
  #close connection if it exists
  global db
  if db != None:
    db.close()

def create_table():
  #create the contents table
  cursor = get_db().cursor()
  sql = 'CREATE TABLE contents(id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT(30));'
  cursor.execute(sql)

def print_contents():
  #print all the contents of the database
  cursor = get_db().cursor()
  cursor.execute("SELECT * FROM contents")
  results = cursor.fetchall()
  print(results)

def insert_item(item_name):
  #put an item into contents
  cursor = get_db().cursor()
  sql = "INSERT INTO contents (item_name) VALUES (?)"
  cursor.execute(sql,(item_name,))





