import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def app():
    st.title('Simulation 3')

    st.write('The Sensitivity of distrubution of Token A is presented below with the parameter "weight_Token_B": (0.5, 0.99).')


    # Load dataset
    df3 = pd.read_csv('./data/Simulation 3_weight_Token_B 0.5 - 0.99 - Sheet1.csv')

    # Chart building
    fig3 = px.line(
        df3,
        title='Sensitivity of distrubution of Token_A - Parameter: Weight of Token B (0.5 -> 0.99)',
        x='timestep',
        y='balance_of_Token_A',
        color='par_weight_token_B',
        animation_frame='par_weight_token_B',
        height=450, width=1000)
    st.plotly_chart(fig3)
