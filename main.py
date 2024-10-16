import os
import sqlite3
import streamlit as st
import google.generativeai as genai
import pandas as pd 

genai.configure(api_key={apikey})

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text
    
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = [
    """
    You're an expert in converting English questions into SQL queries! 
    The SQL database is named "students" and has the following columns: 
    Student_ID, Name, Gender, Age, GPA, Major, Interested_Domain, Projects, Future_Career, Python, SQL, Java.

    Examples:
    1. If the question is "How many entries of records are present?", 
       the SQL query would be: SELECT COUNT(*) FROM students;

    2. If the question is "Tell me all the students studying in Computer Science Major?", 
       the SQL query would be: SELECT * FROM students WHERE Major = "Computer Science";

    Note: Don't include SQL keywords in the output, and make sure the SQL code doesn't have backticks (`) at the beginning or end.
    """
]

st.set_page_config(page_title="Gemini App: Retrieve Any SQL Query")

st.markdown(
    """
    <style>
    .css-18e3th9 {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .css-1d391kg {
        background-color: #1e1e1e;
    }
    .css-1cpxqw2 {
        color: #ffffff;
    }
    .css-1v3fvcr {
        color: #ffffff;
    }
    .css-1v3fvcr:hover {
        color: #ffffff;
    }
    .css-1v3fvcr:focus {
        color: #ffffff;
    }
    .css-1v3fvcr:active {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Talk to database")

question = st.text_input("What's your query? (e.g., How many students are there?)", key="input")
submit = st.button("Ask the Question")

if submit:
    response = get_gemini_response(question, prompt)
    response = read_sql_query(response, "students.db")
    
    df = pd.DataFrame(response, columns=['Student_ID', 'Name', 'Gender', 'Age', 'GPA', 'Major', 'Interested_Domain', 'Projects', 'Future_Career', 'Python', 'SQL', 'Java'])
    
    st.subheader("Here's your SQL Query Result:")
    st.table(df)
