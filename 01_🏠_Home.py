import streamlit as st

# Full size page
st.set_page_config(
    page_title = "ANALYSE - PROFIL FORCE-VITESSE",
    page_icon = "🔬",
    layout="wide")

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")

# Hide Hamburger (Top Right Corner) and "Made with Streamlit" footer:
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.markdown(f'<h1 style="background-color:#6497b1;border-radius:14px;text-align:center;">{"APPLICATION | PROFIL FORCE - VITESSE"}</h1>', unsafe_allow_html=True)
f"*version 2.10 - par Corentin Casali*"
f"""Bienvenue dans l'application profil force-vitesse. Vous trouverez dans le menu à gauche 2 onglets, vous permettant de traiter vos fichiers de profil force-vitesse.\n
Vous pouvez utilisez des **fichiers .tdms** ou alors des **fichiers .xls** \n
⚠️ À l'heure actuelle, aucun paramètre concernant le vélo ne peut être régler. 
"""

st.info("""Des informations sont disponibles dans les différents onglets. N'hésitez pas à jeter un coup d'oeil !

Si vous avez des problèmes, merci de contacter : corentin.casali@univ-st-etienne.fr
""", icon="ℹ️")