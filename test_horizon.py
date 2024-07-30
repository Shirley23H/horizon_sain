import streamlit as st
import numpy as np
import joblib
import requests
import os
import tempfile

# Streamlit setup
st.set_page_config(
    page_title="HORIZON SAIN",
    layout="wide",
    page_icon='🧪'
)

# Helper function to download a file from a URL
def download_file(url):
    response = requests.get(url)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(response.content)
        return tmp_file.name

def main():
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-color: #9FC4C0; /* Matching the background color from home page */
        }
        .st-emotion-cache-13ln4jf {
            max-width: none !important; /* Remove max-width limitation */
        }
        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }
        .stButton>button {
            background-color: #9FC4C0;
            color: white;
            margin: 0;
            border: 1px solid #2F2F2F; /* Add border around the button */;
        }
        .stButton>button:hover {
            background-color: #333333; /* Change to desired hover color */
            color: white;
        }
        .stButton>button:active {
            background-color: #666666; /* Change to desired active color */
            color: white;
        }
        .stSuccess {
            color: #4CAF50; /* Green color for success message */
        }
        .title {
            font-family: 'Verdana', sans-serif;
            color: white;
            text-align: center;
            font-size: 50px; /* Larger font size for the title */
        }
        .subtitle {
            font-family: 'Verdana', sans-serif;
            color: white;
            text-align: center;
            font-size: 20px; /* Smaller font size for the subtitle */
            margin-top: -10px; /* Adjust margin to bring it closer to the title */
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .fixed-button-container {
            position: fixed;
            top: 10px;
            left: 10px;
            z-index: 1000;
        }
        input[type="text"], input[type="number"], select, textarea {
            border: none !important;
            box-shadow: none !important;
            outline: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Fixed button container for Home button
    st.markdown('<div class="fixed-button-container">', unsafe_allow_html=True)
    if st.button('Accueil', key='home_button'):
        st.session_state.page = 'main'
        st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if 'page' not in st.session_state:
        st.session_state.page = 'main'

    # Display the selected page
    if st.session_state.page == 'main':
        display_home_page()
    else:
        if st.session_state.page == 'liver':
            liver_page()
        elif st.session_state.page == 'heart':
            heart_page()
        elif st.session_state.page == 'kidney':
            kidney_page()
        elif st.session_state.page == 'diabetes':
            diabetes_page()
        elif st.session_state.page == 'breast_cancer':
            breast_cancer_page()

def display_home_page():
    st.markdown('<h1 class="title">HORIZON SAIN</h1>', unsafe_allow_html=True)
    st.write("")
    st.markdown("<h3 class='subtitle'>Bienvenue sur notre plateforme de détection des maladies.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 class='subtitle'>Chez Horizon-Sain, nous fournissons aux professionnels de la santé des solutions de diagnostic de pointe, alliant confort des patients et analyses de données pour des estimations rigoureuses des probabilités de maladies.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 class='subtitle'>Entrez les résultats d'analyses sanguines pour obtenir une prédiction précise de la présence éventuelle de maladies.</h3>", unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/photo_horizon.png", use_column_width=True)
    display_navigation_buttons('home')

def display_navigation_buttons(page_suffix):
    # Navigation buttons
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col2, col3, col4, col5, col6 = st.columns(5)  # Removed col1 for "Accueil"
    with col2:
        if st.button('Maladie du Foie', key=f'liver_button_{page_suffix}_{st.session_state.page}'):
            st.session_state.page = 'liver'
            st.experimental_rerun()
    with col3:
        if st.button('Maladie Cardiaque', key=f'heart_button_{page_suffix}_{st.session_state.page}'):
            st.session_state.page = 'heart'
            st.experimental_rerun()
    with col4:
        if st.button('Maladie Rénale', key=f'kidney_button_{page_suffix}_{st.session_state.page}'):
            st.session_state.page = 'kidney'
            st.experimental_rerun()
    with col5:
        if st.button('Diabète', key=f'diabetes_button_{page_suffix}_{st.session_state.page}'):
            st.session_state.page = 'diabetes'
            st.experimental_rerun()
    with col6:
        if st.button('Cancer du Sein', key=f'brest_cancer_button_{page_suffix}_{st.session_state.page}'):
            st.session_state.page = 'breast_cancer'
            st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def liver_page():
    st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/photo_horizon.png", use_column_width=True)
    display_navigation_buttons('liver')
    st.markdown('<h3 class="subtitle">Détection de la Maladie Chronique du Foie</h3>', unsafe_allow_html=True)

    # Download and load model
    filename = download_file('https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/models/foiet.sav')
    foie_model = joblib.load(filename)

    # Create the input form below the container
    with st.form(key='liver_form'):
        # Define age range
        age_range = list(range(1, 100))  # assuming age range is from 1 to 99

        # Split Columns
        col1, col2, col3, col4, col5 = st.columns(5)

        with col2:
            Age = st.selectbox('Saisissez votre âge', age_range)
            Genre = st.selectbox('Genre', ('Homme', 'Femme'))
            Gender_Male = 1 if Genre == 'Homme' else 0
            Gender_Female = 1 if Genre == 'Femme' else 0
            Total_Bilirubin = st.number_input('Taux de Bilirubine')
        with col4:    
            Alkaline_Phosphotase = st.number_input("Taux d'Alkaline Phosphotase")
            Alamine_Aminotransferase = st.number_input("Taux d'alamine aminotransferase")
            Albumin_and_Globulin_Ratio = st.number_input('Ratio Alubumine / Globuline')

        # Center the submit button
        col_center = st.columns([3, 1, 3])
        with col_center[1]:
            submit_button = st.form_submit_button(label='Prédiction de la maladie du foie')

    # Prediction
    if submit_button:
        input_data = np.array([[Age, Total_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Albumin_and_Globulin_Ratio, Gender_Female, Gender_Male]])
        foie_prediction = foie_model.predict(input_data)

        if foie_prediction[0] == 1:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/foie.png")
            st.markdown('<div class="center"><p style="color: red; font-size: 24px;">Suspicion détectée</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires suggèrent une prob
