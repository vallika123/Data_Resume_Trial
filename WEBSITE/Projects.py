
import streamlit as st
from pathlib import Path 
import base64
from PIL import Image

st.title("Projects Page")
st.subheader("PROJECTS")

#-----PROJECT 1
st.subheader("NBA players Line Up Prediction")
# Upload the PDF file

current_dir=Path(__file__).parent  if "__file__" in locals() else Path.cwd()
Paper1 = current_dir / "Final Report_project.pdf"
Ppt1 = current_dir / "Project_data mining .pdf"
with open(Paper1,"rb") as pdf_file:
    PDFbyte_1=pdf_file.read()
with open(Ppt1,"rb") as pdf_file:
    PDFbyte_2=pdf_file.read()
    
pdf_base64_1 = base64.b64encode(PDFbyte_1).decode('utf-8')
pdf_base64_2 = base64.b64encode(PDFbyte_2).decode('utf-8')

st.markdown(f"""
        <style>
            .fixed-panel {{
               
                word-wrap: break-word; /* Ensures long words or lines break appropriately */
                white-space: normal; /* Allows text to wrap normally */
                overflow-wrap: break-word; /* Fallback for older browsers */
            }}
        </style>
        <div class='fixed-panel'>
        <p style='margin-bottom: 5px;'>
        In sports, predicting a team's lineup is crucial for determining the match outcome. Through trial and error and Feature Selection, Feature Transformation, Classification Models (SVM, Logistic Regression, Gradient Boosting, Neural Networks and Random Forest), and Embeddings for text data, we (a team of 2) acquired 79% accuracy using Random Forest. The Problem Statements addressed in this paper would be: <br>
        1) When provided with five home team players' names and five away team players' names, predict the outcome of the game.<br>
        2) When four away team players and five home team players are given, predict the fifth player in the lineup and predict the fifth player in the lineup to enhance the likelihood of the away team winning.<br>
        </p>
        <br>
        </div>
    """, unsafe_allow_html=True) 

view_option = st.selectbox(
    'To view documents:',
    ['Collapse', 'View PDF']
)
    # Create two columns: one for the PDF preview, one for the description
col1,col2 = st.columns(2, gap="large")
if view_option == 'View PDF':   
    with col1:
        st.markdown(f"""
        <style>
         .scrollable-block {{
        max-width: 100%; /* Adjust width as needed */
        height: 600px; /* Fixed height for the block */
        overflow: auto; /* Enable scrolling if content overflows */
        border: 1px solid #ccc; /* Optional border for the block */
        }}
        iframe {{
        width: 100%; /* Make the iframe fill the width of the container */
        height: 100%; /* Make the iframe fill the height of the container */
        border: none; /* Remove iframe border */
        }}
        </style>
    
        <div class='scrollable-block'>
        <iframe src="data:application/pdf;base64,{pdf_base64_1}" 
        type="application/pdf"></iframe>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <style>
        .scrollable-block {{
        max-width: 100%; /* Adjust width as needed */
        height: 600px; /* Fixed height for the block */
        overflow: auto; /* Enable scrolling if content overflows */
        border: 1px solid #ccc; /* Optional border for the block */
        }}
        iframe {{
        width: 100%; /* Make the iframe fill the width of the container */
        height: 100%; /* Make the iframe fill the height of the container */
        border: none; /* Remove iframe border */
         }}
        </style>
    
        <div class='scrollable-block'>
        <iframe src="data:application/pdf;base64,{pdf_base64_2}" 
        type="application/pdf"></iframe>
        </div>
        """, unsafe_allow_html=True)



#-----PROJECT 1
st.subheader("NBA players Line Up Prediction")
# Upload the PDF file
current_dir=Path(__file__).parent  if "__file__" in locals() else Path.cwd()
Paper1 = current_dir / "Final Report_project.pdf"
Ppt1 = current_dir / "Project_data mining .pdf"
with open(Paper1,"rb") as pdf_file:
    PDFbyte_1=pdf_file.read()
with open(Ppt1,"rb") as pdf_file:
    PDFbyte_2=pdf_file.read()
    
pdf_base64_1 = base64.b64encode(PDFbyte_1).decode('utf-8')
pdf_base64_2 = base64.b64encode(PDFbyte_2).decode('utf-8')

st.markdown(f"""
        <style>
            .fixed-panel {{
                max-width: 1200px; /* Sets maximum width for the panel */
                word-wrap: break-word; /* Ensures long words or lines break appropriately */
                white-space: normal; /* Allows text to wrap normally */
                overflow-wrap: break-word; /* Fallback for older browsers */
            }}
        </style>
        <div class='fixed-panel'>
        <p style='margin-bottom: 5px;'>
        In sports, predicting a team's lineup is crucial for determining the match outcome. Through trial and error and Feature Selection, Feature Transformation, Classification Models (SVM, Logistic Regression, Gradient Boosting, Neural Networks and Random Forest), and Embeddings for text data, we (a team of 2) acquired 79% accuracy using Random Forest. The Problem Statements addressed in this paper would be: <br>
        1) When provided with five home team players' names and five away team players' names, predict the outcome of the game.<br>
        2) When four away team players and five home team players are given, predict the fifth player in the lineup and predict the fifth player in the lineup to enhance the likelihood of the away team winning.<br>
        </p>
        <br>
        </div>
    """, unsafe_allow_html=True) 

