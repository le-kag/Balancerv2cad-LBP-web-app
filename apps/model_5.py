import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def app():
    st.title('Simulation 5')

    st.write('The Sensitivity of distrubution of Token A is presented below with the parameter: Swap Fees.')

    # Load dataset
    df5 = pd.read_csv("./data/Simulation 5 _ Swap fee - Sheet1.csv")

    fig5 = px.line(
        df5,
        title='Sensitivity of distrubution of Token_A - Parameter: Swap Fees',
        x='timestep',
        y='balance_of_Token_A',
        color='par_swap_fee',
        animation_frame='par_swap_fee',
        height=450, width=800)
    st.plotly_chart(fig5)
