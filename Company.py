import streamlit as st
import pandas


# cf = pandas.read_csv("data.csv", sep=",")
def cf_iterator(i=0, j=12):
    cf = pandas.read_csv("data.csv")
    for index, row in cf[i:j].iterrows():
        name = row["first name"].title() + " " + \
               row["last name"].title()
        st.header(name)
        st.subheader(row["role"])
        imgpath = "images/" + row["image"]
        st.image(imgpath)


st.set_page_config(layout="wide")

st.title("The Best Company")

content = """ This is a startup started by Vaishnav Nigade and Navyam Raushan. 
            We provide so many IT sevices, and we want to introduce our team and 
            pople who make our goal a success."""
st.info(content)
st.header("Our Team")

col1, empty_col1, col2, empty_col2, col3 = \
                                    st.columns([1, 0.1, 1, 0.1, 1])
# cf means company file


with col1:
    cf_iterator(0, 4)

with col2:
    cf_iterator(4, 8)

with col3:
    cf_iterator(8, 12)
