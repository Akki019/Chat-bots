import streamlit as st
from streamlit_chat import message
from bardapi import Bard
import json 

with open('credentials.json','r') as f:
        file = json.load(f)
        token = file['token']

#Response from bot
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response

#FUNCTION TO RECIEVE USER QUERIES
def get_text():
    input_text= st.text_input('CN Bot', ' ', key='input')
    return input_text

# TITLE OF THE ATREAMLIT APP
st.title('Personal Tutoring Bot')

# url = 'https://images.unsplash.com/photo-1622099330140-69125ac0d6a9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'
# data-testid = "stAppViewContainer"

changes='''

<style>
[data-testid="stAppViewContainer"]
{
background-image : url('https://images.unsplash.com/photo-1622099330140-69125ac0d6a9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80');
background-size: cover;
}
</style>
'''
st.markdown(changes, unsafe_allow_html = True)

print(st.session_state)

if'generated' not in st.session_state:
    st.session_state['generated'] = []
    
if 'past' not in st.session_state:
    st.session_state['past']=[]


#ACCEPTING USER INPUT
user_input= get_text()
if user_input:
    print(user_input)
    output=generate_response (user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)


    if st.session_state['generated']:
        for i in range (len(st.session_state['generated']) -1, -1, -1):
            message(st.session_state['generated'][i], key=str(i))
            message(st.session_state['past'][i], key="user_"+str(i), is_user=True)