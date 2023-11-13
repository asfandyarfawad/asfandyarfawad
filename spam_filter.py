import streamlit as st
import pickle
import pandas as pd
import re




# all data
with open('p_spam.pkl', 'rb') as file:
    p_spam = pickle.load(file)
with open('p_ham.pkl', 'rb') as file:
    p_ham = pickle.load(file)
with open('parameters_spam.pkl', 'rb') as file:
    parameters_spam = pickle.load(file)
with open('parameters_ham.pkl', 'rb') as file:
    parameters_ham = pickle.load(file)



# the main filter which will classify the new msg
def classify(message):
    """
    message: a string
    """
    
    message = re.sub("\W"," ", message)
    message = message.lower().split()
    
    p_spam_given_messeage = p_spam
    p_ham_given_messeage = p_ham
    
    for word in message:
        if word in parameters_spam:
            p_spam_given_messeage *= parameters_spam[word]
            
        if word in parameters_ham:
            p_ham_given_messeage *= parameters_ham[word]
            
    if p_ham_given_messeage > p_spam_given_messeage:
        return "ham"
    elif p_ham_given_messeage < p_spam_given_messeage:
        return "SPAM !"
    else:
        return "needs human classification"



st.set_page_config(page_title="SPAM CHECKER",
                   page_icon="📬")
    

st.title("📬 SPAM CHECKER")
st.markdown("##")



st.markdown('<p style="font-size: 20px">Enter the message:</p>', unsafe_allow_html=True)

# Create a text input
user_input = st.text_input("")



if user_input:
    # Apply the function to the user input
    result = classify(user_input)

    # Display the result
    st.write("This Message is ", result)








hide_st_style= """
                <style>
                #MainMenu {visibility:hidden;}
                footer {visibility:hidden;}
                header {visibility:hidden;}
                </style>"""

st.markdown(hide_st_style,unsafe_allow_html=True)