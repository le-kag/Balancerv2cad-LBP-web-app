import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def app():
    st.title('Simulation 1')

    st.write('The Sensitivity of distrubution of Token A is presented below with the parameter weight_Token_A: (0.5, 0.99).')

    # Load dataset
    df1 = pd.read_csv("./data/Simulation 1 _ Weights_Token_A_0.5_0.99 - Sheet1 (1).csv")

    # Chart building
    fig1 = px.line(
        df1,
        title='Sensitivity of distrubution of Token_A - Parameter: Weight of Token A (0.5 -> 0.99)',
        x='timestep',
        y='balance_of_Token_A',
        color='par_weight_token_A',
        animation_frame='par_weight_token_A',
        height=450, width=1000)
    st.plotly_chart(fig1)
