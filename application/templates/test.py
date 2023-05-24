import pickle
import streamlit as st

st.set_page_config(page_title="Art Classifier")

trained_model = pickle.load(open(decision_tree_model.pkl, 'rb'))

# Header section
#st.subheader("This is a subheader")
st.title("Art Genre Classifier")
#st.write("Upload an image here to classify the genre")
uploaded_file = st.file_uploader("Upload an image here to classify the genre", type=['png', 'jpeg', 'jgp'])
