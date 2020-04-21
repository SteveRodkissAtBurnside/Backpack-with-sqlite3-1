'''Write your project here or copy and paste your code from VSCode and test it here to make sure it works- note this is an experiment and is optional. Don't stress if it isn't working!    :) '''

import sqlite3

DATABASE_FILENAME = "backpack.db"

def initialize_database():
  '''Initialise my custom database table(s) if not already created with sqlite studio!!!'''
  with sqlite3.connect(DATABASE_FILENAME) as db:
    cursor = db.cursor()
    sql='CREATE TABLE contents(id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT(30));'
    cursor.execute(sql)
    db.commit()
  

def get_contents(db):
  #print all the contents of the database
  cursor = db.cursor()
  cursor.execute("SELECT * FROM contents")
  return cursor.fetchall()

def insert_item(db, item_name):
  #put an item into contents
  cursor = db.cursor()
  sql = "INSERT INTO contents (item_name) VALUES (?)"
  cursor.execute(sql,(item_name,))

def delete_item(db, item_name):
  '''delete the item if it exists'''
  cursor = db.cursor()
  sql = "DELETE FROM contents WHERE item_name=?"
  cursor.execute(sql, (item_name, ))
  db.commit()

if __name__=="__main__":
  #main program starts here
  with sqlite3.connect(DATABASE_FILENAME) as db:
    while True:
      #ask for what you want to do
      user_input = input("What do you want to do?\n1. Print Contents\n2. Add an Item\n3. Delete an Item\n4. Exit\n")
      if user_input=="1":
        #print all contents
        print(get_contents(db))
      elif user_input=="2":
        item = input("What item do you want to add? ")
        insert_item(db,item)
      elif user_input=="3":
        item = input("What item do you want to delete? ")
        delete_item(db,item)
      elif user_input=="4":
        break
    

  



