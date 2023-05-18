import streamlit as st
from google.cloud import firestore

st.header('Hello 🌎!')
if st.button('Balloons?'):
    st.balloons()


# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")


# Now let's make a reference to ALL of the posts
posts_ref = db.collection("posts")

# For a reference to a collection, we use .stream() instead of .get()
for doc in posts_ref.stream():
    st.write("The id is: ", doc.id)
    st.write("The contents are: ", doc.to_dict())


# Streamlit widgets to let a user create a new post
title = st.text_input("Post title")
url = st.text_input("Post url")
submit = st.button("Submit new post")
