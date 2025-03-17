import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="todo_fastapi"
)

mycursor = mydb.cursor()