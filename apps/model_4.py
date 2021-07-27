import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def app():
    st.title('Simulation 4')

    st.write('The Sensitivity of distrubution of Token A is presented below with the parameter "weight_Token_B": (0.5, 0.01).')

    #Load dataset
    df4 = pd.read_csv("./data/Simulation 4_ weight_Token_B 0.5 -_ 0.01 - Sheet1.csv")

    # Chart building
    fig4 = px.line(
        df4,
        title='Sensitivity of distrubution of Token_A - Parameter: Weight of Token B (0.5 -> 0.01)',
        x='timestep',
        y='balance_of_Token_A',
        color='par_weight_token_B_inverse',
        animation_frame='par_weight_token_B_inverse',
        height=450, width=1000)
    st.plotly_chart(fig4)
