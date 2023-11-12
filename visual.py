import pandas as pd
import numpy as np
import streamlit as st
import pickle


def org_count(person_name):
    person_name = str(person_name)
    name_ref = df[df['Name'] == person_name]['Organization'].unique()
    unique_counts = np.unique(name_ref, return_counts=True)[1]
    return unique_counts.sum()

def customer_count(person_name):
    cond_1 = df[df['Customer\nName 1'].notnull()]
    name_ref_1 = cond_1[cond_1['Name'] == person_name]['Customer\nName 1'].unique()
    name_ref_1 = name_ref_1.astype(str)
    unique_count = np.unique(name_ref_1, return_counts=True)[1]
    return unique_count.sum()
def visits(person_name):
    no_of_visits = df[df['Name']==person_name]['Organization'].count()
    return no_of_visits

st.set_page_config(page_title="Weekly Visits Report",
                   page_icon=":bar_chart:", layout='wide')

with open('new_data.pkl', 'rb') as file:
    df = pickle.load(file)




# # Name filter

# st.sidebar.header("Please Filter Here:")
# name = st.sidebar.selectbox(
#     "Select Person Name:",
#     options=df['Name'].unique()
# )

# # Organization Filter

# org = st.sidebar.multiselect(
#     "Organization:",
#     options=df['Organization'].unique(),
#     default=df['Organization'].unique()
# )

# # Date Filter

# date = st.sidebar.multiselect(
#     "Date:",
#     options=df['Date'].unique()
# )


# df_selection = df.query(
#     "Name == @name & Organization==@org & Date==@date"
# )

##### code from gpt

st.sidebar.header("Please Filter Here:")
name = st.sidebar.selectbox(
    "Select Person Name:",
    options=['All'] + list(df['Name'].unique())  # Include 'All' as an option
)

# Organization Filter

org = st.sidebar.multiselect(
    "Organization:",
    options=['All'] + list(df['Organization'].unique()),  # Include 'All' as an option
    default=['All']  # Set 'All' as the default
)

# Date Filter

date = st.sidebar.multiselect(
    "Date:",
    options=['All'] + list(df['Date'].unique()),  # Include 'All' as an option
    default=['All']  # Set 'All' as the default
)

# Filter the DataFrame based on selected filters
df_selection = df

if name != 'All':
    df_selection = df_selection[df_selection['Name'] == name]

if org != ['All']:
    df_selection = df_selection[df_selection['Organization'].isin(org)]

if date != ['All']:
    df_selection = df_selection[df_selection['Date'].isin(date)]

########## ends

st.title(":bar_chart: Weekly Visits Report")
st.markdown("##")






left_column, middle_column,right_column  = st.columns(3)

with left_column:
    st.markdown("<p style='text-align:center; font-size: 30px;'>Total No. Of visits</p>", unsafe_allow_html=True)
    if name:
        selected_name_1 = name  # Assuming you are interested in the first selection if multiple selections are possible
        no_of_visits = visits(selected_name_1)
        st.markdown(f"<p style='text-align: center; font-size: 30px;'>{no_of_visits}</p>", unsafe_allow_html=True)

with middle_column:
    st.markdown("<p style='text-align:center; font-size: 30px;'>No. Of Organization visit:</p>", unsafe_allow_html=True)
    if name:
        selected_name = name  # Assuming you are interested in the first selection if multiple selections are possible
        org_count_result = org_count(selected_name)
        st.markdown(f"<p style='text-align: center; font-size: 30px;'>{org_count_result}</p>", unsafe_allow_html=True)

with right_column:
    st.markdown("<p style='text-align:center; font-size: 30px;'>No. Of Doctors visit:</p>", unsafe_allow_html=True)
    if name:
        select_name = name  # Assuming you are interested in the first selection if multiple selections are possible
        client_count = customer_count(select_name)
        st.markdown(f"<p style='text-align: center; font-size: 30px;'>{client_count}</p>", unsafe_allow_html=True)



st.table(df_selection.rename({"Customer\nName 1":'Name of Doctor', 'Comments':'COMMENTS'}, axis=1)[['Date','Organization','Name of Doctor']])



hide_st_style= """
                <style>
                #MainMenu {visibility:hidden;}
                footer {visibility:hidden;}
                header {visibility:hidden;}
                </style>"""

st.markdown(hide_st_style,unsafe_allow_html=True)