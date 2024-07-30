import streamlit as st
import numpy as np
import joblib
import pickle

# Streamlit setup
st.set_page_config(
    page_title="HORIZON SAIN",
    layout="wide",
    page_icon='🧪'
)

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
        if st.button('Cancer du Sein', key=f'breast_cancer_button_{page_suffix}_{st.session_state.page}'):
            st.session_state.page = 'breast_cancer'
            st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def liver_page():
    st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/photo_horizon.png", use_column_width=True)
    display_navigation_buttons('liver')
    st.markdown('<h3 class="subtitle">Détection de la Maladie Chronique du Foie</h3>', unsafe_allow_html=True)


    # Load model
    foie_model = pickle.load(open('foiet.sav', 'rb'))

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
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires suggèrent une probabilité de maladie du foie. Des examens complémentaires sont recommandés pour confirmation.</p></div>', unsafe_allow_html=True)
        else:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/foie.png")
            st.markdown('<div class="center"><p style="color: green; font-size: 24px;">Pas de suspicion</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires indiquent une faible probabilité de maladie du foie. Veuillez continuer le suivi médical habituel.</p></div>', unsafe_allow_html=True)


# Placeholder functions for other pages
def heart_page():
    st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/photo_horizon.png", use_column_width=True)
    display_navigation_buttons('heart')
    st.markdown('<h3 class="subtitle">Détection de la Maladie Cardiaque</h3>', unsafe_allow_html=True)

    # Load the heart disease model
    filename = 'https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/models/df_coeur_new.sav'
    coeur_model = joblib.load(filename)

    # Create the input form below the container
    with st.form(key='heart_form'):
        # Define age range
        age_range = list(range(1, 100))

        # Split Columns
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            age = st.selectbox('Entrez votre âge', age_range)
            Douleur = st.number_input('Entrez la douleur ressentie : CP')
            Electro = st.number_input('Entrez le résultat de l\'électrocardiographie : RESTECG')
            Angine = st.number_input('Y a-t-il eu une angine induite par un exercice physique : EXANG')
        with col2:
            Genre = st.selectbox('Entrez votre genre', ['Homme', 'Femme'])
            Pression = st.number_input('Entrez la valeur de la pression arterielle au repos : TRESTBPS')
            FC = st.number_input('Entrez la valeur de la fréquence cardiaque maximale : THALACH')
            Oldpeak = st.number_input('Dépression du segment ST induite par un exercice par rapport au repos : OLDPEAK')
        with col3:
            Cholesterol = st.number_input('Entrez la valeur du cholesterol : CHOL')
            Sucre = st.number_input('Entrez la valeur de sucre dans le sang à jeun : FBS')
            Slope = st.number_input('Valeur de la pente du segment ST à un effort maximal : SLOPE')
            CA = st.number_input('Nombre de vaisseaux majeurs colorés par fluoroscopie : CA')
        with col4:
            Thal = st.number_input('Type de thalassémie : THAL')

        # Center the submit button
        col_center = st.columns([3, 1, 3])
        with col_center[1]:
            submit_button = st.form_submit_button(label='Test de Prédiction Cardiaque')

    # Prediction
    if submit_button:
        # Prepare input data
        input_data = np.array([[age, 
                                1 if Genre == 'Homme' else 0,  # Assuming 'Homme' = 1, 'Femme' = 0
                                Douleur, Pression, Cholesterol, 
                                1 if Sucre > 0 else 0,  # Assuming 'Sucre' > 0 means True
                                Electro, FC, 
                                1 if Angine > 0 else 0,  # Assuming 'Angine' > 0 means True
                                Oldpeak, Slope, CA, Thal]])

        # Perform prediction
        renale_prediction = coeur_model.predict(input_data)

        if renale_prediction[0] == 1:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/coeur.png")  # Add an appropriate heart image
            st.markdown('<div class="center"><p style="color: red; font-size: 24px;">Suspicion détectée</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires suggèrent une probabilité de maladie du cœur. Des examens complémentaires sont recommandés pour confirmation.</p></div>', unsafe_allow_html=True)
        else:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/coeur.png")  # Add an appropriate heart image
            st.markdown('<div class="center"><p style="color: green; font-size: 24px;">Pas de suspicion</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires indiquent une faible probabilité de maladie du cœur. Veuillez continuer le suivi médical habituel.</p></div>', unsafe_allow_html=True)

def kidney_page():
    st.markdown('<h3 class="subtitle">Détection de la Maladie Rénale</h3>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/photo_horizon.png", use_column_width=True)
    display_navigation_buttons('kidney')
    st.markdown('<h3 class="subtitle">Détection de la Maladie Rénale</h3>', unsafe_allow_html=True)


def diabetes_page():
    st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/photo_horizon.png", use_column_width=True)
    display_navigation_buttons('diabetes')
    st.markdown('<h3 class="subtitle">Prédiction du Diabète</h3>', unsafe_allow_html=True)

    # Load the diabetes model
    diabete_model = joblib.load(open('diabete.sav'))

    # Create the input form below the container
    with st.form(key='diabetes_form'):
        # Split Columns
        col1, col2, col3, col4, col5 = st.columns(5)

        with col2:
            Pregnancies = st.number_input('Entrez la valeur des grossesses')
            BloodPressure = st.number_input('Entrez la valeur de la pression artérielle')
            BMI = st.number_input("Entrez la valeur de l'IMC (Indice de Masse Corporelle)")
            Age = st.number_input("Entrez la valeur de l'âge")

        with col4:
            Glucose = st.number_input('Entrez la valeur de la glycémie')
            Insulin = st.number_input("Entrez la valeur de l'insuline")
            DiabetesPedigreeFunction = st.number_input('Entrez la valeur de la fonction de pedigree du diabète', format="%.3f")

        # Center the submit button
        col_center = st.columns([3, 1, 3])
        with col_center[1]:
            submit_button = st.form_submit_button(label='Test de Prédiction du Diabète')

    # Prediction
    if submit_button:
        # Prediction input without SkinThickness
        diabetes_prediction = diabete_model.predict([[Pregnancies, Glucose, BloodPressure, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diabetes_prediction[0] == 1:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/diabete.png")  # Add an appropriate diabetes image
            st.markdown('<div class="center"><p style="color: red; font-size: 24px;">Suspicion détectée</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires suggèrent une probabilité de maladie diabétique. Des examens complémentaires sont recommandés pour confirmation.</p></div>', unsafe_allow_html=True)
        else:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/diabete.png")  # Add an appropriate diabetes image
            st.markdown('<div class="center"><p style="color: green; font-size: 24px;">Pas de suspicion</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires indiquent une faible probabilité de maladie diabétique. Veuillez continuer le suivi médical habituel.</p></div>', unsafe_allow_html=True)

def breast_cancer_page():
    st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/photo_horizon.png", use_column_width=True)
    display_navigation_buttons('breast_cancer')
    st.markdown('<h3 class="subtitle">Prédiction du Cancer du Sein</h3>', unsafe_allow_html=True)

    # Load the breast cancer model
    filename = 'https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/models/seins.sav'
    seins_model = joblib.load(filename)

    # Create the input form below the container
    with st.form(key='breast_cancer_form'):
        # Split Columns
        col1, col2, col3, col4, col5 = st.columns(5)

        with col2:
            Radius = st.number_input('Entrez la valeur de Radius Mean')
            Perimeter = st.number_input('Entrez la valeur de Perimeter Mean')
            Smoothness = st.number_input("Entrez la valeur de Smoothness Mean", format="%.4f")
            Concavity = st.number_input("Entrez la valeur de Concavity Mean", format="%.4f")
            Symmetry = st.number_input("Entrez la valeur de Symmetry Mean", format="%.4f")

        with col4:
            Texture = st.number_input('Entrez la valeur de Texture Mean')
            Area = st.number_input("Entrez la valeur de Area Mean")
            Compactness = st.number_input('Entrez la valeur de Compactness Mean', format="%.4f")
            Concave_point = st.number_input("Entrez la valeur de Concave Point Mean", format="%.5f")
            Fractal = st.number_input("Entrez la valeur de Fractal Dimension Mean", format="%.5f")

        # Center the submit button
        col_center = st.columns([3, 1, 3])
        with col_center[1]:
            submit_button = st.form_submit_button(label='Test de Prédiction du Cancer du sein')

    # Prediction
    if submit_button:
        # Prediction input without SkinThickness
        seins_prediction = seins_model.predict([[Radius, Texture, Perimeter, Area, Smoothness, Compactness, Concavity, Concave_point, Symmetry, Fractal]])

        if seins_prediction[0] == 1:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/seins.png")  # Add an appropriate breast cancer image
            st.markdown('<div class="center"><p style="color: red; font-size: 24px;">Suspicion détectée</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires suggèrent une probabilité de cancer du sein. Des examens complémentaires sont recommandés pour confirmation.</p></div>', unsafe_allow_html=True)
        else:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/seins.png")  # Add an appropriate breast cancer image
            st.markdown('<div class="center"><p style="color: green; font-size: 24px;">Pas de suspicion</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires indiquent une faible probabilité de cancer du sein. Veuillez continuer le suivi médical habituel.</p></div>', unsafe_allow_html=True)

def kidney_page():
    st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/photo_horizon.png", use_column_width=True)
    display_navigation_buttons('kidney')
    st.markdown('<h3 class="subtitle">Prédiction de la Maladie Rénale Chronique</h3>', unsafe_allow_html=True)

    # Load the breast cancer model
    filename = 'https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/models/reins.sav'
    reins_model = joblib.load(filename)

    # Create the input form below the container
    with st.form(key='kidney_form'):
        # Split Columns
        col1, col2, col3, col4, col5 = st.columns(5)

        with col2:
            age = st.selectbox('Entrez votre âge', list(range(0, 100)))
            sod = st.number_input('Entrez la valeur du sodium')
            hemo = st.number_input('Entrez la valeur de l\'hémoglobine')
            sg = st.number_input('Entrez la valeur du SG')
            sc = st.number_input('Entrez la valeur du SC')

        with col4:
            bp = st.number_input('Entrez la valeur de la pression artérielle')
            pot = st.number_input('Entrez la valeur du potassium')
            al = st.number_input('Entrez la valeur de l\'albumine')
            su = st.number_input('Entrez la valeur du SU')

        # Center the submit button
        col_center = st.columns([3, 1, 3])
        with col_center[1]:
            submit_button = st.form_submit_button(label='Test de Prédiction de la Maladie Rénale')

    # Prediction
    if submit_button:
        # Prediction input without SkinThickness
        reins_prediction = reins_model.predict([[age,sod, hemo, sg, sc, bp, pot, al, su ]])

        if reins_prediction[0] == 1:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/reins.png")  # Add an appropriate breast cancer image
            st.markdown('<div class="center"><p style="color: red; font-size: 24px;">Suspicion détectée</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires suggèrent une probabilité de maladie rénale. Des examens complémentaires sont recommandés pour confirmation.</p></div>', unsafe_allow_html=True)
        else:
            col_center = st.columns([3, 1, 3])
            with col_center[1]:
                st.image("https://raw.githubusercontent.com/Shirley23H/horizon_sain/main/pictures/reins.png")  # Add an appropriate breast cancer image
            st.markdown('<div class="center"><p style="color: green; font-size: 24px;">Pas de suspicion</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="center"><p style="color: white; font-size: 16px;">Les résultats préliminaires indiquent une faible probabilité de maladie rénale. Veuillez continuer le suivi médical habituel.</p></div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
