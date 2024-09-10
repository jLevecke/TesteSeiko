from os import write
from numpy.core.fromnumeric import size
import streamlit as st
import streamlit_survey as ss
import pandas as pd
from PIL import image

survey = ss.StreamlitSurvey()

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.markdown("""
<style>
   p {
      font-size: 28px;
      text-align: center; 
      
   }
</style>
""", unsafe_allow_html=True)
    
def disable():
    st.session_state.disabled = True

if "disabled" not in st.session_state:
    st.session_state.disabled = False
    
st.title("Pesquisa de satisfação")

with st.form(key="pesquisa_satisfacao"):
    input_nome = survey.text_input(
         "Insira seu nome:"
)
    input_experiencia = survey.select_slider(
        "Em uma escala de 0 a 10, como você avaliaria sua experiência em nosso espaço?", options=["0", "1", "2", "3", "3", "5", "6", "7", "8", "9", "10"], id="Q2"
)
    input_desempenho = survey.select_slider(
        "Como você avalia nosso desempenho em solucionar suas necessidades?", options=["0", "1", "2", "3", "3", "5", "6", "7", "8", "9", "10"], id="Q3"
)
    input_retorno = survey.radio(
        "Você voltaria ao nosso consultório em outra oportunidade?", options=["👍", "👎"], horizontal=True, id="Q4"
)
    
    col1, col2, col3 = st.columns([2,1,2])

    with col1:
        pass

    with col2:
        input_submit = st.form_submit_button("Enviar", on_click=disable, disabled=st.session_state.disabled)
         
    with col3:
        pass
    

if input_submit:
        st.info("Obrigado por enviar sua avaliação")

