import os
import sqlite3
import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyDNwP-ueLjKVZRoC8qy7zoGZiZTHAbLZgw')

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

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name students and has the following columns - Student_ID,	Name,	Gender,	Age,	GPA,	Major,	Interested_Domain,	Projects,	Future_Career,	Python,	SQL,	Java
     \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM students ;
    \nExample 2 - Tell me all the students studying in Computer Science Major?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where Major="Computer Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """

]
# Set page configuration
st.set_page_config(page_title="I can Retrieve Any SQL query")

# Apply dark theme
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

# Header
st.header("Gemini App To Retrieve SQL Data")

# Input field
question = st.text_input("Input: ", key="input")

# Submit button
submit = st.button("Ask the question")

# Handle submit action
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "students.db")
    single_array = [item for sublist in response for item in sublist]
    st.subheader("The Response is")
    st.write(single_array)
