import sqlite3
con = sqlite3.connect("Mundo_da_Josy.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE clientes ")