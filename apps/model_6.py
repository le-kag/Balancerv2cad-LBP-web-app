import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def app():
    st.title('Simulation 6')

    st.write('The Sensitivity of distrubution of Token A is presented below with the parameter: Actors.')

    #Load dataset
    df6 = pd.read_csv("./data/Simulation 6_ Actors - Sheet1.csv")

    # Chart building
    fig6 = px.line(
        df6,
        title='Sensitivity of distrubution of Token_A - Parameter: Actors Trading Volume',
        x='timestep',
        y='balance_of_Token_A',
        color='par_profile_actors',
        animation_frame='par_profile_actors',
        height=450, width=800)
    st.plotly_chart(fig6)
