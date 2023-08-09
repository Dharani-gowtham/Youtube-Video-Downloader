import streamlit as st
import sqlite3

connection = sqlite3.connect("sample.db")
cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS "user" (
	"id" INTEGER NOT NULL UNIQUE,
	"username" TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
    );
    '''
)

username = st.text_input("Enter Your name")
if st.button("Add User"):
    cursor.execute(f"INSERT INTO user (username) values ('{username}')")
    st.success("User Added Successfully")
    connection.commit()

if st.button("Show Table"):
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    for row in rows:
        st.write(row)
