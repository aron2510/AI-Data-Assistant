import os
from keys.apikey import apikey
import streamlit as st
import pandas as pd
from langchain_community.llms import openai
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv,find_dotenv

#OpenAI key
os.environ['OPENAI_API_KEY']=apikey
load_dotenv(find_dotenv())


#llm model
llm = openai.OpenAI(temperature=0)  

#Main
st.title('AI Assistant🤖 for Data Science')
st.write('hello👋, I am your AI Assistant and I am here to help🤝 you with your data science projects.')

with st.sidebar:
    st.write('*Your Data Science Adventure🚶🏽 begins with an CSV file.❎*')
    st.caption('''**You may already know that every 
               exciting data science journey starts
               with a dataset🗂️.Once we hv ur data in 
               hand,we'll dive into understanding it 
               and hv some fun exploring it.Then we'll
               work together to shape ur business 
               challenge💼 into a data science framework.
               I'll introduce you to the coolest ml 
               models,and we'll use then to tackle 
               your problem🚩.Sounds fun right?🤩**''')
    
    

    
    st.divider()

    st.caption("<p style='text-align:center'>Made with love by Aron</p>",unsafe_allow_html=True)

#Initialize the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked={1:False}

#Function to update the value in session state
def clicked(button):
    st.session_state.clicked[button]=True
st.button("Let's get started",on_click=clicked,args=[1])
if st.session_state.clicked[1]:
    st.header('Exploratory Data Analysis Part')
    st.subheader('Solution')
    user_csv=st.file_uploader("Upload your file here",type="csv")

    if user_csv is not None:
        user_csv.seek(0)
        df=pd.read_csv(user_csv,low_memory=False)

with st.sidebar:
    with st.expander('What are the steps of EDA?'):
        st.write(llm('What are the steps of EDA?'))

pandas_agent=create_pandas_dataframe_agent(llm,df,verbose=True)
question='What is the meaning of the columns'
     
